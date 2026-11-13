#!/usr/bin/env python3
"""
Special Dispatch: Latest Philosophical News, SEP Additions & Academic Brief.
Compiles a dense, rigorous philosophical news digest and dispatches via PhilosophyMailer.
"""

import sys
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.mailer import PhilosophyMailer, DISPATCH_LOG_FILE

ARCHIVE_MD_DIR = BASE_DIR / "archive" / "markdown"
ARCHIVE_HTML_DIR = BASE_DIR / "archive" / "html"
ARCHIVE_MD_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_HTML_DIR.mkdir(parents=True, exist_ok=True)

NEWS_BRIEF_DATA = {
    "issue_number": "SPECIAL-2026-11",
    "title": "Contemporary Philosophical Digest: SEP Breakthroughs, Mind & AI Frontiers, and Disciplinary Updates",
    "edition_date": "November 2026",
    "recipient": "anshukumar64149@gmail.com",
    "sections": [
        {
            "category": "DISCIPLINARY HEADLINES & INSTITUTIONAL SHIFTS",
            "items": [
                {
                    "headline": "APA Formally Concludes Virtual Divisional Meetings Experiment",
                    "details": (
                        "The American Philosophical Association (APA) has confirmed the termination of its experiment "
                        "with virtual divisional meetings, mandating a return to strictly in-person conferences (beginning with "
                        "the upcoming Eastern Division meeting in Boston). Institutional audits revealed a ~50% drop in paper "
                        "submissions and severe attrition in spontaneous dialectical engagement and graduate networking during online sessions."
                    ),
                    "significance": "Re-affirms the embodied, dialogical nature of professional philosophical symposiums against technocratic virtualization."
                },
                {
                    "headline": "Marc Sanders Foundation & Journal Editors Address AI in Research",
                    "details": (
                        "Convened to address the deluge of synthetic submissions, journal editors across leading analytic and "
                        "continental publications established unified guidelines. Discussions centered on Kyle van Oosterum’s "
                        "'Simple Principle': AI assistance is ethically permissible only for tasks one would assign to a human "
                        "research assistant (e.g. proofing, transcription, counter-argument probing), with strict non-delegation of epistemic authorship."
                    ),
                    "significance": "Draws an institutional demarcation line between instrumental drafting tools and non-delegable philosophical agency."
                },
                {
                    "headline": "In Memoriam: John Heil (1943–2026) & The Metaphysics of Realism",
                    "details": (
                        "The philosophical community mourns the passing of John Heil, foundational metaphysician and inaugural Editor-in-Chief "
                        "of the Journal of the American Philosophical Association. Heil’s monumental defense of ontological dispositionalism—the "
                        "doctrine that properties are simultaneously qualitative and dispositional ('powers')—fundamentally dismantled the "
                        "Cartesian and Humean orthodoxies of inert matter and categorical-dispositional dualism."
                    ),
                    "significance": "A major theoretical touchstone for physicalists seeking non-reductive accounts of mental causation without emergentist mysteries."
                },
                {
                    "headline": "2027 John Dewey Lectures & Spring 2026 APA Honors",
                    "details": (
                        "Eva Kittay (Stony Brook) awarded Eastern Division Dewey Lecture for pioneering work in disability theory, "
                        "relational ontology, and ethics of care; Elliott Sober (UW-Madison) awarded Central Division Dewey Lecture "
                        "for definitive contributions to the philosophy of evolutionary biology, parsimony (Ockham's Razor), and multi-level selection."
                    ),
                    "significance": "Demonstrates the dual vitality of applied relational ethics and formal philosophy of science in contemporary recognition."
                }
            ]
        },
        {
            "category": "STANFORD ENCYCLOPEDIA OF PHILOSOPHY (SEP) — AUTUMN/WINTER 2026 FRONTIERS",
            "items": [
                {
                    "headline": "Epistemic Closure (Marc Alspector-Kelly, Nov 4, 2026)",
                    "details": (
                        "A critical systemic overhaul of the principle that knowing p and knowing that p implies q entails knowing q. "
                        "The entry formalizes the structural battles between Fred Dretske / Robert Nozick’s counterfactual tracking "
                        "(which reject closure to dissolve radical skepticism) versus neo-Moorean contextualists (Keith DeRose, Stewart Cohen) "
                        "and John Hawthorne / Jason Stanley’s subject-sensitive invariantism that defend closure at all costs."
                    ),
                    "core_formula": "K(p) ∧ K(p → q) ⊢ K(q) vs. Tracking: ¬p □→ ¬B(p)",
                    "relevance": "Direct intersection with classical Indian Svataḥ Prāmāṇyavāda and Nyāya inference verification (Anuvyavasāya)."
                },
                {
                    "headline": "Epistemology of Artificial Intelligence (Oct 16, 2026)",
                    "details": (
                        "Examines the 'Black Box' epistemic opacity problem: whether deep connectionist architectures can confer genuine "
                        "justification or warrant to human believers, or whether relying on deep learning outputs constitutes epistemic deference "
                        "without understanding. Explores algorithmic bias as structural epistemic injustice and whether artificial systems "
                        "can possess non-derived epistemic virtues."
                    ),
                    "relevance": "Reframes the problem of Testimony (Śabda-pramāṇa) in the context of non-human, sub-symbolic stochastic engines."
                },
                {
                    "headline": "Bioethics & Moral Reasoning (Jennifer Flynn, Nov 5, 2026)",
                    "details": (
                        "Dissects the methodological schism between Jonathan Dancy's Radical Moral Particularism (where moral reasons are "
                        "holistic and context-dependent, possessing no invariant valence) and Tom Beauchamp & James Childress's Principlism "
                        "(beneficence, non-maleficence, autonomy, justice), particularly when automating medical triage algorithms."
                    ),
                    "relevance": "Foundational for modern normative ethics debates on rule-consequentialism vs. context-sensitive deontology."
                },
                {
                    "headline": "Saadya Gaon (Gyongyi Hegedus, Nov 12, 2026)",
                    "details": (
                        "New monograph on the 10th-century polymath and architect of Judeo-Arabic rationalism. Focuses on Saadya’s "
                        "The Book of Beliefs and Opinions (Kitāb al-Amānāt wal-I'tiqādāt), establishing an early four-source epistemology: "
                        "sense perception ('ilm al-ḥiss), intellect/axioms ('ilm al-'aql), necessary inference ('ilm al-darūrah), and authentic transmission ('ilm al-khabar al-ṣādiq)."
                    ),
                    "relevance": "Remarkable historical parallel to the Pramāṇa-samuccaya debates in classical Indian epistemology."
                },
                {
                    "headline": "Consequentializing (Douglas W. Portmore, Oct 30, 2026 Revision)",
                    "details": (
                        "Analyzes the provocative meta-normative thesis that any plausible non-consequentialist theory (including Kantianism "
                        "and Rossian intuitionism) can be represented as a version of consequentialism by properly evaluating states of affairs "
                        "from an agent-relative perspective (evaluator-relative consequentialism)."
                    ),
                    "relevance": "Vital for ethics candidates analyzing whether the Bhagavad Gītā’s Niṣkāma Karma can be 'consequentialized'."
                }
            ]
        },
        {
            "category": "PHILOSOPHY OF MIND & ARTIFICIAL CONSCIOUSNESS: THE LIVE DEBATES",
            "items": [
                {
                    "headline": "The 'Copernican Principle' vs. Structural Skepticism (Substrate Chauvinism)",
                    "details": (
                        "Philosophers of mind (advocates of functionalism and panpsychist informationalism) argue that restricting "
                        "phenomenal consciousness exclusively to carbon-based neurobiology constitutes unjustifiable 'substrate chauvinism'. "
                        "In opposition, structural skeptics (Seth, LeCun) argue that transformer architectures lack the integrated causal topology "
                        "(Integrated Information Theory, IIT) and autopoietic homeostatic self-maintenance required for phenomenal experience."
                    ),
                    "dialectic": "Functional Equivalence (Computationalism) vs. Biological Embodiment & Causal-Topological Constraints."
                },
                {
                    "headline": "The 'Fallacy of the Continuum' in AI Intelligence vs. Sentience",
                    "details": (
                        "A critical methodological critique warns against conflating functional intelligence (task solving, theory-of-mind tests, "
                        "synthetic empathy) with phenomenal sentience ('what-it-is-like-ness'). A system may achieve superintelligent strategic "
                        "optimization and linguistic mimicry without possessing a solitary scintilla of inner subjective awareness."
                    ),
                    "ethical_warning": "Anthropomorphic fallacy risks misallocating moral patienthood to automated statistical echoes while ignoring real moral patients."
                },
                {
                    "headline": "The Modernized Chinese Room: Vector Geometry vs. Intrinsic Semantics",
                    "details": (
                        "Contemporary debates update John Searle’s classic 1980 thought experiment. While modern LLMs construct astonishingly dense "
                        "high-dimensional latent spaces mapping conceptual relations, skeptics argue that geometric proximity between vector tokens "
                        "still represents derived, ungrounded syntax—failing to bridge the chasm to Brentano’s intrinsic intentionality ('aboutness')."
                    ),
                    "dialectic": "Latent Space Syntactic Manipulation vs. Phenomenological & Embodied Grounding."
                }
            ]
        }
    ],
    "practice_questions": [
        {
            "question": "In contemporary epistemology, the rejection of the 'Epistemic Closure Principle' was famously adopted by Fred Dretske and Robert Nozick primarily to:",
            "options": [
                "(A) Prove the infallibility of sense perception (Pratyakṣa)",
                "(B) Defeat radical Cartesian skepticism without claiming knowledge of the denial of skeptical hypotheses",
                "(C) Establish that all knowledge requires infinite justificatory regress",
                "(D) Defend classical coherence theories against foundationalism"
            ],
            "correct_option": "(B)",
            "explanation": "By rejecting closure (K(p) ∧ K(p→¬SH) ⊬ K(¬SH)), Nozick argued one can know an ordinary truth (p: 'I have two hands') through tracking, without needing to know the denial of an untracked skeptical hypothesis (¬SH: 'I am not a Brain in a Vat')."
        },
        {
            "question": "According to John Heil’s identity theory of properties in metaphysics (ontological dispositionalism):",
            "options": [
                "(A) Dispositional properties and qualitative properties are identical—every property is essentially both a quality and a power",
                "(B) Mental properties are eliminated entirely in favor of physical behavior",
                "(C) Dispositions are merely linguistic descriptions with no ontological reality",
                "(D) Qualities alone exist, and powers are psychological projections"
            ],
            "correct_option": "(A)",
            "explanation": "Heil rejects the standard dualism between categorical (qualitative) and dispositional properties, asserting that a property’s qualitative nature and its dispositional capacity are identical aspects of a unitary ontological reality."
        },
        {
            "question": "The attempt to formalize non-consequentialist constraints (such as agent-centered duties) within a consequentialist framework by indexing outcomes to the agent is technically termed:",
            "options": [
                "(A) Ethical Egoism",
                "(B) Consequentializing",
                "(C) Prescriptivism",
                "(D) Emotivism"
            ],
            "correct_option": "(B)",
            "explanation": "'Consequentializing' is the meta-normative strategy (pioneered by Dreier and Portmore) that translates deontological rules into evaluator-relative rankings of states of affairs."
        }
    ]
}


