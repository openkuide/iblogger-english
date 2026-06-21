# Antigravity Workspace Rules - iblogger-english

This ruleset governs the behavior of Antigravity agents when working inside this workspace.

## 1. Bilingual Content Integrity
* Maintain matching bilingual structure. Ensure every lesson header, description, and explanation contains both Khmer and English equivalents.
* Align text blocks so they are balanced. Avoid writing massive Khmer explanations with tiny English translations, or vice versa.

## 2. Learning Philosophy Compliance (Cycology & Philosophy)
* **Cognitive Load Control**: Limit each page to at most **3 grammar rules** or **10 technical terms** to prevent working memory overload.
* **Psychological Safety (Compilation Analogy)**: Lower the learner's "affective filter" by framing speech practice as a code compilation loop. Explain that speaking errors are syntax/runtime bugs—healthy, iterative signals, not signs of personal failure. Document L1-transfer errors with logical explanations.
* **Active Retrieval & Spacing (Cycology)**: Every lesson must end with a `### 🧠 ការអនុវត្ត និងការឆ្លុះបញ្ចាំង (Practice & Reflection)` section testing active recall. Interleave vocabulary by re-testing 1-2 terms from previous chapters in current exercises to trigger spaced repetition memory cycles.
* **Socratic Inquiry**: Introduce lessons with a leading, open-ended question that prompts developers to reflect on the conceptual necessity of a syntax standard or verbal format before explaining it.
* **Pragmatism & Stoic Resilience**: Focus 100% of material on developer-specific utility (git, standups, reviews). In communication templates (e.g. asking for help, reporting incidents), model objective, factual, and calm expressions (reflecting Stoic emotional regulation during production fires).
* **Hermeneutic Symmetry**: Ensure every Khmer paragraph is matched with its English translation block or inline translation. This symmetry allows learners to understand specific vocabulary (the parts) in relation to the overall meaning (the whole).
* **Epistemic Scaffolding**: Structure lessons to build from core linguistic axioms (Module 1/2) to technical application (Module 6) and spontaneous professional expression (Module 7).


## 3. Formatting Standards
* **Mermaid Styling**: Include the custom theme initialization block at the start of all Mermaid diagrams. Wrap node labels with `<br/>` every 2-3 words. Use `#e74c3c` (Red) for failures, `#27ae60` (Green) for successes, and `#2980b9` (Blue) for standard flows.
* **Table of Contents**: Create Table of Contents using numbered HTML anchors (`<a id="0"></a>` through `<a id="N"></a>`).
* **Navigation backlinks**: Always include the navigation backlink at the bottom of lesson pages: `🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**`.

## 4. Khmer Unicode & Spacing
* **Unicode Order**: Consonant ➔ Subscript (`្` + Subscript Consonant) ➔ Dependent Vowel ➔ Diacritic.
* **ZWSP (`\u200B`)**: Use Zero-Width Spaces between word boundaries inside a single Khmer clause.
* **Regular Spaces**: Use spaces only between clauses/sentences or list items.

## 5. Automated Verification
* Always run the command `python3 scripts/audit_lessons.py` to check for formatting errors and Unicode issues after modifying any markdown files in the workspace.

## 6. Agent Self-Reflection & Metacognitive Protocol
* **Self-Audit Check**: Before finalizing any modified or newly generated content, the agent must inspect its output against the rules in this document.
* **Hermeneutic Symmetry Review**: Confirm that Khmer text matches English text section-by-section. Check for correct digital IT context translation.
* **Recall Adequacy**: Ensure the practice exercises test active recall (e.g. prompt completion, error correction) rather than passive reading or simple multi-choice.
* **Zero Unicode Error Target**: If the audit script fails due to Unicode sequence errors, the agent must fix the character sequences (Consonant + Subscript + Vowel + Diacritic) before finishing.
