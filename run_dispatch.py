#!/usr/bin/env python3
"""
Philosophy Gist Dispatcher.
Autonomous server entrypoint for scheduled execution via GitHub Actions or local cron.
Dispatches 4 high-focus flashcards at 5:00 AM IST and 4 high-focus flashcards at 5:00 PM IST.
Guarantees zero content repetition across dispatches.
"""

import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.verifier import PhilosophyVerifier
from src.session_dispatcher import SessionDispatcher


def main():
    parser = argparse.ArgumentParser(description="Philosophy Gist Academic Flashcard Dispatcher")
    parser.add_argument("--session", choices=["morning_5am", "evening_5pm", "auto"], default="auto",
                        help="Session mode: morning_5am (5 AM IST), evening_5pm (5 PM IST), or auto-detect")
    parser.add_argument("--count", type=int, default=4,
                        help="Number of distinct flashcard emails to dispatch in this session (default: 4)")
    parser.add_argument("--verify-only", action="store_true",
                        help="Run academic verifier on database and exit")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate issue and log without sending SMTP email")
    parser.add_argument("--recipient", type=str, default=None,
                        help="Override recipient email address")
    args = parser.parse_args()

    dispatcher = SessionDispatcher()

    # 1. Full Database Verification
    cards = dispatcher.database.get("flashcards", [])
    print(f"[*] Verifying {len(cards)} flashcards in academic database...")
    all_valid = True
    for card in cards:
        valid, errs = PhilosophyVerifier.validate_flashcard(card)
        if not valid:
            all_valid = False
            print(f"[!] Verification failed for {card.get('id')}: {errs}")

    if all_valid:
        print(f"[✓] All {len(cards)} database flashcards passed 6-dimension academic verification!")
    else:
        print("[✗] Database contains validation errors. Please check above.")
        if args.verify_only:
            sys.exit(1)

    if args.verify_only:
        print("[✓] Verification complete. Exiting.")
        sys.exit(0)

    # 2. Run Session Batch Dispatch (4 emails per session)
    session_choice = None if args.session == "auto" else args.session
    dispatcher.run_session(
        session_type=session_choice,
        count=args.count,
        dry_run=args.dry_run,
        recipient=args.recipient,
    )


if __name__ == "__main__":
    main()