def render_html(data: dict) -> str:
    sections_html = ""
    for sec in data["sections"]:
        items_html = ""
        for it in sec["items"]:
            extra_badges = ""
            if "significance" in it:
                extra_badges += f"""<div style="margin-top:8px; padding:8px 12px; background:#F8FAFC; border-left:3px solid #0969DA; font-size:12px; color:#1E293B;">
                    <strong>🏛️ Disciplinary Takeaway:</strong> {it['significance']}
                </div>"""
            if "relevance" in it:
                extra_badges += f"""<div style="margin-top:8px; padding:8px 12px; background:#FEF3C7; border-left:3px solid #D97706; font-size:12px; color:#92400E;">
                    <strong>📖 Curriculum & Canonical Hook:</strong> {it['relevance']}
                </div>"""
            if "dialectic" in it:
                extra_badges += f"""<div style="margin-top:8px; padding:8px 12px; background:#EEF2FF; border-left:3px solid #4F46E5; font-size:12px; color:#312E81;">
                    <strong>⚖️ Dialectical Tension:</strong> {it['dialectic']}
                </div>"""
            if "ethical_warning" in it:
                extra_badges += f"""<div style="margin-top:8px; padding:8px 12px; background:#FEE2E2; border-left:3px solid #DC2626; font-size:12px; color:#991B1B;">
                    <strong>⚠️ Existential & Ethical Hazard:</strong> {it['ethical_warning']}
                </div>"""

            items_html += f"""
            <div style="margin-bottom: 24px; padding-bottom: 18px; border-bottom: 1px dashed #E2E8F0;">
                <h4 style="font-size: 16px; font-weight: 700; color: #0F172A; margin-bottom: 6px;">{it['headline']}</h4>
                <p style="font-size: 14px; line-height: 1.6; color: #334155; margin-bottom: 6px;">{it['details']}</p>
                {extra_badges}
            </div>
            """

        sections_html += f"""
        <div style="margin-bottom: 32px; border: 1px solid #CBD5E1; border-radius: 8px; background: #FFFFFF; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.04);">
            <div style="background: #F1F5F9; padding: 12px 18px; border-bottom: 1px solid #CBD5E1;">
                <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: #0969DA;">
                    {sec['category']}
                </span>
            </div>
            <div style="padding: 20px 18px;">
                {items_html}
            </div>
        </div>
        """

    mcq_html = ""
    for idx, q in enumerate(data["practice_questions"], 1):
        opts = "".join([f"<li style='margin-bottom:4px; font-size:13px; color:#334155;'>{o}</li>" for o in q["options"]])
        mcq_html += f"""
        <div style="margin-bottom: 18px; padding: 14px 16px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 6px;">
            <div style="font-weight: 600; font-size: 13px; color: #0F172A; margin-bottom: 8px;">Q{idx}. {q['question']}</div>
            <ul style="list-style: none; padding-left: 0; margin-bottom: 10px;">{opts}</ul>
            <div style="font-size: 12px; color: #166534; background: #DCFCE7; padding: 6px 10px; border-radius: 4px; display: inline-block;">
                <strong>Correct: {q['correct_option']}</strong> &mdash; {q['explanation']}
            </div>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{data['title']}</title>
</head>
<body style="background-color: #F8FAFC; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #0F172A; margin: 0; padding: 24px 12px;">
  <div style="max-width: 680px; margin: 0 auto; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <div style="background-color: #0F172A; padding: 30px 24px; border-bottom: 4px solid #0969DA; color: #FFFFFF;">
      <div style="display:inline-block; font-size:11px; font-weight:700; letter-spacing:0.1em; text-transform:uppercase; padding:3px 8px; background:#1E293B; color:#38BDF8; border-radius:4px; margin-bottom:10px;">
        🏛️ ACADEMIC DISPATCH &mdash; {data['edition_date']}
      </div>
      <h1 style="font-size: 22px; font-weight: 700; line-height: 1.3; margin: 0 0 8px 0; color: #FFFFFF;">
        {data['title']}
      </h1>
      <p style="color: #94A3B8; font-size: 13px; margin: 0;">
        Curated for Assistant Professor Interviews (DU, JNU, Central Universities) & UGC NET/JRF (Philosophy)
      </p>
    </div>

    <div style="padding: 24px;">
      <div style="background: #F0FDF4; border-left: 4px solid #16A34A; padding: 12px 16px; margin-bottom: 24px; font-size: 13px; color: #14532D; border-radius: 0 6px 6px 0;">
        <strong>📡 High-Density Executive Summary:</strong> A synthesis of late-2026 Stanford Encyclopedia of Philosophy (SEP) entries, professional disciplinary actions from the APA, and cutting-edge debates at the crossroads of Philosophy of Mind and Artificial General Intelligence.
      </div>

      {sections_html}

      <div style="margin-top: 32px; border-top: 2px solid #E2E8F0; padding-top: 20px;">
        <h3 style="font-size: 16px; font-weight: 700; color: #0F172A; margin-bottom: 14px;">
          🎯 Central University & UGC NET Practice Problems
        </h3>
        {mcq_html}
      </div>

      <div style="margin-top: 28px; padding: 16px; background: #F8FAFC; border-radius: 6px; font-size: 11px; color: #64748B; text-align: center; border: 1px solid #E2E8F0;">
        DU Philosophy Gist Dispatcher &bull; Recipient: <strong>{data['recipient']}</strong><br>
        Archived automatically under <code>archive/html/</code> and <code>archive/markdown/</code>.
      </div>
    </div>
  </div>
</body>
</html>"""


