import os

def remove_dismiss(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace(' data-bs-dismiss="offcanvas"', '')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

remove_dismiss("index.html")

for d in ["hotels", "Destinations"]:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                remove_dismiss(os.path.join(d, filename))

print("Removed data-bs-dismiss from HTML")
