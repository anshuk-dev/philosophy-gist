# 🏛️ DU Philosophy Gist: Academic Newsletter & Flashcard Engine
**Autonomous Preparation Server for Central University Assistant Professor & UGC NET / JRF (Philosophy)**

[![Philosophy Gist Daily Academic Dispatch](https://github.com/anshuk-dev/philosophy-gist/actions/workflows/daily_dispatch.yml/badge.svg)](https://github.com/anshuk-dev/philosophy-gist/actions/workflows/daily_dispatch.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Curriculum](https://img.shields.io/badge/Curriculum-UGC%20NET%20%7C%20DU%20Faculty-success.svg)](content/syllabus_mapping.json)

---

## 📖 Overview

**Philosophy Gist** is an automated academic dispatch engine designed to deliver high-yield, authentic philosophical flashcards and dialectical syntheses directly to candidates preparing for **Assistant Professor interviews in Central Universities** (University of Delhi, JNU, BHU, University of Hyderabad) and **UGC NET / JRF Philosophy (Subject Code 03)**.

Each edition is carefully curated, authenticated against canonical primary texts, rendered in a minimalist GitHub-inspired layout, and automatically emailed to **anshukumar64149@gmail.com** on schedule.

---

## ⚡ The 6-Dimension Flashcard Grasp

Unlike shallow summaries or robotic bullet points, every concept is presented with academic depth:

1. **The Core Dilemma (The Problem)**: The fundamental philosophical knot the thinker seeks to untangle.
2. **Technical Lexicon & Vocabulary**: Precise Sanskrit, Greek, or German terms with exact diacritics and semantic scope.
3. **The Dialectic (Pūrvapakṣa vs. Siddhānta)**: The opponent's challenge juxtaposed against the philosophical defense.
4. **Primary Canonical Citation**: Exact root texts (*sūtra*, *bhāṣya*, or published treatise with locus).
5. **⚠️ Central University Interview Trap**: Sub-school nuances and tricky distinctions frequently tested by selection panels.
6. **Wisdom Gist**: The existential and contemplative resonance of the idea for human life.

---

## 📂 Repository Structure

```
Philosophy Gist/
├── .github/
│   └── workflows/
│       └── daily_dispatch.yml      # Autonomous GitHub Actions server (Daily 6:30 AM IST)
├── content/
│   ├── database.json               # Curated & verified curriculum flashcard database
│   ├── syllabus_mapping.json       # 6 Units of UGC NET / CU syllabus
│   └── cache/                      # Scraped & cached SEP / IEP articles
├── src/
│   ├── scraper.py                  # Scraper for SEP, IEP, and local notes
│   ├── verifier.py                 # 6-dimension academic validation engine
│   ├── generator.py                # Compiles HTML newsletter & Markdown archive
│   └── mailer.py                   # SMTP mailer with dry-run & delivery logs
├── templates/
│   └── newsletter.html             # Minimalist, GitHub-grade responsive HTML email
├── archive/
│   ├── markdown/                   # Standalone Markdown editions
│   ├── html/                       # Standalone browsable HTML editions
│   └── dispatch_log.json           # Execution and delivery records
├── run_dispatch.py                 # Primary CLI runner & automation entrypoint
├── ROADMAP.md                      # 120-Day systematic curriculum progression
└── requirements.txt                # Python dependencies
```

---

## 🛠️ Local Usage & Testing

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Verify Academic Integrity of Database
```bash
python run_dispatch.py --verify-only
```

### 3. Generate Dry-Run Preview (Without Sending Email)
```bash
python run_dispatch.py --dry-run
```
This generates the standalone HTML in `archive/html/issue_XXX.html` and Markdown in `archive/markdown/issue_XXX.md`.

### 4. Send Live Email (Local Execution)
Set your environment variables (or place them in a `.env` file):
```bash
export GMAIL_USER="anshu.philosophy@gmail.com"
export GMAIL_APP_PASSWORD="your-16-char-app-password"
export RECIPIENT_EMAIL="anshukumar64149@gmail.com"

python run_dispatch.py
```

---

## 🤖 GitHub Actions Automated Server

The repository runs completely autonomously via GitHub Actions:
- **Schedule**: Executes daily at `01:00 UTC` (**06:30 AM IST**).
- **Manual Trigger**: Can be dispatched on-demand via the GitHub Actions tab (`workflow_dispatch`).
- **Auto-Archiving**: Every dispatched edition is committed and pushed back into `archive/` automatically.

### Required GitHub Secrets:
To enable automated sending from your GitHub repository:
1. Go to **Settings > Secrets and variables > Actions**.
2. Add the following repository secrets:
   - `GMAIL_USER`: `anshu.philosophy@gmail.com`
   - `GMAIL_APP_PASSWORD`: Your 16-character Google App Password ([How to generate](https://myaccount.google.com/apppasswords))
   - `RECIPIENT_EMAIL`: `anshukumar64149@gmail.com`

---

## 🗺️ Syllabus Coverage

- **Unit 01**: Classical Indian Philosophy (Astika & Nastika traditions)
- **Unit 02**: Classical Western Philosophy (Pre-Socratics, Plato, Aristotle, Medieval)
- **Unit 03**: Modern Western Philosophy (Rationalism, Empiricism, Kant, Hegel)
- **Unit 04**: Contemporary Western Philosophy (Phenomenology, Existentialism, Analytic, Positivism)
- **Unit 05**: Contemporary Indian Philosophy (Aurobindo, Ambedkar, Gandhi, Vivekananda, Radhakrishnan)
- **Unit 06**: Epistemology, Logic & Ethics (Pramāṇas, Khyātivāda, Hetvābhāsa, Normative Ethics)

See [ROADMAP.md](ROADMAP.md) for the complete 120-day daily breakdown.
