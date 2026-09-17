import re

def add_google_onclick(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # We want to replace the href with an onclick that simulates the redirect
    pattern = r'<a href="https://accounts.google.com/ServiceLogin" target="_blank" class="btn btn-outline-dark w-100 rounded-pill fw-semibold">'
    
    new_tag = '<a href="https://accounts.google.com/ServiceLogin" target="_blank" onclick="localStorage.setItem(\'isLoggedIn\', \'true\'); localStorage.setItem(\'loginType\', \'google\'); setTimeout(() => window.location.href=\'index.html\', 1500);" class="btn btn-outline-dark w-100 rounded-pill fw-semibold">'
    
    html = html.replace(pattern, new_tag)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

add_google_onclick("signin.html")
add_google_onclick("signup.html")
print("Google onclick added")
