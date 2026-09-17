google_script = """
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
"""

def inject_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    if 'function simulateGoogleLogin' not in html:
        html = html.replace('</body>', google_script + '\n</body>')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

inject_script("signin.html")
inject_script("signup.html")
print("Injected missing Google script")
