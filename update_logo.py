import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the old icon with bi-compass
html = html.replace('bi-airplane-engines-fill', 'bi-compass')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Logo changed to compass")
