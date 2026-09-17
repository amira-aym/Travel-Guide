import os
import re

auth_html = """
                        <!-- Guest Links -->
                        <div id="guestLinks" class="d-flex align-items-center gap-2">
                            <a href="signin.html" class="nav-link auth-link fw-semibold">SIGN IN</a>
                            <a href="signup.html" class="btn btn-primary btn-sm fw-semibold shadow-sm rounded-pill px-4">SIGN UP</a>
                        </div>
                        
                        <!-- User Links (Hidden by default) -->
                        <div id="userLinks" class="d-flex align-items-center d-none ms-2">
                            <div class="dropdown">
                                <a class="nav-link dropdown-toggle d-flex align-items-center fw-semibold text-body p-0" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    <img src="https://ui-avatars.com/api/?name=Amira&background=2563eb&color=fff" alt="User" class="rounded-circle me-2 border border-2 border-primary user-avatar" width="36" height="36">
                                    <span class="d-none d-lg-block user-name">My Account</span>
                                </a>
                                <ul class="dropdown-menu dropdown-menu-end shadow-sm border-0 mt-3" style="min-width: 200px;">
                                    <li><h6 class="dropdown-header">Welcome, <span class="user-first-name">Amira</span>!</h6></li>
                                    <li><a class="dropdown-item py-2" href="settings.html"><i class="bi bi-person me-2 text-primary"></i> Profile</a></li>
                                    <li><a class="dropdown-item py-2" href="settings.html"><i class="bi bi-gear me-2 text-secondary"></i> Settings</a></li>
                                    <li><a class="dropdown-item py-2" href="bookings.html"><i class="bi bi-bag-check me-2 text-success"></i> My Bookings</a></li>
                                    <li><hr class="dropdown-divider"></li>
                                    <li><a class="dropdown-item py-2 text-danger fw-bold" href="#" id="signOutBtn"><i class="bi bi-box-arrow-right me-2"></i> Sign Out</a></li>
                                </ul>
                            </div>
                        </div>
"""

def apply_auth_html(filepath, is_root=True):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    old_auth = r'<!-- Guest Links -->.*?</div>\s*<!-- User Links.*?</div>\s*</div>'
    
    replacement = auth_html
    if not is_root:
        replacement = replacement.replace('href="signin.html"', 'href="../signin.html"')
        replacement = replacement.replace('href="signup.html"', 'href="../signup.html"')
        replacement = replacement.replace('href="settings.html"', 'href="../settings.html"')
        replacement = replacement.replace('href="bookings.html"', 'href="../bookings.html"')
        
    html = re.sub(old_auth, replacement, html, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

apply_auth_html("index.html")

for d in ["hotels", "Destinations"]:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                apply_auth_html(os.path.join(d, filename), False)

# Now inject the full navbar into bookings.html and settings.html
with open("index.html", "r", encoding="utf-8") as f:
    idx = f.read()
nav_match = re.search(r'<nav id="mainNavbar".*?</nav>', idx, re.DOTALL)
full_nav = nav_match.group(0)

for new_page in ["bookings.html", "settings.html"]:
    with open(new_page, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace('<div id="navbar-placeholder"></div>', full_nav)
    # Remove search form since it's not home page
    search_form = re.search(r'<!-- Always Visible Search Form -->.*?</form>', content, re.DOTALL)
    if search_form:
        content = content.replace(search_form.group(0), '')
    with open(new_page, "w", encoding="utf-8") as f:
        f.write(content)

print("Auth UI updated with correct links")
