import os

floating_btn = """
    <!-- Floating Back Button -->
    <button onclick="history.back()" class="btn btn-primary rounded-circle shadow-lg position-fixed d-flex align-items-center justify-content-center" style="bottom: 30px; left: 30px; width: 60px; height: 60px; z-index: 1050;" title="Go Back">
        <i class="bi bi-arrow-left fs-3"></i>
    </button>
</body>
"""

dest_dir = "Destinations"
if os.path.exists(dest_dir):
    for filename in os.listdir(dest_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(dest_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if 'onclick="history.back()"' not in content:
                content = content.replace('</body>', floating_btn)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)

print("Floating back buttons added to Destinations pages")
