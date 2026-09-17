import re

new_google_js = """
<script>
    function simulateGoogleLogin(event) {
        event.preventDefault();
        
        const userName = prompt("Please choose a Google Account to continue (Enter your Name):");
        if (!userName || userName.trim() === "") {
            return;
        }

        const btn = event.currentTarget;
        const originalText = btn.innerHTML;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Connecting...';
        btn.disabled = true;
        
        setTimeout(() => {
            localStorage.setItem('isLoggedIn', 'true');
            localStorage.setItem('loginType', 'google');
            localStorage.setItem('googleName', userName);
            window.location.href = 'index.html';
        }, 1200);
    }
</script>
"""

def update_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    old_script = r'<script>\s*function simulateGoogleLogin.*?setTimeout.*?</script>'
    
    html = re.sub(old_script, new_google_js.strip(), html, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

update_script("signin.html")
update_script("signup.html")

print("Updated simulateGoogleLogin in auth pages")
