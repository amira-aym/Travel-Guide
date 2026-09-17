import os

# 1. Fix search.js in index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

if 'search.js' not in index_html:
    index_html = index_html.replace('</body>', '    <script src="search.js"></script>\n</body>')
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

# 2. Fix CSS and scripts in hotels pages
hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(hotels_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Link style.css
            if 'style.css' not in content:
                content = content.replace('</head>', '    <link rel="stylesheet" href="../style.css">\n</head>')
            
            # The search bar is now in the hotels page navbar. But search.js expects #searchResultsSection which doesn't exist.
            # We must either remove the search bar from hotels navbar, or redirect it to index.html
            # Let's just remove the search bar from the hotels navbar to keep it clean and avoid JS errors.
            # Or we can link a modified search.js that redirects. Removing it is safer.
            import re
            search_html = re.search(r'<!-- Search Input Collapse -->.*?</div>', content, re.DOTALL)
            if search_html:
                content = content.replace(search_html.group(0), '')
            search_icon = re.search(r'<li class="nav-item">\s*<a class="nav-link px-lg-2 text-body search-btn".*?</li>', content, re.DOTALL)
            if search_icon:
                content = content.replace(search_icon.group(0), '')

            # And link theme.js if not present
            if 'theme.js' not in content:
                content = content.replace('</body>', '    <script src="../theme.js"></script>\n</body>')

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Search restored and Hotel Dark Mode fixed")
