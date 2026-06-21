#!/usr/bin/env python3
import os
import re
import sys
import argparse

# Terminal colors for output formatting
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Unicode character classes for Khmer script
KHMER_CONSONANTS = r"[\u1780-\u17A2]"
KHMER_VOWELS = r"[\u17B6-\u17C5]"

# Standard diacritics that must always follow dependent vowels.
# Excludes register shifters \u17C9 (៉) and \u17CA (៊).
KHMER_DIACRITICS = r"[\u17C6\u17C7\u17C8\u17CB\u17CC\u17CD\u17CE\u17CF\u17D0\u17D1\u17D3]"  # ំ, ះ, ៈ, ់, ៌, ៍, ៎, ៏, ័, ៑, ៈ
KHMER_SUBSCRIPT_SIGN = r"\u17D2"  # ្

# Regex for common Khmer Unicode ordering mistakes
ERR_VOWEL_BEFORE_SUBSCRIPT = re.compile(r"[\u17B6-\u17C5]\u17D2")
ERR_DIACRITIC_BEFORE_VOWEL = re.compile(f"{KHMER_DIACRITICS}{KHMER_VOWELS}")


def get_clean_content(content):
    """Returns content with all code blocks (fenced and inline) removed.
    This prevents false positives on examples, templates, or instructions."""
    # Strip fenced code blocks (``` ... ```)
    clean = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    # Strip inline code (`...`)
    clean = re.sub(r"`[^`\n]+`", "", clean)
    return clean


def check_khmer_unicode(content, filepath):
    """Checks for Khmer Unicode ordering violations in the file content."""
    errors = []
    
    # Check Vowel before Subscript
    for match in ERR_VOWEL_BEFORE_SUBSCRIPT.finditer(content):
        start = match.start()
        context = content[max(0, start - 10) : min(len(content), start + 10)]
        line_num = content.count('\n', 0, start) + 1
        errors.append(
            f"Line {line_num}: Dependent vowel placed before subscript. Context: '...{context.strip()}...'"
        )
        
    # Check Diacritic before Vowel
    for match in ERR_DIACRITIC_BEFORE_VOWEL.finditer(content):
        start = match.start()
        context = content[max(0, start - 10) : min(len(content), start + 10)]
        line_num = content.count('\n', 0, start) + 1
        errors.append(
            f"Line {line_num}: Diacritic placed before dependent vowel. Context: '...{context.strip()}...'"
        )
        
    return errors


def check_mermaid_diagrams(content, filepath):
    """Validates Mermaid diagram initialization and text-wrapping requirements."""
    errors = []
    
    # Find all mermaid blocks
    mermaid_blocks = re.findall(r"```mermaid\s+(.*?)\s+```", content, re.DOTALL)
    
    for i, block in enumerate(mermaid_blocks):
        # Calculate line offset
        parts = content.split("```mermaid")
        block_line_offset = sum(part.count("\n") for part in parts[:i+1]) + 1
        
        # 1. Check for dark mode theme/init variables
        if "%%{init:" not in block or "'theme': 'dark'" not in block or "'themeCSS':" not in block:
            errors.append(
                f"Mermaid block #{i+1} starting around line {block_line_offset} is missing the required contrast-safe dark theme initialization header."
            )
            
        # 2. Check for node text wrapping
        labels = re.findall(r'\["(.*?)"\]|\("(.*?)"\)|\{\{"(.*?)"\}\}|"(.*?)"', block)
        flat_labels = [lbl for group in labels for lbl in group if lbl]
        
        for label in flat_labels:
            clean_label = label.replace("<br/>", "\n").replace("<br >", "\n").replace("<br>", "\n")
            lines = clean_label.split("\n")
            for line in lines:
                if len(line) > 25:
                    errors.append(
                        f"Mermaid block #{i+1} contains a label line longer than 25 characters: '{line}'. Please wrap using '<br/>' every 2-3 words."
                    )
                    
    return errors


def check_toc_and_anchors(clean_content, content, filepath):
    """Checks if Table of Contents anchor links point to valid HTML anchors."""
    errors = []
    
    # Get all HTML anchors in the file (e.g., <a id="0"></a> or <a id="anchor"></a>)
    anchors = set(re.findall(r'<a\s+(?:name|id)=["\'](.*?)["\']\s*>\s*</a>', clean_content, re.IGNORECASE))
    
    # Get all markdown links starting with #
    toc_links = re.findall(r'\[.*?\]\(#(.*?)\)', clean_content)
    
    for link in toc_links:
        if link not in anchors:
            errors.append(
                f"TOC link references anchor #{link}, but no matching anchor '<a id=\"{link}\"></a>' was found in the file."
            )
            
    return errors


def check_relative_links(clean_content, filepath, root_dir):
    """Verifies that all relative markdown links point to existing files."""
    errors = []
    file_dir = os.path.dirname(filepath)
    
    # Find links, e.g. [text](path) or [text](path#anchor)
    links = re.findall(r'\[.*?\]\((?!http|https|mailto|ftp|#)(.*?)\)', clean_content)
    
    for link in links:
        link_path = link.split('#')[0]
        if not link_path:
            continue
            
        from urllib.parse import unquote
        link_path = unquote(link_path)
        
        target_path = os.path.normpath(os.path.join(file_dir, link_path))
        
        if not os.path.exists(target_path):
            errors.append(
                f"Broken link: '{link}' points to non-existent path '{target_path}'"
            )
            
    return errors


