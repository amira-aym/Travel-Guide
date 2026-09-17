import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the compass with a clean airplane
html = html.replace('bi-compass', 'bi-airplane-fill')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Logo changed to airplane-fill")
