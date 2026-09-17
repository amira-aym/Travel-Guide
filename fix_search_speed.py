import re
import random
import time

urls = [
    "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1539667468225-eebb663053e6?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1544148103-0773bf10d330?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=500&q=60"
]

with open("search.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace all existing img: "..." with one of the fast URLs
def replacer(match):
    return f'img: "{random.choice(urls)}"'
js = re.sub(r'img:\s*"[^"]+"', replacer, js)

# Restore the fast HTML img tag without loremflickr
old_html = r'<img src="https://loremflickr.com/500/300/[^"]+" class="card-img-top"[^>]*>'
new_html = '<img src="${city.img}" class="card-img-top" alt="${city.name}" style="height: 220px; object-fit: cover;">'
js = re.sub(old_html, new_html, js)

with open("search.js", "w", encoding="utf-8") as f:
    f.write(js)

# Bust cache again in index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

timestamp = int(time.time())
html = re.sub(r'search\.js\?v=\d+', f'search.js?v={timestamp}', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Images replaced with fast CDN URLs and cache busted")
