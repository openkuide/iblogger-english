/**
 * Markdown Web App Engine for iblogger-english
 * Supports Vue 3, Markdown parsing, and Mermaid diagrams.
 */

/**
 * Parses the main README.md roadmap to build the navigation hierarchy.
 * @param {string} markdown
 * @returns {Array} List of modules with lessons
 */
export function parseRoadmap(markdown) {
  if (!markdown) return [];
  const lines = markdown.split("\n");
  const modules = [];
  let currentModule = null;

  for (let line of lines) {
    line = line.trim();
    if (!line) continue;

    // Check for Module header (H3 with link)
    const moduleMatch = line.match(/^###\s+.*\[([^\]]+)\]\(([^)]+)\)/);
    if (moduleMatch) {
      currentModule = {
        title: moduleMatch[1].trim(),
        path: moduleMatch[2].trim(),
        description: "",
        lessons: []
      };
      modules.push(currentModule);
      continue;
    }

    // Check for Lesson list item (bullet list with link)
    const lessonMatch = line.match(/^[-*]\s+\[([^\]]+)\]\(([^)]+)\)/);
    if (lessonMatch) {
      if (currentModule) {
        currentModule.lessons.push({
          title: lessonMatch[1].trim(),
          path: lessonMatch[2].trim()
        });
      }
      continue;
    }

    // Capture italic description text under a module header before any lessons are defined
    if (line.startsWith("*") && line.endsWith("*")) {
      if (currentModule && currentModule.lessons.length === 0) {
        const cleanDesc = line.replace(/^\*+|\*+$/g, "").trim();
        if (currentModule.description) {
          currentModule.description += "\n" + cleanDesc;
        } else {
          currentModule.description = cleanDesc;
        }
      }
    }
  }
  return modules;
}

/**
 * Resolves a relative file link (e.g. "../README.md") against a current file path.
 * @param {string} currentPath - Path of the active markdown file
 * @param {string} relativeLink - Relative link inside the markdown file
 * @returns {string} Fully resolved path relative to project root
 */
export function resolveRelativeLink(currentPath, relativeLink) {
  if (!relativeLink) return "";
  
  // Return absolute URLs or anchors untouched
  if (relativeLink.match(/^(https?:|mailto:|#)/i)) {
    return relativeLink;
  }
  
  const dirParts = currentPath.split("/");
  dirParts.pop(); // Remove current filename to get directory path
  
  const linkParts = relativeLink.split("/");
  for (const part of linkParts) {
    if (part === "" || part === ".") {
      continue;
    } else if (part === "..") {
      dirParts.pop();
    } else {
      dirParts.push(part);
    }
  }
  return dirParts.join("/");
}

/**
 * Extracts the file path from the hash route parameter.
 * @param {string} hash - The window.location.hash string
 * @returns {string} The resolved file path
 */
export function getMarkdownPath(hash) {
  if (!hash || hash === "#" || hash === "#/") return "README.md";
  
  let path = hash;
  if (path.startsWith("#/")) {
    path = path.substring(2);
  } else if (path.startsWith("#")) {
    path = path.substring(1);
  }
  
  // Strip any anchor/hash parts from the target path (e.g., path/to/file.md#anchor)
  return path.split("#")[0] || "README.md";
}

// Mount the Vue App if running in a browser environment
if (typeof window !== "undefined" && window.Vue) {
  const { createApp, ref, computed, onMounted } = window.Vue;

  createApp({
    setup() {
      const sidebarModules = ref([]);
      const currentContent = ref("");
      const currentPath = ref("README.md");
      const isSidebarOpen = ref(true);
      const isLoading = ref(false);
      const isMobileMenuOpen = ref(false);

      // Render markdown using Marked.js and sanitize with DOMPurify
      const renderedHtml = computed(() => {
        if (!currentContent.value) return "";
        const rawHtml = window.marked.parse(currentContent.value);
        return window.DOMPurify ? window.DOMPurify.sanitize(rawHtml) : rawHtml;
      });

      const fetchMarkdown = async (path) => {
        isLoading.value = true;
        try {
          const res = await fetch(path);
          if (!res.ok) throw new Error("File not found");
          let text = await res.text();

          // Transform relative links in markdown to work with hash-based routing
          // matches e.g. [text](relative-link.md) but skips http/https/mailto/#
          text = text.replace(/\[([^\]]+)\]\(((?!http|https|mailto|#)[^)]+)\)/g, (match, textPart, linkPart) => {
            const resolved = resolveRelativeLink(path, linkPart);
            return `[${textPart}](#/${resolved})`;
          });

          currentContent.value = text;
          currentPath.value = path;
          
          // Re-render Mermaid diagrams after DOM updates
          setTimeout(() => {
            if (window.mermaid) {
              window.mermaid.init(undefined, document.querySelectorAll('.mermaid'));
            }
          }, 150);
          
          // Scroll content back to top
          window.scrollTo({ top: 0, behavior: 'smooth' });
        } catch (err) {
          currentContent.value = `# ⚠️ Error\nCould not load page: \`${path}\`. Please verify the path exists.`;
          currentPath.value = path;
        } finally {
          isLoading.value = false;
        }
      };

      const handleRouteChange = () => {
        const path = getMarkdownPath(window.location.hash);
        fetchMarkdown(path);
        isMobileMenuOpen.value = false; // Close menu on route change
      };

      const toggleSidebar = () => {
        isSidebarOpen.value = !isSidebarOpen.value;
      };

      const toggleMobileMenu = () => {
        isMobileMenuOpen.value = !isMobileMenuOpen.value;
      };

      onMounted(async () => {
        // Fetch roadmap index to construct sidebar
        try {
          const res = await fetch("README.md");
          if (res.ok) {
            const readmeText = await res.text();
            sidebarModules.value = parseRoadmap(readmeText);
          }
        } catch (e) {
          console.error("Failed to load navigation menu", e);
        }

        // Initialize and listen to routes
        handleRouteChange();
        window.addEventListener("hashchange", handleRouteChange);
      });

      return {
        sidebarModules,
        currentPath,
        renderedHtml,
        isSidebarOpen,
        isLoading,
        isMobileMenuOpen,
        toggleSidebar,
        toggleMobileMenu
      };
    }
  }).mount("#app");
}
