import os
import re

def fix_subpages(directory):
    if not os.path.exists(directory):
        return
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Remove theme.js
            content = content.replace('<script src="../theme.js"></script>', '')
            
            # Add dark-mode.js to head
            if '<script src="../Jave/dark-mode.js"></script>' not in content:
                content = content.replace('</head>', '    <script src="../Jave/dark-mode.js"></script>\n</head>')
                
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

fix_subpages("hotels")
fix_subpages("Destinations")

with open("index.html", "r", encoding="utf-8") as f:
    idx = f.read()

# Also make sure index.html links dark-mode.js in head, not body, to prevent flash
if '<script src="Jave/dark-mode.js"></script>' in idx:
    # Remove from body
    idx = idx.replace('<script src="Jave/dark-mode.js"></script>', '')

if '<script src="Jave/dark-mode.js"></script>' not in idx:
    idx = idx.replace('</head>', '    <script src="Jave/dark-mode.js"></script>\n</head>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx)

print("Fixed JS links")
