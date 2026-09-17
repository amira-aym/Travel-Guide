import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Target the exact bad media query block
bad_media_query = re.compile(
    r'@media only screen and \(max-width: 600px\) \{\s*\.navbar \{.*?\.right-links \{.*?\}\s*\}', 
    re.DOTALL
)

css = bad_media_query.sub('', css)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Bad mobile CSS removed!")
