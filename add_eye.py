import re

js_code = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtns = document.querySelectorAll('.toggle-password');
    toggleBtns.forEach(btn => {
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
</body>
"""

def add_eye(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        # Find the password input and the following invalid-feedback
        # old:
        # <input type="password" class="form-control" id="password" placeholder="..." required>
        # <div class="invalid-feedback">...</div>
        
        pattern = r'(<input type="password" class="form-control" id="password" placeholder=".*?" required>)\s*(<div class="invalid-feedback">.*?</div>)'
        
        def repl(m):
            input_tag = m.group(1)
            feedback_tag = m.group(2)
            return f'<div class="input-group has-validation">\n                            {input_tag}\n                            <button class="btn btn-outline-secondary toggle-password" type="button"><i class="bi bi-eye"></i></button>\n                            {feedback_tag}\n                        </div>'
            
        html = re.sub(pattern, repl, html)
        
        # Add JS
        if 'toggle-password' in html and 'const toggleBtns' not in html:
            html = html.replace('</body>', js_code)
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
            
        print(f"Added eye to {filepath}")
    except Exception as e:
        print(f"Error {filepath}: {e}")

add_eye("signin.html")
add_eye("signup.html")
