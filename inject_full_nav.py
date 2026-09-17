import os
import re

# Get the clean navbar from index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

nav_match = re.search(r'<nav id="mainNavbar".*?</nav>', html, re.DOTALL)
if nav_match:
    full_nav = nav_match.group(0)
else:
    print("Could not find mainNavbar")
    exit()

# Modify the links to work from the 'hotels' subfolder
full_nav = full_nav.replace('href="#destinations"', 'href="../index.html#destinations"')
full_nav = full_nav.replace('href="#things-to-do"', 'href="../index.html#things-to-do"')
full_nav = full_nav.replace('href="#restaurants"', 'href="../index.html#restaurants"')
full_nav = full_nav.replace('href="#travel-tips"', 'href="../index.html#travel-tips"')
full_nav = full_nav.replace('href="#"', 'href="../index.html"')
full_nav = full_nav.replace('href="signin.html"', 'href="../signin.html"')
full_nav = full_nav.replace('href="signup.html"', 'href="../signup.html"')

hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(hotels_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # The hotel pages currently have a mini nav like this:
            # <nav class="navbar navbar-expand-lg border-bottom py-3 bg-body position-sticky top-0 z-3 shadow-sm"> ... </nav>
            content = re.sub(r'<nav class="navbar.*?</nav>', full_nav, content, flags=re.DOTALL)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Full navbar injected into hotel pages")
