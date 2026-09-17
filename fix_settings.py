import re

floating_btn = """
    <!-- Floating Back Button -->
    <button onclick="history.back()" class="btn btn-primary rounded-circle shadow-lg position-fixed d-flex align-items-center justify-content-center" style="bottom: 30px; left: 30px; width: 60px; height: 60px; z-index: 1050;" title="Go Back">
        <i class="bi bi-arrow-left fs-3"></i>
    </button>
</body>
"""

# Add floating btn to bookings.html
with open("bookings.html", "r", encoding="utf-8") as f:
    b = f.read()
if 'history.back()' not in b:
    b = b.replace('</body>', floating_btn)
    with open("bookings.html", "w", encoding="utf-8") as f:
        f.write(b)

# Fix settings.html
with open("settings.html", "r", encoding="utf-8") as f:
    s = f.read()

# Add floating btn
if 'history.back()' not in s:
    s = s.replace('</body>', floating_btn)

# Add password eye toggles
pwd_old = r'<div class="mb-[34]">\s*<label class="form-label text-muted">(.*?)</label>\s*<input type="password" class="form-control">\s*</div>'
def repl_pwd(m):
    label = m.group(1)
    return f"""<div class="mb-3">
        <label class="form-label text-muted">{label}</label>
        <div class="input-group">
            <input type="password" class="form-control">
            <button class="btn btn-outline-secondary toggle-password" type="button"><i class="bi bi-eye"></i></button>
        </div>
    </div>"""
s = re.sub(pwd_old, repl_pwd, s)

# Replace all "Save Changes" / "Save Preferences" / "Update Password" / "Save Settings" buttons with simulated save logic
# We add a green alert div at the top of the tab-content
alert_html = '<div id="settingsAlert" class="alert alert-success d-none fw-bold shadow-sm" role="alert"><i class="bi bi-check-circle-fill me-2"></i> Settings saved successfully!</div>\n                    <!-- Personal Info -->'
if 'id="settingsAlert"' not in s:
    s = s.replace('<!-- Personal Info -->', alert_html)

# Add onclick to all primary/danger save buttons
s = s.replace('<button type="button" class="btn btn-primary rounded-pill px-4 fw-bold">Save Changes</button>', '<button type="button" class="btn btn-primary rounded-pill px-4 fw-bold" onclick="showSaveAlert()">Save Changes</button>')
s = s.replace('<button class="btn btn-primary rounded-pill px-4 mt-3 fw-bold">Save Preferences</button>', '<button type="button" class="btn btn-primary rounded-pill px-4 mt-3 fw-bold" onclick="showSaveAlert()">Save Preferences</button>')
s = s.replace('<button class="btn btn-danger rounded-pill px-4 fw-bold">Update Password</button>', '<button type="button" class="btn btn-danger rounded-pill px-4 fw-bold" onclick="showSaveAlert()">Update Password</button>')
s = s.replace('<button class="btn btn-primary rounded-pill px-4 mt-4 fw-bold">Save Settings</button>', '<button type="button" class="btn btn-primary rounded-pill px-4 mt-4 fw-bold" onclick="showSaveAlert()">Save Settings</button>')

# Inject JS for toggle password and save alert
js = """
    <script>
        function showSaveAlert() {
            const alert = document.getElementById('settingsAlert');
            alert.classList.remove('d-none');
            setTimeout(() => alert.classList.add('d-none'), 3000);
        }

        document.addEventListener('DOMContentLoaded', () => {
            document.querySelectorAll('.toggle-password').forEach(btn => {
                btn.addEventListener('click', function() {
                    const input = this.previousElementSibling;
                    const icon = this.querySelector('i');
                    if (input.type === 'password') {
                        input.type = 'text';
                        icon.classList.remove('bi-eye');
                        icon.classList.add('bi-eye-slash');
                    } else {
                        input.type = 'password';
                        icon.classList.remove('bi-eye-slash');
                        icon.classList.add('bi-eye');
                    }
                });
            });
        });
    </script>
</body>"""
s = s.replace('</body>', js)

with open("settings.html", "w", encoding="utf-8") as f:
    f.write(s)

print("Settings and Bookings fixed")
