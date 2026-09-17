import os
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update search bar
old_search = """<!-- Search Input Collapse -->
                <div class="collapse me-lg-3 my-2 my-lg-0" id="searchCollapse">
                    <input type="text" class="form-control" placeholder="Type to search...">
                </div>"""
new_search = """<!-- Search Input Collapse -->
                <div class="collapse me-lg-3 my-2 my-lg-0 position-relative" id="searchCollapse">
                    <input type="text" class="form-control" id="searchInput" placeholder="Search (e.g. Egypt)..." autocomplete="off">
                    <ul class="list-group position-absolute w-100 mt-1 d-none shadow-sm" id="searchSuggestions" style="max-height: 200px; overflow-y: auto; z-index: 1050;"></ul>
                </div>"""
content = content.replace(old_search, new_search)

# 2. Add Search Results Section above Destinations
old_dest = """<!-- Destinations Section -->
    <section id="destinations" class="py-5 mt-4">"""
new_dest = """<!-- Search Results Section (Hidden by default) -->
    <section id="searchResultsSection" class="py-5 mt-4 d-none">
        <div class="container">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h2 class="fw-bold fs-1 text-primary" id="searchCountryTitle">Search Results</h2>
                <button class="btn btn-outline-danger btn-sm rounded-pill px-3" id="closeResultsBtn"><i class="bi bi-x-circle"></i> Close</button>
            </div>
            <p class="text-muted fs-5 mb-5" id="searchCountryDesc"></p>
            <div class="row g-4" id="searchCitiesContainer">
                <!-- Cities will be injected here -->
            </div>
        </div>
    </section>

    <!-- Destinations Section -->
    <section id="destinations" class="py-5 mt-4">"""
content = content.replace(old_dest, new_dest)

# 3. Add script tag at the bottom
if 'src="search.js"' not in content:
    content = content.replace('</body>', '    <script src="search.js"></script>\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html")
