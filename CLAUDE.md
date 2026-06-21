# CLAUDE.md - Development & Content Standards

This guide describes development commands, structure, and formatting guidelines for the **iblogger-english** repository.

---

## 🛠️ Build & Audit Commands

Since this is a static markdown-based curriculum repository, the main operations are validating files and checking links:

* **Validate Content Rules & Unicode**: `python3 scripts/audit_lessons.py`
* **Validate Single File**: `python3 scripts/audit_lessons.py --file <path-to-file>`
* **Run Local Preview Server (optional)**: `python3 -m http.server 8000`

---

## 📚 Content & Teaching Philosophy (Cycology & Philosophy)

All lessons, guides, and exercises must adhere to specific cognitive and philosophical standards to optimize developer learning:

### 1. Psychological Cognitive Cycles ("Cycology")
* **Active Retrieval & Spacing**: Do not let lessons be purely passive reading. Every lesson must end with a `### 🧠 ការអនុវត្ត និងការឆ្លុះបញ្ចាំង (Practice & Reflection)` section containing active recall exercises. Interleave 1-2 terms from previous chapters into current exercises to trigger spaced repetition memory loops.
* **Cognitive Scaffolding**: Limit each page to at most **3 grammar points** or **10 technical terms** to prevent working memory overload.
* **Empathy & Psychological Safety (Compilation Analogy)**: Frame verbal and grammatical mistakes as syntax/runtime bugs in a compiler. Explain *why* they happen logically (e.g., L1 transfer bias) to lower speaking anxiety and build developer confidence.

### 2. Philosophical Integration
* **Socratic Inquiry**: Introduce lessons with a leading, open-ended question prompting developers to reflect on the conceptual need for a standard or format before explaining it.
* **Pragmatism & Stoic Resilience**: Focus 100% of material on developer-specific utility (git, standups, code comments). In templates (incident reports, reviews), model objective, factual, and calm expressions (reflecting Stoic emotional control during incidents/outages).
* **Hermeneutic Symmetry**: Ensure every Khmer paragraph is matched with its English translation block. This symmetry allows learners to understand specific vocabulary (the parts) in relation to the overall meaning (the whole).
* **Epistemic Scaffolding**: Structure lessons to build from core linguistic axioms (Module 1/2) to technical application (Module 6) and spontaneous professional expression (Module 7).


---

## 📝 Document Formatting Standards

### 1. File Structure
Every lesson folder must contain a `README.md` file structured as follows:
1. `# Title (Khmer Translation in Parentheses)`
2. Core concept explanation (Khmer + English side-by-side or block-by-block).
3. `##` Content Sections (with numbered bullet points or tables).
4. `### 🧠 ការអនុវត្ត និងការឆ្លុះបញ្ចាំង (Practice & Reflection)` (Active recall exercises).
5. Backlink to the parent index at the very bottom: `🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**`.

### 2. Mermaid Diagrams
* **Initial Configuration Block**: Always start Mermaid blocks with the following dark mode styling configuration:
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
* **Text wrapping**: Wrap node labels using `<br/>` every 2-3 words. Do not let text stretch past 20-25 characters.
* **Semantic Colors**: Use `#e74c3c` (Red) for failures/traps, `#27ae60` (Green) for successes/solutions, and `#2980b9` (Blue) for standard pathways.

### 3. Khmer Unicode & Spacing
* **Unicode Sequence Order**: Consonant ➔ Subscript (`្` + Subscript Consonant) ➔ Dependent Vowel ➔ Diacritic.
* **ZWSP (`\u200B`)**: Insert a Zero-Width Space between word boundaries within a clause to prevent rendering overflows.
* **Regular Spaces**: Use spaces only to separate clauses, list numbers, or list items.

---

## 🧠 Agent Self-Reflection & Metacognitive Protocol
When modifying or drafting educational materials in this project, Claude must verify its own work:
1. **Bilingual Match Check**: Do the English explanations match the Khmer translations block-by-block? Are terms translated accurately in developer contexts?
2. **Cognitive Load Check**: Are we staying under the 3 grammar rules or 10 technical terms limit per page?
3. **Retrieval Practice Check**: Does the end of the lesson contain actual recall prompts or interactive tasks?
4. **Link & Anchor Check**: Are the anchors referenced in the TOC matching HTML `<a id="...">` elements? Are the parent backlinks pointing correctly to standard paths?
5. **Execution Verification**: Always execute `python3 scripts/audit_lessons.py` and fix any formatting or Unicode errors.
