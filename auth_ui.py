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
                                    <img src="https://ui-avatars.com/api/?name=Amira&background=2563eb&color=fff" alt="User" class="rounded-circle me-2 border border-2 border-primary" width="36" height="36">
                                    <span class="d-none d-lg-block">My Account</span>
                                </a>
                                <ul class="dropdown-menu dropdown-menu-end shadow-sm border-0 mt-3" style="min-width: 200px;">
                                    <li><h6 class="dropdown-header">Welcome, Amira!</h6></li>
                                    <li><a class="dropdown-item py-2" href="#"><i class="bi bi-person me-2 text-primary"></i> Profile</a></li>
                                    <li><a class="dropdown-item py-2" href="#"><i class="bi bi-gear me-2 text-secondary"></i> Settings</a></li>
                                    <li><a class="dropdown-item py-2" href="#"><i class="bi bi-bag-check me-2 text-success"></i> My Bookings</a></li>
                                    <li><hr class="dropdown-divider"></li>
                                    <li><a class="dropdown-item py-2 text-danger fw-bold" href="#" id="signOutBtn"><i class="bi bi-box-arrow-right me-2"></i> Sign Out</a></li>
                                </ul>
                            </div>
                        </div>
"""

# We need to replace the old sign in/sign up links with this new block.
old_auth = r'<a href="signin\.html".*?</a>\s*<a href="signup\.html".*?</a>'

def apply_auth_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check if we are in subfolder, if so adjust the avatar source or it doesn't matter (external URL)
    # But adjust the signin/signup paths!
    in_subfolder = "hotels" in filepath or "Destinations" in filepath
    replacement = auth_html
    if in_subfolder:
        replacement = replacement.replace('href="signin.html"', 'href="../signin.html"').replace('href="signup.html"', 'href="../signup.html"')
        
    html = re.sub(old_auth, replacement, html, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

apply_auth_html("index.html")

for d in ["hotels", "Destinations"]:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                apply_auth_html(os.path.join(d, filename))

# 2. Update signin.html to redirect on success
with open("signin.html", "r", encoding="utf-8") as f:
    signin = f.read()
    
signin = signin.replace('// Additional check for HTML5 required fields', """// Mock login success
                    if(isValid) {
                        localStorage.setItem('isLoggedIn', 'true');
                        window.location.href = 'index.html';
                    }
                    """)
with open("signin.html", "w", encoding="utf-8") as f:
    f.write(signin)
    
print("Auth UI injected")
