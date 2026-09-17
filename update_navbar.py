import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_nav_pattern = r'<nav id="mainNavbar"[^>]*>.*?</nav>'

new_nav = """<nav id="mainNavbar" class="navbar navbar-expand-lg bg-body position-sticky top-0 start-0 end-0 border-bottom z-3">
        <div class="container-fluid px-4">

            <!-- Logo -->
            <a class="navbar-brand logo fw-bold text-body fs-3 d-flex align-items-center" href="#">
                <i class="bi bi-airplane-engines-fill text-primary me-2"></i> travel guide
            </a>

            <!-- Toggler Button for Mobile (Offcanvas) -->
            <button class="navbar-toggler border-0 shadow-none" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <!-- Offcanvas Navbar Content -->
            <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <div class="offcanvas-header border-bottom">
                    <h5 class="offcanvas-title fw-bold d-flex align-items-center" id="offcanvasNavbarLabel">
                        <i class="bi bi-airplane-engines-fill text-primary me-2"></i> travel guide
                    </h5>
                    <button type="button" class="btn-close shadow-none" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div class="offcanvas-body">
                    <!-- Center Links -->
                    <ul class="navbar-nav mx-auto mb-2 mb-lg-0 align-items-lg-center">
                        <li class="nav-item">
                            <a class="nav-link custom-hover fw-semibold px-lg-3 text-body" href="#destinations">DESTINATIONS</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link custom-hover fw-semibold px-lg-3 text-body" href="#things-to-do">THINGS TO DO</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link custom-hover fw-semibold px-lg-3 text-body" href="#restaurants">RESTAURANTS</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link custom-hover fw-semibold px-lg-3 text-body" href="#travel-tips">TRAVEL TIPS</a>
                        </li>
                        
                        <li class="nav-item">
                            <a class="nav-link px-lg-2 text-body search-btn" data-bs-toggle="collapse" href="#searchCollapse" role="button" aria-expanded="false" aria-controls="searchCollapse">
                                <i class="bi bi-search"></i> <span class="d-lg-none ms-2">Search</span>
                            </a>
                        </li>
                    </ul>

                    <!-- Search Input Collapse -->
                    <div class="collapse me-lg-3 my-2 my-lg-0 position-relative" id="searchCollapse">
                        <input type="text" class="form-control" id="searchInput" placeholder="Search (e.g. Egypt)..." autocomplete="off">
                        <ul class="list-group position-absolute w-100 mt-1 d-none shadow-sm" id="searchSuggestions" style="max-height: 200px; overflow-y: auto; z-index: 1050;"></ul>
                    </div>

                    <!-- Right Links -->
                    <div class="d-flex align-items-center right-links gap-3 mt-3 mt-lg-0 border-top border-lg-0 pt-3 pt-lg-0">
                        <!-- Dark Mode Toggle -->
                        <button class="btn btn-link nav-link px-2 dark-mode-btn" id="darkModeToggle" aria-label="Toggle Dark Mode" title="Dark Mode">
                            <i class="bi bi-moon-fill" id="darkModeIcon"></i>
                        </button>
                        <a href="signin.html" class="nav-link auth-link fw-semibold">SIGN IN</a>
                        <a href="signup.html" class="btn btn-primary btn-sm fw-semibold shadow-sm rounded-pill px-3">SIGN UP</a>
                    </div>
                </div>
            </div>

        </div>
    </nav>"""

html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Navbar converted to Offcanvas and Logo added")
