# 🏛️ DU Philosophy Gist: Academic Flashcard Dispatch Engine
**Twice-Daily Preparation Server for Central University Assistant Professor & UGC NET / JRF (Philosophy)**

[![Philosophy Gist Scheduled Flashcards](https://github.com/anshuk-dev/philosophy-gist/actions/workflows/daily_dispatch.yml/badge.svg)](https://github.com/anshuk-dev/philosophy-gist/actions/workflows/daily_dispatch.yml)
[![Schedule](https://img.shields.io/badge/Schedule-5%3A00%20AM%20%26%205%3A00%20PM%20IST-blueviolet.svg)](#-delivery-schedule)
[![Volume](https://img.shields.io/badge/Daily%20Volume-8%20Flashcards%20%284%20%2B%204%29-success.svg)](#-delivery-schedule)
[![Curriculum](https://img.shields.io/badge/Curriculum-UGC%20NET%20%7C%20DU%20Faculty-informational.svg)](content/syllabus_mapping.json)

---

## 📖 Overview

**Philosophy Gist** is an autonomous academic dispatch server designed for candidates preparing for **Assistant Professor appointments in Central Universities** (University of Delhi, JNU, BHU, University of Hyderabad) and **UGC NET / JRF Philosophy (Subject Code 03)**.

Every day, the system delivers **8 unique, non-repeating concept flashcards** divided into two dedicated reading sessions:
- **☀️ Morning Session (05:00 AM IST)**: 4 distinct flashcard emails
- **🌙 Evening Session (05:00 PM IST)**: 4 distinct flashcard emails

Every email is delivered as its own individual, bite-sized flashcard formatted in an ultra-focused, high-contrast layout, complete with an **unbroken conceptual chain** showing the dialectical evolution of ideas.

---

## 🔗 Chained Concepts: From Origin to Horizon

No philosophical concept exists in a vacuum. Every flashcard is explicitly anchored in its dialectical lineage:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 🔗 CONCEPTUAL CHAIN (DIALECTICAL LINEAGE)                              │
│ 1. Origin / Prior Knot:  Cārvāka Skepticism (Doubt of unperceived)     │
│ 2. Core Pivot (Current): Cognition carries intrinsic validity (Svataḥ) │
│ 3. Next Horizon:         Theories of Illusion (Khyātivāda)             │
└────────────────────────────────────────────────────────────────────────┘
```

This continuous chaining trains candidates to answer complex viva-voce and interview panel questions that trace the historical development of thought from one school to another.

---

## ⚡ The 6-Dimension High-Focus Flashcard Layout

Every flashcard cuts through empty jargon to present the concentrated essence:

1. **The Fundamental Dilemma**: The core epistemological or metaphysical tension stated in 1 crisp sentence.
2. **Canonical Vocabulary (Precision Lexicon)**: Sanskrit (with IAST diacritics), Greek, and German terms with their authentic philosophical scope.
3. **The Dialectic**: A sharp juxtaposition between **Pūrvapakṣa** (the opponent's strongest objection) and **Siddhānta** (the definitive philosophical defense).
4. **Primary Textual Locus**: Direct citation of root texts (*sūtra*, *bhāṣya*, or published treatise with chapter/verse).
5. **⚠️ Central University Interview Trap**: Subtle distinction, sub-school variance, or common pitfall where selection committees test deep mastery versus superficial memorization.
6. **Wisdom Gist**: The existential, contemplative truth connecting ancient rigor to human consciousness.

---

## ⏰ Delivery Schedule & Zero-Repetition Engine

| Session | Time (IST) | Time (UTC) | Volume | Content Balance |
|---|---|---|---|---|
| **Morning Briefing** | **05:00 AM** | 23:30 (prev. day) | 4 Separate Emails | 2 Indian + 2 Western (Chained) |
| **Evening Briefing** | **05:00 PM** | 11:30 | 4 Separate Emails | 2 Indian + 2 Western (Chained) |

### Zero-Repetition State Tracking:
All delivered card IDs are recorded in [`archive/sent_history.json`](archive/sent_history.json). The engine verifies that **no concept is ever repeated** until the entire curriculum database has been completely traversed.

---

## 📂 Repository Structure

```
Philosophy Gist/
├── .github/
│   └── workflows/
│       └── daily_dispatch.yml       # Scheduled server (5 AM & 5 PM IST)
├── content/
│   ├── database.json                # Curated & verified curriculum flashcard database
│   ├── syllabus_mapping.json        # 6 Units of UGC NET / CU syllabus
│   └── cache/                       # Cached articles and references
├── src/
│   ├── session_dispatcher.py        # 4-mail morning & evening session engine
│   ├── verifier.py                  # 6-dimension academic validation engine
│   ├── generator.py                 # Markdown & HTML issue compiler
│   ├── mailer.py                    # SMTP delivery engine with rate-limit pacing
│   └── scraper.py                   # SEP / IEP scraper & local notes search
├── templates/
│   ├── single_flashcard_email.html  # High-focus, distraction-free flashcard layout
│   └── newsletter.html              # Combined digest template
├── archive/
│   ├── sent_history.json            # Persistent tracking ensuring zero repetition
│   ├── html/                        # HTML archive of every dispatched flashcard
│   └── markdown/                    # Plain text / Markdown archive
├── run_dispatch.py                  # Primary entrypoint script
├── ROADMAP.md                       # 120-Day systematic curriculum progression
└── requirements.txt                 # Dependencies
```

---

## 🛠️ CLI Commands & Testing

### 1. Verify Database Academic Integrity
```bash
python run_dispatch.py --verify-only
```

### 2. Test 4-Card Dispatch in Dry-Run Mode
```bash
# Preview 5 AM Morning Session (4 emails)
python run_dispatch.py --session morning_5am --dry-run

# Preview 5 PM Evening Session (4 emails)
python run_dispatch.py --session evening_5pm --dry-run
```

### 3. Dispatch Live 4-Card Session Locally
```bash
python run_dispatch.py --session morning_5am
```

### 4. Trigger via GitHub Actions Cloud Runner
```bash
gh workflow run daily_dispatch.yml -f session=morning_5am -f count=4
```
