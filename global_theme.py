import os
import re

# 1. Create theme.js
theme_js = """
// Immediately apply the saved theme to avoid flashing
const savedTheme = localStorage.getItem('travelGuideTheme');
if (savedTheme) {
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
}

document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const darkModeIcon = document.getElementById('darkModeIcon');
    const htmlElement = document.documentElement;

    // Set correct icon on load
    if (darkModeIcon) {
        if (htmlElement.getAttribute('data-bs-theme') === 'dark') {
            darkModeIcon.classList.remove('bi-moon-fill');
            darkModeIcon.classList.add('bi-sun-fill');
            if(darkModeToggle) darkModeToggle.title = 'Light Mode';
        } else {
            darkModeIcon.classList.remove('bi-sun-fill');
            darkModeIcon.classList.add('bi-moon-fill');
            if(darkModeToggle) darkModeToggle.title = 'Dark Mode';
        }
    }

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            if (htmlElement.getAttribute('data-bs-theme') === 'dark') {
                htmlElement.setAttribute('data-bs-theme', 'light');
                localStorage.setItem('travelGuideTheme', 'light');
                if (darkModeIcon) {
                    darkModeIcon.classList.remove('bi-sun-fill');
                    darkModeIcon.classList.add('bi-moon-fill');
                }
                darkModeToggle.title = 'Dark Mode';
            } else {
                htmlElement.setAttribute('data-bs-theme', 'dark');
                localStorage.setItem('travelGuideTheme', 'dark');
                if (darkModeIcon) {
                    darkModeIcon.classList.remove('bi-moon-fill');
                    darkModeIcon.classList.add('bi-sun-fill');
                }
                darkModeToggle.title = 'Light Mode';
            }
        });
    }
});
"""

with open("theme.js", "w", encoding="utf-8") as f:
    f.write(theme_js)

# 2. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Add theme.js to head
if '<script src="theme.js"></script>' not in index_html:
    index_html = index_html.replace('</head>', '    <script src="theme.js"></script>\n</head>')

# Remove old inline script
old_script = re.compile(r"<script>\s*document\.addEventListener\('DOMContentLoaded', \(\) => \{\s*const darkModeToggle.*?\}\);\s*\}\);\s*</script>", re.DOTALL)
index_html = old_script.sub('', index_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)


# 3. Update all hotel pages
hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(hotels_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Remove hardcoded dark theme
            content = content.replace('data-bs-theme="dark"', '')

            # Add theme.js
            if '<script src="../theme.js"></script>' not in content:
                content = content.replace('</head>', '    <script src="../theme.js"></script>\n</head>')
            
            # Add the dark mode toggle button to the hotel navbar
            nav_button = """<button class="btn btn-link nav-link px-2 dark-mode-btn me-3" id="darkModeToggle" aria-label="Toggle Dark Mode" title="Dark Mode" style="color: inherit;">
                <i class="bi bi-moon-fill" id="darkModeIcon"></i>
            </button>"""
            
            # Look for the Back to Home button and insert dark mode toggle before it
            if 'id="darkModeToggle"' not in content:
                content = content.replace('<a href="../index.html" class="btn btn-outline-primary', nav_button + '\n            <a href="../index.html" class="btn btn-outline-primary')

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Global Dark Mode implemented!")
