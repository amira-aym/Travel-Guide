import re

def update_google_btn(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
            
        old_btn = r'<button class="btn btn-outline-dark w-100 rounded-pill fw-semibold">\s*<i class="bi bi-google me-2 text-danger"></i> Sign (in|up) with Google\s*</button>'
        
        # Replace with an anchor tag that goes to Google Login
        def repl(match):
            action = match.group(1) # 'in' or 'up'
            return f'<a href="https://accounts.google.com/ServiceLogin" target="_blank" class="btn btn-outline-dark w-100 rounded-pill fw-semibold"><i class="bi bi-google me-2 text-danger"></i> Sign {action} with Google</a>'
            
        new_html = re.sub(old_btn, repl, html)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

update_google_btn("signin.html")
update_google_btn("signup.html")
