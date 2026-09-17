import os
import re

def cache_bust(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # replace "Jave/dark-mode.js" or "Jave/dark-mode.js?v=..." with "Jave/dark-mode.js?v=2"
    html = re.sub(r'Jave/dark-mode\.js(\?v=\d+)?', 'Jave/dark-mode.js?v=2', html)
    
    # Also for search.js just in case
    html = re.sub(r'search\.js(\?v=\d+)?', 'search.js?v=2', html)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

cache_bust("index.html")
cache_bust("signin.html")
cache_bust("signup.html")
cache_bust("bookings.html")
cache_bust("settings.html")

for d in ["hotels", "Destinations"]:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                cache_bust(os.path.join(d, filename))

print("Cache busted")
