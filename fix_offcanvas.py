import os
import re

# 1. Update CSS to limit offcanvas width
css_fix = """
/* Make Offcanvas burger menu only take 75% of screen width on mobile */
@media (max-width: 600px) {
    .offcanvas {
        max-width: 75vw !important;
    }
}
"""
with open("style.css", "a", encoding="utf-8") as f:
    f.write(css_fix)

# 2. Add data-bs-dismiss="offcanvas" to the nav links in all pages
def add_dismiss_to_links(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the offcanvas-body
    body_match = re.search(r'<div class="offcanvas-body">.*?(?=</div>\s*</div>\s*</div>\s*</nav>)', html, re.DOTALL)
    if not body_match:
        return

    offcanvas_body = body_match.group(0)
    
    # We want to add data-bs-dismiss to all <a class="nav-link..."> inside it
    # except the search button or dark mode toggle if we don't want them to close it, 
    # but actually closing on any click is fine!
    
    # Let's specifically target the section links
    updated_body = re.sub(r'(<a class="nav-link custom-hover[^>]*href="[^"]*#(?:destinations|things-to-do|restaurants|travel-tips)"[^>]*)>', r'\1 data-bs-dismiss="offcanvas">', offcanvas_body)
    
    html = html.replace(offcanvas_body, updated_body)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)


add_dismiss_to_links("index.html")

for d in ["hotels", "Destinations"]:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                add_dismiss_to_links(os.path.join(d, filename))

print("Offcanvas width and auto-close fixed")
