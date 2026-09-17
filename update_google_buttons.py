import re

google_js = """
<script>
    function simulateGoogleLogin(event) {
        event.preventDefault();
        const btn = event.currentTarget;
        const originalText = btn.innerHTML;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Connecting...';
        btn.disabled = true;
        
        setTimeout(() => {
            localStorage.setItem('isLoggedIn', 'true');
            localStorage.setItem('loginType', 'google');
            window.location.href = 'index.html';
        }, 1200);
    }
</script>
</body>
"""

def update_google_btn(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # We want to replace the anchor tag back to a button that calls simulateGoogleLogin
    pattern = r'<a href="https://accounts.google.com/ServiceLogin" target="_blank" onclick=".*?" class="btn btn-outline-dark w-100 rounded-pill fw-semibold">(.*?)</a>'
    
    def repl(m):
        content = m.group(1)
        return f'<button type="button" class="btn btn-outline-dark w-100 rounded-pill fw-semibold" onclick="simulateGoogleLogin(event)">{content}</button>'
    
    html = re.sub(pattern, repl, html)
    
    if 'simulateGoogleLogin' not in html:
        html = html.replace('</body>', google_js)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

update_google_btn("signin.html")
update_google_btn("signup.html")

print("Google buttons updated to fake login")