def check_pedagogical_structure(clean_content, filepath, root_dir):
    """Validates that lesson files follow standard pedagogical structure."""
    filename = os.path.basename(filepath)
    
    # 1. Skip all index files, root configs, or routine schedules (any README.md, CLAUDE.md, etc.)
    if filename.lower() == "readme.md" or filename.upper() == "CLAUDE.MD" or filename.upper() == "AGENTS.MD" or "routine.md" in filename.lower():
        return []
        
    # 2. Only enforce on files inside module directories (01-07)
    rel_path = os.path.relpath(filepath, root_dir)
    path_parts = rel_path.split(os.sep)
    is_lesson_file = any(re.match(r"^0\d-", part) for part in path_parts)
    
    if not is_lesson_file:
        return []
        
    errors = []
    
    # 3. Check for Socratic title or bilingual format
    title_match = re.search(r"^#\s+(.+)$", clean_content, re.MULTILINE)
    if not title_match:
        errors.append("File is missing a main H1 title ('# Title').")
    else:
        title = title_match.group(1).strip()
        if "(" not in title or ")" not in title:
            errors.append(
                f"H1 title '{title}' should follow the bilingual format: 'English Title (Khmer Title)'."
            )
            
    # 4. Check for Practice & Reflection section using Markdown heading syntax
    has_practice = re.search(
        r"^###\s+.*(?:Practice\s+&\s+Reflection|ការអនុវត្ត\s+និង\s+ការឆ្លុះបញ្ចាំង)", 
        clean_content, 
        re.MULTILINE | re.IGNORECASE
    )
    if not has_practice:
        errors.append(
            "Missing the required '### 🧠 ការអនុវត្ត និងការឆ្លុះបញ្ចាំង (Practice & Reflection)' section for active retrieval practice."
        )
        
    # 5. Check for Backlink at the bottom
    has_backlink = (
        ("ត្រឡប់ទៅមេរៀន" in clean_content or "Back to Module" in clean_content or "Back to English" in clean_content)
        and "README.md" in clean_content
    )
    if not has_backlink:
        errors.append(
            "Missing navigation backlink at the end of the file pointing to parent README.md."
        )
        
    return errors


def audit_file(filepath, root_dir):
    """Audits a single markdown file against all rules."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"Failed to read file: {e}"]
        
    # Create code-free version for structural and link analyses
    clean_content = get_clean_content(content)
    
    errors = []
    
    # Run audit checks
    errors.extend(check_khmer_unicode(content, filepath))
    errors.extend(check_mermaid_diagrams(content, filepath))
    errors.extend(check_toc_and_anchors(clean_content, content, filepath))
    errors.extend(check_relative_links(clean_content, filepath, root_dir))
    errors.extend(check_pedagogical_structure(clean_content, filepath, root_dir))
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Audit markdown files for iblogger-english repository standards."
    )
    parser.add_argument(
        "--file", 
        type=str, 
        help="Specify a single file to audit. If omitted, all markdown files are audited recursively."
    )
    args = parser.parse_args()
    
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files_to_audit = []
    
    if args.file:
        full_path = os.path.abspath(args.file)
        if not os.path.exists(full_path):
            print(f"{RED}{BOLD}Error:{RESET} File not found: {args.file}")
            sys.exit(1)
        files_to_audit.append(full_path)
    else:
        # Recursively find all markdown files
        for root, dirs, files in os.walk(root_dir):
            # Skip hidden directories and node_modules
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
            for file in files:
                if file.endswith(".md"):
                    files_to_audit.append(os.path.join(root, file))
                    
    total_files = len(files_to_audit)
    failed_files = 0
    total_errors = 0
    
    print(f"{BLUE}{BOLD}Starting Audit on {total_files} file(s)...{RESET}\n")
    
    for filepath in sorted(files_to_audit):
        rel_path = os.path.relpath(filepath, root_dir)
        errors = audit_file(filepath, root_dir)
        
        if errors:
            failed_files += 1
            total_errors += len(errors)
            print(f"{RED}{BOLD}✗ {rel_path}{RESET} ({len(errors)} error(s) found)")
            for err in errors:
                print(f"  {RED}-{RESET} {err}")
            print()
        else:
            print(f"{GREEN}✓ {rel_path}{RESET}")
            
    print("-" * 50)
    if total_errors > 0:
        print(
            f"{RED}{BOLD}Audit Failed!{RESET} {failed_files}/{total_files} files failed with a total of {total_errors} errors."
        )
        sys.exit(1)
    else:
        print(f"{GREEN}{BOLD}Audit Passed!{RESET} All {total_files} files comply with standard formatting and Unicode guidelines.")
        sys.exit(0)


if __name__ == "__main__":
    main()
