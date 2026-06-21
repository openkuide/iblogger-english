---
name: iblogger-english
description: "Guidelines, templates, and audit rules for drafting and validating English learning lessons, conversations, and scripts in the iblogger-english repository."
---

# English Learning Path Content Creation & Audit Guidelines

Use this skill when creating, editing, or auditing lesson files, practice scripts, or documentation in the `iblogger-english` project.

---

## 1. Pedagogical Standards (Cycology & Philosophy)

All lessons must implement **Cognitive Learning Cycles** (psychology) and **Pragmatic Utility** (philosophy):

### Psychological Principles
1. **Active Retrieval & Spacing (Cycology)**: Every lesson file must have a `### 🧠 ការអនុវត្ត និងការឆ្លុះបញ្ចាំង (Practice & Reflection)` section. Interleave 1-2 terms from past lessons to trigger spaced repetition memory loops.
2. **Cognitive Scaffolding**: Keep pages modular. Introduce a maximum of 3 grammar points or 10 terms to avoid working memory overload.
3. **Psychological Safety (Compilation Analogy)**: Frame speech and grammar errors as syntax or compiler runtime errors. Explain *why* they happen (e.g. transfer bias) to reduce speaking anxiety.

### Philosophical Principles
1. **Socratic Inquiry**: Introduce lessons with an open-ended inquiry question prompting developers to reflect on the conceptual need for a standard before explaining it.
2. **Pragmatism & Stoic Resilience**: Focus vocabulary and dialogues 100% on real IT tasks (git commits, standups). In dialogue scripts (e.g., asking for help, incident reporting), model objective, calm, and factual language (reflecting Stoic emotional regulation during production fires).
3. **Hermeneutic Symmetry**: Ensure every Khmer paragraph is matched with its English translation block. This symmetry allows learners to understand specific vocabulary (the parts) in relation to the overall meaning (the whole).
4. **Epistemic Scaffolding**: Structure lessons to build from core linguistic axioms (Module 1/2) to technical application (Module 6) and spontaneous expression (Module 7).


---

## 2. Mermaid Diagram Formatting

Always initialize Mermaid diagrams with the dark mode CSS overrides to prevent rendering issues:

```mermaid
%%{init: {
  'theme': 'dark',
  'themeVariables': {
    'background': '#1e1e1e',
    'primaryTextColor': '#ffffff',
    'lineColor': '#a0a0a0',
    'actorBkg': '#2c3e50',
    'actorBorder': '#34495e',
    'actorTextColor': '#ffffff',
    'noteBkgColor': '#2c3e50',
    'noteTextColor': '#ffffff',
    'noteBorderColor': '#34495e'
  },
  'themeCSS': 'svg { background-color: #1e1e1e !important; padding: 1rem !important; border-radius: 8px !important; } .edgeLabel rect { fill: #1e1e1e !important; } text, tspan { fill: #ffffff !important; } .messageText, .messageText tspan, .signalText, .signalText tspan { fill: #ffffff !important; stroke: #1e1e1e !important; stroke-width: 3px !important; paint-order: stroke fill !important; stroke-linejoin: round !important; }'
}}%%
```

### Constraints:
* Wrap label texts using `<br/>` every 2-3 words.
* Do not let text stretch past 20-25 characters.
* Semantic Colors:
  * Failure / Trap / Error: `#e74c3c`
  * Success / Solution / Good Path: `#27ae60`
  * Process / Standard Concept: `#2980b9`

---

## 3. Khmer Unicode Sequence & Spacing Rules

* **Unicode Input Order**:
  1. Consonant
  2. Subscript (`្` + Subscript Consonant)
  3. Dependent Vowel
  4. Diacritic
* **ZWSP (`\u200B`)**: Insert between word boundaries inside a single clause.
* **Regular Spaces**: Use spaces only between clauses/sentences or list items.

---

## 4. Verification Protocol

After creating or modifying content:
1. Run `python3 scripts/audit_lessons.py` to validate Unicode, formatting, and link integrity.
2. Fix all reported errors before committing.

---

## 5. Agent Self-Reflection & Metacognitive Protocol

When executing tasks under this skill, the agent must perform a self-audit:
* **Pedagogical Alignment**: Inspect lesson H1 structure, Socratic inquiry questions, cognitive load parameters (limits: 3 grammar rules, 10 terms), and active recall exercise adequacy.
* **Linguistic Symmetry**: Inspect the matched Khmer-English blocks to ensure they map clean vocabulary and sentence flow.
* **Mermaid & Formatting Integrity**: Verify Mermaid configuration init headers are injected and node line wrapping (<25 chars) is followed.
* **Code verification**: Run the audit tool `scripts/audit_lessons.py` and fix any errors synchronously.
