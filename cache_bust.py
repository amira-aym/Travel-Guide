import re
import time

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Bust cache for search.js by appending a timestamp
timestamp = int(time.time())
content = re.sub(r'search\.js\?v=\d+', f'search.js?v={timestamp}', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated with cache bust")
