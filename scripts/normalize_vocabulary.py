#!/usr/bin/env python3
import os
import re

def normalize_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    filename = os.path.basename(filepath)
    changed = False
    
    # 1. Update Title and remove blockquote for chapters 06-10
    title_mapping = {
        "06-ai-machine-learning.md": "# AI & Machine Learning Vocabulary (វាក្យសព្ទ AI និង Machine Learning)",
        "07-cloud-cybersecurity.md": "# Cloud & Cybersecurity Vocabulary (វាក្យសព្ទ Cloud & Cybersecurity)",
        "08-software-testing.md": "# Software Testing & QA Vocabulary (វាក្យសព្ទ Software Testing & QA)",
        "09-system-design.md": "# System Design & Architecture Vocabulary (វាក្យសព្ទ System Design & Architecture)",
        "10-networking-infrastructure.md": "# Networking & Infrastructure Vocabulary (វាក្យសព្ទ Networking & Infrastructure)",
    }
    
    if filename in title_mapping:
        lines = content.splitlines()
        if lines and lines[0].startswith("# "):
            lines[0] = title_mapping[filename]
            changed = True
            
        if len(lines) > 1 and (lines[1].strip().startswith("> **ជំពូក") or lines[1].strip().startswith("> **វាក្យសព្ទ")):
            lines.pop(1)
            changed = True
        elif len(lines) > 2 and (lines[2].strip().startswith("> **ជំពូក") or lines[2].strip().startswith("> **វាក្យសព្ទ")):
            lines.pop(2)
            changed = True
            
        content = "\n".join(lines)
        
    # 2. Add Practice & Reflection section if missing (using strict Markdown heading search)
    has_practice = re.search(
        r"^###\s+.*(?:Practice\s+&\s+Reflection|ការអនុវត្ត\s+និង\s+ការឆ្លុះបញ្ចាំង)", 
        content, 
        re.MULTILINE | re.IGNORECASE
    )
    if not has_practice:
        practice_section = """

---

### 🧠 ការអនុវត្ត និងការឆ្លុះបញ្ចាំង (Practice & Reflection)

1. **Active Retrieval (ការរំលឹកឡើងវិញ)**: Select 5 key terms from the list above that you commonly encounter in your work. Write down their meanings in your own words.
2. **Contextual Writing (ការសរសេរតាមបរិបទ)**: Write a brief paragraph (3-5 sentences) in English describing your current software development project, integrating at least 3 vocabulary words from this chapter.
3. **Reflective Discussion (ការឆ្លុះបញ្ចាំង)**: Why is using precise, standardized technical English terminology important when communicating with cross-border team members or writing documentation? How does it affect cognitive clarity in a distributed team?"""
        
        # Insert practice section before the backlink if backlink exists, otherwise at the end
        if "🔗" in content or "ត្រឡប់ទៅមេរៀនមុន" in content:
            parts = re.split(r"(🔗.*ត្រឡប់ទៅ|🔗.*Back to)", content, flags=re.IGNORECASE)
            if len(parts) >= 3:
                backlink_part = parts[-2] + parts[-1]
                main_part = "".join(parts[:-2]).rstrip()
                content = main_part + practice_section + "\n\n" + backlink_part
                changed = True
        else:
            content = content.rstrip() + practice_section + "\n"
            changed = True
            
    # 3. Add Backlink if missing
    if "ត្រឡប់ទៅមេរៀន" not in content and "Back to Module" not in content and "Back to English" not in content:
        backlink = "\n\n---\n🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**\n"
        content = content.rstrip() + backlink
        changed = True
        
    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Normalized: {filename}")
    else:
        print(f"Skipped (already normalized): {filename}")


def main():
    vocab_dir = "/Users/chamrong/Documents/Projects/github/ichamrong/iblogger-english/04-reading-vocabulary/04-common-it-vocabulary"
    
    files = [
        "01-backend-programming.md",
        "02-frontend-uiux.md",
        "03-database-data.md",
        "04-devops-git.md",
        "05-agile-workplace.md",
        "06-ai-machine-learning.md",
        "07-cloud-cybersecurity.md",
        "08-software-testing.md",
        "09-system-design.md",
        "10-networking-infrastructure.md",
    ]
    
    for filename in files:
        filepath = os.path.join(vocab_dir, filename)
        if os.path.exists(filepath):
            normalize_file(filepath)
        else:
            print(f"File not found: {filename}")


if __name__ == "__main__":
    main()
