"""
Issue Generator for Philosophy Gist Newsletter.
Pairs verified Indian and Western philosophy cards, constructs practice questions,
and renders both GitHub-grade responsive HTML and standalone Markdown archives.
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
CONTENT_DIR = BASE_DIR / "content"
ARCHIVE_MD_DIR = BASE_DIR / "archive" / "markdown"
ARCHIVE_HTML_DIR = BASE_DIR / "archive" / "html"

ARCHIVE_MD_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_HTML_DIR.mkdir(parents=True, exist_ok=True)


class IssueGenerator:
    """Compiles daily philosophical editions."""

    def __init__(self):
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            autoescape=True,
        )
        self.database = self._load_database()

    def _load_database(self) -> Dict[str, Any]:
        db_path = CONTENT_DIR / "database.json"
        if not db_path.exists():
            raise FileNotFoundError(f"Database not found at {db_path}")
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_cards_by_pair(self, index: int = 0) -> Dict[str, Any]:
        """
        Pairs one Indian philosophy card and one Western philosophy card based on index.
        """
        cards = self.database.get("flashcards", [])
        indian_cards = [c for c in cards if c.get("tradition") == "Indian"]
        western_cards = [c for c in cards if c.get("tradition") == "Western"]

        ind_card = indian_cards[index % len(indian_cards)]
        west_card = western_cards[index % len(western_cards)]

        issue_num = f"{index + 1:03d}"

        # Standard curated issues with specific synthesis notes & practice MCQs
        curated_issues = [
            {
                "issue_number": "001",
                "title": "The Architecture of Epistemic Trust & Transcendental Cognition",
                "cards": [ind_card, west_card],
                "synthesis_note": (
                    "Both Kumārila Bhaṭṭa's Svataḥ Prāmāṇyavāda and Immanuel Kant's Transcendental Deduction "
                    "rebel against paralyzing skepticism. For the Mīmāṃsaka, skepticism is halted by positing that "
                    "cognition is intrinsically true until actively falsified; for Kant, skepticism is halted by proving "
                    "that the categorical structures of the mind are the very preconditions for an objective world to appear at all. "
                    "Both recognize that knowledge cannot be justified from a neutral, detached vantage point outside experience itself."
                ),
                "practice_questions": [
                    {
                        "question": "According to Bhāṭṭa Mīmāṃsā, how is the validity (prāmāṇya) of a cognition known?",
                        "options": [
                            "(A) Directly perceived simultaneously with the object via Sākṣī",
                            "(B) Inferred from the 'knownness' (jñātatā) produced in the object",
                            "(C) Verified exclusively through pragmatic success (pravṛtti-sāmarthya)",
                            "(D) Ascertained by an extraordinary divine perception (Alaukika Pratyakṣa)"
                        ],
                        "correct_option": "(B)",
                        "explanation": "Kumārila Bhaṭṭa holds that cognition is supersensuous (atīndriya); we infer cognition and its intrinsic validity from the property of 'knownness' (jñātatā or prākaṭya) generated in the known object."
                    },
                    {
                        "question": "Which of the following propositions represents a 'Synthetic A Priori' judgment for Kant?",
                        "options": [
                            "(A) All bachelors are unmarried men",
                            "(B) All bodies are extended",
                            "(C) A straight line between two points is the shortest",
                            "(D) The swan in the lake is white"
                        ],
                        "correct_option": "(C)",
                        "explanation": "In the B-Introduction to CPR, Kant explains that 'straight' is a purely qualitative concept containing no notion of magnitude or quantity; that it is 'the shortest' is an ampliative (synthetic) discovery that nonetheless holds with universal necessity (a priori)."
                    }
                ]
            },
            {
                "issue_number": "002",
                "title": "The Metaphysics of Causality: Latency, Emergence & Skeptical Custom",
                "cards": [ind_card, west_card],
                "synthesis_note": (
                    "While Sāṃkhya resolves causation through ontological latency (Satkāryavāda—the effect is the cause unfolded), "
                    "Hume disintegrates the causal nexus altogether into psychological association. For Sāṃkhya, cause and effect "
                    "share identical essence (kāraṇa-bhāva); for Hume, cause and effect are distinct events with zero necessary connection "
                    "discoverable by reason."
                ),
                "practice_questions": [
                    {
                        "question": "Which argument for Satkāryavāda in Sāṃkhyakārikā asserts that 'oil cannot be pressed from sand'?",
                        "options": [
                            "(A) Upādānagrahaṇāt",
                            "(B) Asad-akaraṇāt",
                            "(C) Śaktasya śakya-karaṇāt",
                            "(D) Kāraṇa-bhāvāt"
                        ],
                        "correct_option": "(B)",
                        "explanation": "'Asad-akaraṇāt' (what does not exist cannot be brought into being) establishes that non-existent entities cannot be produced; if the effect were non-existent, even sand would yield oil."
                    },
                    {
                        "question": "Hume locates the origin of our belief in causal necessity in:",
                        "options": [
                            "(A) A priori rational demonstration",
                            "(B) Direct intellectual intuition of power",
                            "(C) Custom or psychological habit of mind",
                            "(D) Innate Cartesian ideas"
                        ],
                        "correct_option": "(C)",
                        "explanation": "Hume concludes that after experiencing constant conjunction, custom or habit alone induces the mind to expect the attendant effect."
                    }
                ]
            }
        ]

        if index < len(curated_issues):
            return curated_issues[index]

        # Generic fallback pairing for future automated rotation
        return {
            "issue_number": issue_num,
            "title": f"Philosophical Dialectics: {ind_card['concept_name']} & {west_card['concept_name']}",
            "cards": [ind_card, west_card],
            "synthesis_note": f"Comparative reflection between {ind_card['school']} and {west_card['school']}.",
            "practice_questions": [
                {
                    "question": f"Which school propounds the doctrine of {ind_card['concept_name']}?",
                    "options": [
                        f"(A) {ind_card['school']}",
                        "(B) Carvaka",
                        "(C) Nyaya",
                        "(D) Samkhya"
                    ],
                    "correct_option": "(A)",
                    "explanation": f"This is the cornerstone thesis of {ind_card['school']}."
                },
                {
                    "question": f"In {west_card['primary_text']['work']}, the primary argument focuses on:",
                    "options": [
                        f"(A) {west_card['concept_name']}",
                        "(B) Skepticism alone",
                        "(C) Dualism alone",
                        "(D) Pure materialism"
                    ],
                    "correct_option": "(A)",
                    "explanation": f"Argued directly in {west_card['primary_text']['work']} by {west_card['primary_text']['author']}."
                }
            ]
        }

    def generate(self, index: int = 0, recipient_email: str = "anshukumar64149@gmail.com") -> Dict[str, Any]:
        """Generates both HTML and Markdown editions and writes them to the archive."""
        issue_data = self.get_cards_by_pair(index)

        # 1. Render HTML
        template = self.jinja_env.get_template("newsletter.html")
        html_content = template.render(
            issue=issue_data,
            recipient_email=recipient_email,
        )

        # 2. Render Markdown
        md_lines = [
            f"# DU Philosophy Gist &mdash; Issue #{issue_data['issue_number']}",
            f"**{issue_data['title']}**\n",
            f"*Dispatched to: {recipient_email}*\n",
            "---",
            "\n## Flashcard 1 (Indian Philosophy)",
            f"### {issue_data['cards'][0]['concept_name']}",
            f"**School:** {issue_data['cards'][0]['school']} | **Unit:** {issue_data['cards'][0]['unit_id']}\n",
            f"**The Problem:**\n> {issue_data['cards'][0]['the_problem']}\n",
            "**Key Lexicon:**",
        ]
        for lex in issue_data['cards'][0]['technical_lexicon']:
            md_lines.append(f"- **{lex['term']}**: {lex['meaning']}")

        md_lines.extend([
            "\n**The Dialectic:**",
            f"- *Pūrvapakṣa (Opponent):* {issue_data['cards'][0]['dialectic']['purvapaksha']}",
            f"- *Siddhānta (Resolution):* {issue_data['cards'][0]['dialectic']['siddhanta']}\n",
            f"**Primary Text:** {issue_data['cards'][0]['primary_text']['author']}, *{issue_data['cards'][0]['primary_text']['work']}* ({issue_data['cards'][0]['primary_text']['passage']})\n",
            f"**⚠️ University Interview Trap:**\n{issue_data['cards'][0]['interview_trap']}\n",
            f"**Wisdom Gist:**\n> \"{issue_data['cards'][0]['wisdom_gist']}\"\n",
            "---",
            "\n## Flashcard 2 (Western Philosophy)",
            f"### {issue_data['cards'][1]['concept_name']}",
            f"**School:** {issue_data['cards'][1]['school']} | **Unit:** {issue_data['cards'][1]['unit_id']}\n",
            f"**The Problem:**\n> {issue_data['cards'][1]['the_problem']}\n",
            "**Key Lexicon:**",
        ])
        for lex in issue_data['cards'][1]['technical_lexicon']:
            md_lines.append(f"- **{lex['term']}**: {lex['meaning']}")

        md_lines.extend([
            "\n**The Dialectic:**",
            f"- *Pūrvapakṣa (Opponent):* {issue_data['cards'][1]['dialectic']['purvapaksha']}",
            f"- *Siddhānta (Resolution):* {issue_data['cards'][1]['dialectic']['siddhanta']}\n",
            f"**Primary Text:** {issue_data['cards'][1]['primary_text']['author']}, *{issue_data['cards'][1]['primary_text']['work']}* ({issue_data['cards'][1]['primary_text']['passage']})\n",
            f"**⚠️ University Interview Trap:**\n{issue_data['cards'][1]['interview_trap']}\n",
            f"**Wisdom Gist:**\n> \"{issue_data['cards'][1]['wisdom_gist']}\"\n",
            "---",
            "\n## Comparative Dialectical Bridge",
            f"{issue_data.get('synthesis_note', '')}\n",
            "---",
            "\n## Central University & UGC NET Practice Questions",
        ])
        for idx, q in enumerate(issue_data.get('practice_questions', []), 1):
            md_lines.append(f"\n**Q{idx}. {q['question']}**")
            for opt in q['options']:
                md_lines.append(f"- {opt}")
            md_lines.append(f"**Answer:** {q['correct_option']} &mdash; *{q['explanation']}*")

        markdown_content = "\n".join(md_lines)

        # 3. Save to Archive
        html_file = ARCHIVE_HTML_DIR / f"issue_{issue_data['issue_number']}.html"
        md_file = ARCHIVE_MD_DIR / f"issue_{issue_data['issue_number']}.md"

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        return {
            "issue_data": issue_data,
            "html_path": str(html_file),
            "md_path": str(md_file),
            "html_content": html_content,
            "markdown_content": markdown_content,
        }


if __name__ == "__main__":
    generator = IssueGenerator()
    res = generator.generate(index=0)
    print(f"Generated Issue #{res['issue_data']['issue_number']}: {res['issue_data']['title']}")
    print(f"HTML saved to: {res['html_path']}")
    print(f"Markdown saved to: {res['md_path']}")
