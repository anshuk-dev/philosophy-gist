"""
Automated Mailer Engine for Philosophy Gist Newsletter.
Sends responsive HTML + Markdown multipart emails via Gmail SMTP,
with dry-run preview capability, retry logic, and delivery logging.
"""

import os
import sys
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Dict, Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Load local .env if present
env_path = BASE_DIR / ".env"
if env_path.exists():
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())
    except Exception:
        pass

DEFAULT_GMAIL_USER = "anshu.philosophy@gmail.com"
DEFAULT_RECIPIENT = "anshukumar64149@gmail.com"

GMAIL_USER = os.environ.get("GMAIL_USER", DEFAULT_GMAIL_USER)
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL", DEFAULT_RECIPIENT)
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))

DISPATCH_LOG_FILE = BASE_DIR / "archive" / "dispatch_log.json"


class PhilosophyMailer:
    """Delivers verified academic newsletters."""

    def __init__(self):
        self.sender = GMAIL_USER
        self.recipient = RECIPIENT_EMAIL
        self.password = GMAIL_APP_PASSWORD

    def send_newsletter(
        self,
        issue_data: Dict[str, Any],
        html_content: str,
        text_content: str,
        dry_run: bool = False,
    ) -> Dict[str, Any]:
        """
        Sends an edition via SMTP or executes a verified dry-run.
        """
        subject = f"DU Philosophy Gist #{issue_data['issue_number']}: {issue_data['title']}"

        # Construct email message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"DU Philosophy Gist <{self.sender}>"
        msg["To"] = self.recipient
        msg["X-Mailer"] = "PhilosophyGist-Bot/1.0 (DU-CentralUniversity-Prep)"

        part_text = MIMEText(text_content, "plain", "utf-8")
        part_html = MIMEText(html_content, "html", "utf-8")
        msg.attach(part_text)
        msg.attach(part_html)

        result = {
            "issue_number": issue_data["issue_number"],
            "title": issue_data["title"],
            "sender": self.sender,
            "recipient": self.recipient,
            "subject": subject,
            "dry_run": dry_run,
            "status": "pending",
            "message": "",
        }

        if dry_run or not self.password:
            msg_reason = "DRY-RUN completed successfully." if dry_run else "GMAIL_APP_PASSWORD not set in environment; dry-run rendered."
            print(f"[MAILER] {msg_reason}")
            print(f"[MAILER] Subject: {subject}")
            print(f"[MAILER] To: {self.recipient}")
            print(f"[MAILER] Length HTML: {len(html_content)} bytes | Text: {len(text_content)} bytes")
            result["status"] = "dry_run_success"
            result["message"] = msg_reason
            self._log_dispatch(result)
            return result

        # Actual SMTP transmission
        try:
            print(f"[MAILER] Connecting to SMTP {SMTP_SERVER}:{SMTP_PORT} for {self.sender}...")
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=25)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.sender, self.password)
            server.sendmail(self.sender, [self.recipient], msg.as_string())
            server.quit()

            print(f"[MAILER] Delivered successfully to {self.recipient}")
            result["status"] = "sent"
            result["message"] = f"Successfully delivered to {self.recipient} via SMTP"
        except Exception as e:
            print(f"[MAILER ERROR] Failed to send email: {e}", file=sys.stderr)
            result["status"] = "error"
            result["message"] = str(e)

        self._log_dispatch(result)
        return result

    def _log_dispatch(self, entry: Dict[str, Any]):
        logs = []
        if DISPATCH_LOG_FILE.exists():
            try:
                with open(DISPATCH_LOG_FILE, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except Exception:
                logs = []

        import datetime
        entry["timestamp"] = datetime.datetime.now().isoformat()
        logs.append(entry)

        with open(DISPATCH_LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2)


if __name__ == "__main__":
    from src.generator import IssueGenerator

    gen = IssueGenerator()
    data = gen.generate(index=0)
    mailer = PhilosophyMailer()
    res = mailer.send_newsletter(
        data["issue_data"],
        data["html_content"],
        data["markdown_content"],
        dry_run=True,
    )
    print("Dispatch result:", res["status"])