def render_markdown(data: dict) -> str:
    md = [
        f"# 🏛️ DU Philosophy Gist: Special Dispatch & Academic Brief",
        f"**{data['title']}**\n",
        f"*Edition: {data['edition_date']} | Dispatched to: {data['recipient']}*\n",
        "---\n",
        "## 📡 Executive Overview",
        "A rigorous, high-density academic briefing covering late-2026 disciplinary milestones, key Stanford Encyclopedia of Philosophy (SEP) revisions, and core dialectical tensions in philosophy of mind and artificial intelligence.\n",
        "---",
    ]

    for sec in data["sections"]:
        md.append(f"\n## 📌 {sec['category']}\n")
        for it in sec["items"]:
            md.append(f"### {it['headline']}")
            md.append(f"{it['details']}\n")
            if "significance" in it:
                md.append(f"> **🏛️ Disciplinary Takeaway:** {it['significance']}")
            if "relevance" in it:
                md.append(f"> **📖 Curriculum & Canonical Hook:** {it['relevance']}")
            if "dialectic" in it:
                md.append(f"> **⚖️ Dialectical Tension:** {it['dialectic']}")
            if "ethical_warning" in it:
                md.append(f"> **⚠️ Existential & Ethical Hazard:** {it['ethical_warning']}")
            md.append("")

    md.extend([
        "---",
        "\n## 🎯 Central University & UGC NET Practice Problems",
    ])
    for idx, q in enumerate(data["practice_questions"], 1):
        md.append(f"\n**Q{idx}. {q['question']}**")
        for opt in q["options"]:
            md.append(f"- {opt}")
        md.append(f"**Answer:** {q['correct_option']} &mdash; *{q['explanation']}*")

    md.append("\n---\n*Archived autonomously by Philosophy Gist Academic Engine.*")
    return "\n".join(md)


def main():
    print("=" * 60)
    print("🏛️ COMPILING PHILOSOPHY NEWS GIST & ACADEMIC BRIEF")
    print("=" * 60)

    html_content = render_html(NEWS_BRIEF_DATA)
    md_content = render_markdown(NEWS_BRIEF_DATA)

    html_path = ARCHIVE_HTML_DIR / "special_news_brief_2026_11.html"
    md_path = ARCHIVE_MD_DIR / "special_news_brief_2026_11.md"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"[✓] HTML archive written: {html_path}")
    print(f"[✓] Markdown archive written: {md_path}")

    # Invoke Mailer
    mailer = PhilosophyMailer()
    issue_info = {
        "issue_number": NEWS_BRIEF_DATA["issue_number"],
        "title": NEWS_BRIEF_DATA["title"],
    }
    res = mailer.send_newsletter(
        issue_data=issue_info,
        html_content=html_content,
        text_content=md_content,
        dry_run=False,
    )

    print("=" * 60)
    print(f"[+] Mailer Status: {res['status']}")
    print(f"[+] Dispatch Message: {res['message']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
