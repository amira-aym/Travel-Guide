import re

new_js = """
<script>
    function simulateGoogleLogin(event) {
        event.preventDefault();
        const btn = event.currentTarget;
        
        // No custom prompt, just simulate immediate login to act like a seamless OAuth
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Authenticating...';
        btn.disabled = true;
        
        setTimeout(() => {
            localStorage.setItem('isLoggedIn', 'true');
            localStorage.setItem('loginType', 'google');
            // We use 'Amira' or 'User' as default since we can't pull real Google data without backend
            if(!localStorage.getItem('googleName')) {
                localStorage.setItem('googleName', 'Amira');
            }
            window.location.href = 'index.html';
        }, 1500);
    }
</script>
"""

def update_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # We replace everything from <script> to </script> that contains simulateGoogleLogin
    # The previous one had a lot of custom overlay code.
    old_script = r'<script>\s*function simulateGoogleLogin.*?setTimeout.*?</script>'
    
    html = re.sub(old_script, new_js.strip(), html, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

update_script("signin.html")
update_script("signup.html")

print("Removed custom prompt from google login")
