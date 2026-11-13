#!/usr/bin/env python3
"""
Philosophy Gist Dispatcher.
Autonomous server script for scheduled execution via GitHub Actions or local cron.
Verifies academic integrity, compiles daily flashcards, archives, and delivers to anshukumar64149@gmail.com.
"""

import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.generator import IssueGenerator
from src.verifier import PhilosophyVerifier
from src.mailer import PhilosophyMailer, DISPATCH_LOG_FILE


def determine_next_issue_index() -> int:
    """Reads dispatch_log.json to determine the next sequential issue index."""
    import json
    if DISPATCH_LOG_FILE.exists():
        try:
            with open(DISPATCH_LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
            if logs:
                last_num = int(logs[-1].get("issue_number", 0))
                return last_num
        except Exception:
            pass
    return 0


def main():
    parser = argparse.ArgumentParser(description="Philosophy Gist Academic Newsletter Dispatcher")
    parser.add_argument("--issue", type=int, default=None, help="Specific issue index to compile (0-based)")
    parser.add_argument("--verify-only", action="store_true", help="Run academic verifier on database and exit")
    parser.add_argument("--dry-run", action="store_true", help="Generate issue and log without sending SMTP email")
    parser.add_argument("--recipient", type=str, default=None, help="Override recipient email address")
    args = parser.parse_args()

    print("=" * 60)
    print("🏛️  DU PHILOSOPHY GIST &mdash; ACADEMIC DISPATCH ENGINE")
    print("=" * 60)

    generator = IssueGenerator()

    # 1. Full Database Verification
    cards = generator.database.get("flashcards", [])
    print(f"[*] Verifying {len(cards)} flashcards in academic database...")
    all_valid = True
    for card in cards:
        valid, errs = PhilosophyVerifier.validate_flashcard(card)
        if not valid:
            all_valid = False
            print(f"[!] Verification failed for {card.get('id')}: {errs}")

    if all_valid:
        print("[✓] All database flashcards passed 6-dimension academic verification!")
    else:
        print("[✗] Database contains validation errors. Please check above.")
        if args.verify_only:
            sys.exit(1)

    if args.verify_only:
        print("[✓] Verification complete. Exiting.")
        sys.exit(0)

    # 2. Select Issue Index
    issue_idx = args.issue if args.issue is not None else determine_next_issue_index()
    print(f"[*] Preparing Issue Index: {issue_idx} (Edition #{issue_idx + 1:03d})...")

    # 3. Generate Issue Content
    recipient = args.recipient if args.recipient else "anshukumar64149@gmail.com"
    gen_result = generator.generate(index=issue_idx, recipient_email=recipient)
    issue_data = gen_result["issue_data"]

    # 4. Verify Edition
    ed_valid, ed_errs = PhilosophyVerifier.validate_edition(issue_data)
    if not ed_valid:
        print(f"[!] Edition validation warnings: {ed_errs}")
    else:
        print("[✓] Daily Edition passed comparative & syllabus checks!")

    print(f"[*] Title: {issue_data['title']}")
    print(f"[*] Flashcard 1: {issue_data['cards'][0]['concept_name']} ({issue_data['cards'][0]['school']})")
    print(f"[*] Flashcard 2: {issue_data['cards'][1]['concept_name']} ({issue_data['cards'][1]['school']})")

    # 5. Dispatch / Delivery
    mailer = PhilosophyMailer()
    if args.recipient:
        mailer.recipient = args.recipient

    res = mailer.send_newsletter(
        issue_data=issue_data,
        html_content=gen_result["html_content"],
        text_content=gen_result["markdown_content"],
        dry_run=args.dry_run,
    )

    print(f"[✓] Dispatch Status: {res['status']}")
    print(f"[✓] HTML Archive: {gen_result['html_path']}")
    print(f"[✓] Markdown Archive: {gen_result['md_path']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
