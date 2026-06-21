import { describe, it, expect } from "vitest";
import { parseRoadmap, resolveRelativeLink, getMarkdownPath } from "../app.js";

describe("Markdown Web App Logic", () => {
  
  describe("parseRoadmap", () => {
    it("should parse hierarchical modules and their lessons from markdown", () => {
      const sampleMarkdown = `
# Learning Path Roadmap

### 📂 [Module 1: Grammar Foundations (គ្រឹះនៃវេយ្យាករណ៍)](01-grammar-foundations/README.md)
*សិក្សាពីគ្រឹះដ៏សំខាន់នៃភាសាអង់គ្លេស។*
*Learn the essential building blocks of English grammar.*

  - [01. Parts of Speech (ថ្នាក់នៃពាក្យ)](01-grammar-foundations/01-parts-of-speech/README.md)
  - [02. Sentence Structure (ទម្រង់ប្រយោគ)](01-grammar-foundations/02-sentence-structure/README.md)

### 📂 [Module 2: Pronunciation (ការបញ្ចេញសំឡេង)](02-pronunciation-phonetics/README.md)
*ស្វែងយល់ពីរបៀបបញ្ចេញសំឡេងឱ្យបានត្រឹមត្រូវ។*

  - [01. IPA System (តារាងសូរសព្ទ)](02-pronunciation-phonetics/01-ipa-system/README.md)
`;

      const modules = parseRoadmap(sampleMarkdown);
      
      expect(modules).toHaveLength(2);
      
      // Verify Module 1
      expect(modules[0].title).toBe("Module 1: Grammar Foundations (គ្រឹះនៃវេយ្យាករណ៍)");
      expect(modules[0].path).toBe("01-grammar-foundations/README.md");
      expect(modules[0].description).toContain("គ្រឹះដ៏សំខាន់");
      expect(modules[0].lessons).toHaveLength(2);
      expect(modules[0].lessons[0].title).toBe("01. Parts of Speech (ថ្នាក់នៃពាក្យ)");
      expect(modules[0].lessons[0].path).toBe("01-grammar-foundations/01-parts-of-speech/README.md");
      
      // Verify Module 2
      expect(modules[1].title).toBe("Module 2: Pronunciation (ការបញ្ចេញសំឡេង)");
      expect(modules[1].path).toBe("02-pronunciation-phonetics/README.md");
      expect(modules[1].lessons).toHaveLength(1);
      expect(modules[1].lessons[0].title).toBe("01. IPA System (តារាងសូរសព្ទ)");
    });

    it("should handle empty or malformed roadmaps gracefully", () => {
      const modules = parseRoadmap("");
      expect(modules).toEqual([]);
    });
  });

  describe("resolveRelativeLink", () => {
    it("should resolve relative links based on current file directory", () => {
      const currentPath = "04-reading-vocabulary/04-common-it-vocabulary/02-frontend-uiux.md";
      
      // Link to sibling in same directory
      expect(resolveRelativeLink(currentPath, "01-backend-programming.md"))
        .toBe("04-reading-vocabulary/04-common-it-vocabulary/01-backend-programming.md");
        
      // Link to parent directory
      expect(resolveRelativeLink(currentPath, "../README.md"))
        .toBe("04-reading-vocabulary/README.md");
        
      // Link to grandparent directory
      expect(resolveRelativeLink(currentPath, "../../README.md"))
        .toBe("README.md");
    });

    it("should preserve absolute URLs and anchor-only links", () => {
      const currentPath = "01-grammar-foundations/README.md";
      
      expect(resolveRelativeLink(currentPath, "https://google.com")).toBe("https://google.com");
      expect(resolveRelativeLink(currentPath, "#anchor")).toBe("#anchor");
      expect(resolveRelativeLink(currentPath, "mailto:test@example.com")).toBe("mailto:test@example.com");
    });
  });

  describe("getMarkdownPath", () => {
    it("should return README.md for empty or root hash", () => {
      expect(getMarkdownPath("")).toBe("README.md");
      expect(getMarkdownPath("#")).toBe("README.md");
      expect(getMarkdownPath("#/")).toBe("README.md");
    });

    it("should return the relative path extracted from hash route", () => {
      expect(getMarkdownPath("#/01-grammar-foundations/README.md")).toBe("01-grammar-foundations/README.md");
      expect(getMarkdownPath("#/07-daily-practice-scripts/01-daily-standup/README.md"))
        .toBe("07-daily-practice-scripts/01-daily-standup/README.md");
    });
  });

});
