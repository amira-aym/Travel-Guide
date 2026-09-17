import re
import random

# Get the 16 working Unsplash URLs from index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

urls = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+\?auto=format&fit=crop&w=500&q=60', html_content)
urls = list(set(urls)) # Remove duplicates if any

if len(urls) == 0:
    # Hardcoded fallbacks just in case
    urls = [
        "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1539667468225-eebb663053e6?auto=format&fit=crop&w=500&q=60",
        "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=500&q=60"
    ]

with open("search.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# I want to rewrite the JSON object in search.js so that each city gets a guaranteed URL
# I will use regex to find each img: "..." and replace it.

def replace_url(match):
    return f'img: "{random.choice(urls)}"'

# Wait, search.js doesn't have img: "..." anymore because I removed it in my last update.
# Oh, in the last update I didn't remove `img: "..."`, I only changed the HTML string inside the `handleSearch` function!
# Let's check search.js
