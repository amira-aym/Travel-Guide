import os

bootstrap_js = '    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>\n'

def add_bootstrap_js(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if 'bootstrap.bundle.min.js' not in content:
        content = content.replace('</body>', bootstrap_js + '</body>')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

for d in ["hotels", "Destinations"]:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                add_bootstrap_js(os.path.join(d, filename))

print("Bootstrap JS added to all subpages")
