import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Force cache bust for search.js
content = content.replace('<script src="search.js"></script>', '<script src="search.js?v=2"></script>')

# Remove text-muted and text-decoration-none from footer links to allow custom hover
content = content.replace('class="text-decoration-none text-muted"', '')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add html { overflow-x: hidden; }
if 'html {\n    overflow-x: hidden;' not in css:
    css = css.replace('html {', 'html {\n    overflow-x: hidden;')

# Add footer links hover styles
footer_css = """
/* Footer Links */
.footer-column ul a {
    text-decoration: none !important;
    color: inherit;
    transition: color 0.3s ease;
}
.footer-column ul a:hover {
    color: #0d6efd !important;
}
[data-bs-theme="dark"] .footer-column ul a {
    color: #adb5bd;
}
[data-bs-theme="dark"] .footer-column ul a:hover {
    color: #0d6efd !important;
}
"""
css += footer_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updates applied")
