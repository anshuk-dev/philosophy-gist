"""
Session-based Batch Dispatcher for Philosophy Gist.
Dispatches 4 distinct, non-repeating flashcards at 5:00 AM IST and 4 distinct flashcards at 5:00 PM IST.
Guarantees zero content repetition across dispatches, formats cards into high-focus layouts,
and preserves an unbroken dialectical chain.
"""

import os
import sys
import json
import time
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from jinja2 import Environment, FileSystemLoader
from src.mailer import PhilosophyMailer, GMAIL_USER, RECIPIENT_EMAIL
from src.verifier import PhilosophyVerifier

TEMPLATES_DIR = BASE_DIR / "templates"
CONTENT_DIR = BASE_DIR / "content"
ARCHIVE_DIR = BASE_DIR / "archive"
ARCHIVE_HTML_DIR = ARCHIVE_DIR / "html"
ARCHIVE_MD_DIR = ARCHIVE_DIR / "markdown"
SENT_HISTORY_FILE = ARCHIVE_DIR / "sent_history.json"

ARCHIVE_HTML_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_MD_DIR.mkdir(parents=True, exist_ok=True)


class SessionDispatcher:
    """Manages twice-daily 4-card batch dispatches with persistent state."""

    def __init__(self):
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            autoescape=True,
        )
        self.database = self._load_database()
        self.sent_history = self._load_sent_history()

    def _load_database(self) -> Dict[str, Any]:
        db_file = CONTENT_DIR / "database.json"
        with open(db_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _load_sent_history(self) -> Dict[str, Any]:
        if SENT_HISTORY_FILE.exists():
            try:
                with open(SENT_HISTORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"sent_card_ids": [], "history": []}

    def _save_sent_history(self):
        with open(SENT_HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.sent_history, f, indent=2, ensure_ascii=False)

    def get_current_session(self) -> str:
        """Determines if the current run is the Morning (5 AM IST) or Evening (5 PM IST) session."""
        # Calculate current time in IST (UTC + 5:30)
        utc_now = datetime.datetime.now(datetime.timezone.utc)
        ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
        # If hour is between 0 and 12, it's morning; otherwise evening
        if ist_now.hour < 12:
            return "morning_5am"
        else:
            return "evening_5pm"

    def select_next_batch(self, count: int = 4) -> List[Dict[str, Any]]:
        """
        Selects `count` unique flashcards that have not yet been sent.
        Balances Indian and Western philosophy (e.g. 2 Indian + 2 Western).
        """
        all_cards = self.database.get("flashcards", [])
        sent_ids = set(self.sent_history.get("sent_card_ids", []))

        # Check if we need to reset cycle because all cards have been exhausted
        available = [c for c in all_cards if c["id"] not in sent_ids]
        if len(available) < count:
            print(f"[STATE] Notice: Only {len(available)} un-sent cards remain. Resetting curriculum cycle!")
            self.sent_history["sent_card_ids"] = []
            sent_ids = set()
            available = list(all_cards)

        # Separate by tradition for balanced delivery
        ind_pool = [c for c in available if c.get("tradition") == "Indian"]
        west_pool = [c for c in available if c.get("tradition") == "Western"]

        selected = []
        # Target: half Indian, half Western
        target_ind = count // 2
        target_west = count - target_ind

        for c in ind_pool[:target_ind]:
            selected.append(c)
        for c in west_pool[:target_west]:
            selected.append(c)

        # If one pool was short, fill from remaining available
        if len(selected) < count:
            for c in available:
                if c not in selected:
                    selected.append(c)
                if len(selected) == count:
                    break

        return selected

    def render_flashcard_html(
        self,
        card: Dict[str, Any],
        session_title: str,
        index: int,
        total: int,
        recipient: str,
    ) -> str:
        template = self.jinja_env.get_template("single_flashcard_email.html")
        return template.render(
            card=card,
            session_title=session_title,
            flash_index=index,
            flash_total=total,
            recipient_email=recipient,
        )

    def render_flashcard_markdown(
        self,
        card: Dict[str, Any],
        session_title: str,
        index: int,
        total: int,
    ) -> str:
        lines = [
            f"# {session_title} &bull; Flash {index} of {total}",
            f"## {card['concept_name']} ({card['tradition']} Philosophy)",
            f"**School:** {card['school']} | **Unit:** {card['unit_id']}\n",
            "### 🔗 Conceptual Chain (Dialectical Lineage)",
            f"- **1. Origin / Prior Knot:** {card['chain']['from_concept']}",
            f"- **2. Current Core Pivot:** **{card['chain']['current_thesis']}**",
            f"- **3. Next Horizon:** {card['chain']['to_concept']}\n",
            "### 🎯 The Fundamental Dilemma",
            f"> \"{card['the_problem']}\"\n",
            "### 🏛️ Canonical Technical Lexicon",
        ]
        for item in card["technical_lexicon"]:
            lines.append(f"- **{item['term']}**: {item['meaning']}")

        lines.extend([
            "\n### ⚔️ The Dialectic: Objection & Resolution",
            f"**Pūrvapakṣa (Opponent):** {card['dialectic']['purvapaksha']}\n",
            f"**Siddhānta (Defense):** {card['dialectic']['siddhanta']}\n",
            "### 📜 Primary Textual Locus",
            f"- **Author:** {card['primary_text']['author']}",
            f"- **Work:** *{card['primary_text']['work']}*",
            f"- **Passage:** {card['primary_text']['passage']}\n",
            "### ⚠️ Central University Interview & UGC NET Trap",
            f"> {card['interview_trap']}\n",
            "### 💡 Wisdom Gist",
            f"> \"{card['wisdom_gist']}\"\n",
        ])
        return "\n".join(lines)

    def run_session(
        self,
        session_type: Optional[str] = None,
        count: int = 4,
        dry_run: bool = False,
        recipient: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Executes a 4-mail batch dispatch for the morning or evening session.
        """
        chosen_session = session_type if session_type in ["morning_5am", "evening_5pm"] else self.get_current_session()
        target_recipient = recipient or RECIPIENT_EMAIL or "anshukumar64149@gmail.com"

        if chosen_session == "morning_5am":
            session_display = "☀️ 5:00 AM MORNING FLASH"
            tag = "5 AM"
        else:
            session_display = "🌙 5:00 PM EVENING FLASH"
            tag = "5 PM"

        print("=" * 65)
        print(f"🏛️  PHILOSOPHY GIST &mdash; {session_display} BATCH")
        print(f"[*] Target Recipient: {target_recipient}")
        print(f"[*] Mode: {'DRY-RUN (Preview Only)' if dry_run else 'LIVE SMTP TRANSMISSION'}")
        print("=" * 65)

        batch_cards = self.select_next_batch(count=count)
        print(f"[*] Selected {len(batch_cards)} non-repeating concept flashcards:")
        for idx, c in enumerate(batch_cards, 1):
            print(f"    {idx}. [{c['tradition'][:3].upper()}] {c['concept_name']} ({c['school']})")

        mailer = PhilosophyMailer()
        mailer.recipient = target_recipient
        results = []

        for idx, card in enumerate(batch_cards, 1):
            # Validate card
            valid, errs = PhilosophyVerifier.validate_flashcard(card)
            if not valid:
                print(f"[!] Warning: Card {card['id']} had validation issues: {errs}")

            # Render HTML and Markdown
            html_text = self.render_flashcard_html(card, session_display, idx, count, target_recipient)
            md_text = self.render_flashcard_markdown(card, session_display, idx, count)

            # Archive locally
            date_str = datetime.datetime.now().strftime("%Y%m%d")
            archive_prefix = f"{date_str}_{chosen_session}_flash_{idx}_{card['id']}"
            html_path = ARCHIVE_HTML_DIR / f"{archive_prefix}.html"
            md_path = ARCHIVE_MD_DIR / f"{archive_prefix}.md"

            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_text)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_text)

            # Build subject
            subject_title = f"[{tag} Flash {idx}/{count}] {card['school']}: {card['concept_name']}"
            issue_stub = {
                "issue_number": f"{tag}-{date_str}-{idx}",
                "title": f"{card['school']}: {card['concept_name']}",
            }

            # Send Email
            print(f"[*] Delivering [{idx}/{count}]: {subject_title}...")
            dispatch_res = mailer.send_newsletter(
                issue_data=issue_stub,
                html_content=html_text,
                text_content=md_text,
                dry_run=dry_run,
            )
            dispatch_res["card_id"] = card["id"]
            results.append(dispatch_res)

            # Register as sent if not dry run
            if not dry_run and dispatch_res.get("status") == "sent":
                if card["id"] not in self.sent_history["sent_card_ids"]:
                    self.sent_history["sent_card_ids"].append(card["id"])

            # Polite pause between sends to comply with SMTP rate limits
            if not dry_run and idx < count:
                time.sleep(2.5)

        # Record session in history
        session_record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "session": chosen_session,
            "cards_sent": [c["id"] for c in batch_cards],
            "dry_run": dry_run,
            "success_count": sum(1 for r in results if r.get("status") in ["sent", "dry_run_success"]),
        }
        self.sent_history["history"].append(session_record)
        self._save_sent_history()

        print("=" * 65)
        print(f"[✓] Session completed! {session_record['success_count']}/{count} flashcards delivered/rendered.")
        print(f"[✓] Total unique cards dispatched to date: {len(self.sent_history['sent_card_ids'])}")
        print("=" * 65)
        return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Philosophy Gist 4-Mail Session Dispatcher")
    parser.add_argument("--session", choices=["morning_5am", "evening_5pm", "auto"], default="auto")
    parser.add_argument("--count", type=int, default=4)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--recipient", type=str, default=None)
    args = parser.parse_args()

    dispatcher = SessionDispatcher()
    dispatcher.run_session(
        session_type=args.session if args.session != "auto" else None,
        count=args.count,
        dry_run=args.dry_run,
        recipient=args.recipient,
    )
