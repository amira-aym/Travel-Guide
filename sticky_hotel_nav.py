import os
import re

hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(hotels_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find the nav tag and add position-sticky top-0 z-3
            old_nav = '<nav class="navbar navbar-expand-lg border-bottom py-3 bg-body">'
            new_nav = '<nav class="navbar navbar-expand-lg border-bottom py-3 bg-body position-sticky top-0 z-3 shadow-sm">'
            
            content = content.replace(old_nav, new_nav)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Navbar made sticky in all hotel pages")
