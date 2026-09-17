import re
import os

# 1. Update index.html Navbar Search and Spacing
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the old search icon li
search_li_pattern = r'<li class="nav-item">\s*<a class="nav-link px-lg-2 text-body search-btn" data-bs-toggle="collapse" href="#searchCollapse".*?</li>'
html = re.sub(search_li_pattern, '', html, flags=re.DOTALL)

# Replace the search collapse and right links
old_right_side = r'<!-- Search Input Collapse -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</nav>'
new_right_side = """<!-- Always Visible Search Form -->
                    <form class="d-flex mx-lg-3 position-relative my-3 my-lg-0" id="searchForm" style="min-width: 250px;">
                        <input type="text" class="form-control rounded-pill pe-5 shadow-sm" id="searchInput" placeholder="Search (e.g. Egypt)..." autocomplete="off">
                        <button type="button" class="btn position-absolute end-0 top-0 bottom-0 rounded-pill px-3 text-primary" id="searchBtn">
                            <i class="bi bi-search"></i>
                        </button>
                        <ul class="list-group position-absolute w-100 mt-1 d-none shadow-sm" id="searchSuggestions" style="max-height: 200px; overflow-y: auto; z-index: 1050; top: 100%;"></ul>
                    </form>

                    <!-- Right Links with Spacing -->
                    <div class="d-flex align-items-center right-links gap-4 mt-3 mt-lg-0 border-top border-lg-0 pt-3 pt-lg-0 ms-lg-3">
                        <!-- Dark Mode Toggle -->
                        <button class="btn btn-link nav-link px-2 dark-mode-btn" id="darkModeToggle" aria-label="Toggle Dark Mode" title="Dark Mode" style="color: inherit;">
                            <i class="bi bi-moon-fill" id="darkModeIcon"></i>
                        </button>
                        <a href="signin.html" class="nav-link auth-link fw-semibold">SIGN IN</a>
                        <a href="signup.html" class="btn btn-primary btn-sm fw-semibold shadow-sm rounded-pill px-4">SIGN UP</a>
                    </div>
                </div>
            </div>

        </div>
    </nav>"""

html = re.sub(old_right_side, new_right_side, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html Navbar")

# 2. Update Destinations/*.html and hotels/*.html to include dark mode script and full navbar
# We will copy the new full navbar from index.html (but adjust paths) and inject it into all subpages.
# Also inject theme.js and style.css

nav_match = re.search(r'<nav id="mainNavbar".*?</nav>', html, re.DOTALL)
full_nav = nav_match.group(0)

# Modify paths for subdirectories
full_nav = full_nav.replace('href="#destinations"', 'href="../index.html#destinations"')
full_nav = full_nav.replace('href="#things-to-do"', 'href="../index.html#things-to-do"')
full_nav = full_nav.replace('href="#restaurants"', 'href="../index.html#restaurants"')
full_nav = full_nav.replace('href="#travel-tips"', 'href="../index.html#travel-tips"')
full_nav = full_nav.replace('href="#"', 'href="../index.html"')
full_nav = full_nav.replace('href="signin.html"', 'href="../signin.html"')
full_nav = full_nav.replace('href="signup.html"', 'href="../signup.html"')

def update_subpages(directory):
    if not os.path.exists(directory):
        return
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Inject new navbar
            content = re.sub(r'<nav.*?</nav>', full_nav, content, flags=re.DOTALL)
            
            # Remove the search form from subpages so it doesn't break JS (search is for home only)
            search_form = re.search(r'<!-- Always Visible Search Form -->.*?</form>', content, re.DOTALL)
            if search_form:
                content = content.replace(search_form.group(0), '')
                
            # Add style.css if missing
            if 'style.css' not in content:
                content = content.replace('</head>', '    <link rel="stylesheet" href="../style.css">\n</head>')
                
            # Add theme.js if missing
            if 'theme.js' not in content:
                content = content.replace('</body>', '    <script src="../theme.js"></script>\n</body>')
            
            # Remove any hardcoded dark mode
            content = content.replace('data-bs-theme="dark"', '')

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

update_subpages("hotels")
update_subpages("Destinations")

print("Updated subpages successfully!")
