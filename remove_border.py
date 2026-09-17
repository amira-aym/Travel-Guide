import os
import re

def remove_border(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace('border-top border-lg-0 pt-3 pt-lg-0', '')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

remove_border("index.html")

for d in ["hotels", "Destinations"]:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                remove_border(os.path.join(d, filename))

print("Removed border-top from right links")
