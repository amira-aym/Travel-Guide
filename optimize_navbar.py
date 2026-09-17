import os
import re

def optimize_navbar(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Expand the container to touch the edges more on laptops
    html = html.replace('class="container-fluid px-4"', 'class="container-fluid px-1 px-xl-4"')
    
    # 2. Reduce the size of the search bar
    html = html.replace('style="min-width: 250px;"', 'style="width: 200px;"')
    
    # 3. Reduce gap and margin on the right links to save space
    html = html.replace('gap-4 mt-3 mt-lg-0 border-top border-lg-0 pt-3 pt-lg-0 ms-lg-3', 'gap-2 mt-3 mt-lg-0 border-top border-lg-0 pt-3 pt-lg-0')
    
    # 4. Make center links have smaller horizontal padding
    html = html.replace('px-lg-3', 'px-lg-2')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

optimize_navbar("index.html")

hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            optimize_navbar(os.path.join(hotels_dir, filename))

dest_dir = "Destinations"
if os.path.exists(dest_dir):
    for filename in os.listdir(dest_dir):
        if filename.endswith(".html"):
            optimize_navbar(os.path.join(dest_dir, filename))

print("Navbar optimized to prevent wrapping")
