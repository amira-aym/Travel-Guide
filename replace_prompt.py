import re

custom_prompt_js = """
<script>
    function simulateGoogleLogin(event) {
        event.preventDefault();
        const btn = event.currentTarget;
        
        // Create custom modal since window.prompt might be blocked in iframes
        const overlay = document.createElement('div');
        overlay.style.position = 'fixed';
        overlay.style.top = '0'; overlay.style.left = '0';
        overlay.style.width = '100vw'; overlay.style.height = '100vh';
        overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
        overlay.style.display = 'flex';
        overlay.style.alignItems = 'center';
        overlay.style.justifyContent = 'center';
        overlay.style.zIndex = '9999';
        
        const dialog = document.createElement('div');
        dialog.style.backgroundColor = 'white';
        dialog.style.padding = '20px';
        dialog.style.borderRadius = '8px';
        dialog.style.width = '300px';
        dialog.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
        dialog.style.textAlign = 'center';
        
        dialog.innerHTML = `
            <h5 style="margin-bottom: 15px; font-weight: bold;">Google Sign In</h5>
            <p style="margin-bottom: 15px; font-size: 14px; color: #666;">Enter your Google Account Name:</p>
            <input type="text" id="customPromptInput" class="form-control" style="margin-bottom: 15px;" placeholder="e.g. Mohamed Ali">
            <div style="display: flex; gap: 10px; justify-content: center;">
                <button id="customPromptCancel" class="btn btn-secondary btn-sm">Cancel</button>
                <button id="customPromptOk" class="btn btn-primary btn-sm">Continue</button>
            </div>
        `;
        
        overlay.appendChild(dialog);
        document.body.appendChild(overlay);
        
        document.getElementById('customPromptInput').focus();
        
        document.getElementById('customPromptCancel').onclick = function() {
            document.body.removeChild(overlay);
        };
        
        document.getElementById('customPromptOk').onclick = function() {
            const userName = document.getElementById('customPromptInput').value;
            document.body.removeChild(overlay);
            
            if (!userName || userName.trim() === "") {
                return;
            }
            
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Connecting...';
            btn.disabled = true;
            
            setTimeout(() => {
                localStorage.setItem('isLoggedIn', 'true');
                localStorage.setItem('loginType', 'google');
                localStorage.setItem('googleName', userName);
                window.location.href = 'index.html';
            }, 1200);
        };
    }
</script>
"""

def update_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    old_script = r'<script>\s*function simulateGoogleLogin.*?</script>'
    
    html = re.sub(old_script, custom_prompt_js.strip(), html, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

update_script("signin.html")
update_script("signup.html")

print("Replaced window.prompt with custom HTML modal")
