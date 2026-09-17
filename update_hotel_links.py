import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# We will regex replace the h2 in each hotel card to include the stretched-link
replacements = {
    "Paris, France": "hotels/paris.html",
    "Kyoto, Japan": "hotels/kyoto.html",
    "Santorini, Greece": "hotels/santorini.html",
    "Cairo, Egypt": "hotels/cairo.html",
    "Rome, Italy": "hotels/rome.html",
    "New York, USA": "hotels/newyork.html"
}

for title, link in replacements.items():
    old = f'<h2 class="card-title">{title}</h2>'
    new = f'<h2 class="card-title"><a href="{link}" class="stretched-link text-body text-decoration-none">{title}</a></h2>'
    html = html.replace(old, new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated with stretched links for hotels")
