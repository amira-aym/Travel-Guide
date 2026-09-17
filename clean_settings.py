with open("settings.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
old_js = r'// Update email input if Google login.*?}'
html = re.sub(old_js, '', html, flags=re.DOTALL)

with open("settings.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Removed hardcoded amira email from settings.html")
