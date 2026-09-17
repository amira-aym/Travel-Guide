import urllib.request
import json
import re
import time

cities = [
    "Bodrum", "Fethiye", "Rome", "Venice", "Florence", "Milan", "Naples", "Positano",
    "Paris", "Nice", "Lyon", "Marseille", "Bordeaux", "Strasbourg",
    "Tokyo", "Kyoto", "Osaka", "Hokkaido", "Nara", "Hiroshima"
]

city_images = {}

for city in cities:
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(city)}&prop=pageimages&format=json&pithumbsize=500"
        req = urllib.request.Request(url, headers={'User-Agent': 'CoolBot/1.0 (test@example.com)'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data['query']['pages']
            for page_id in pages:
                if 'thumbnail' in pages[page_id]:
                    img_url = pages[page_id]['thumbnail']['source']
                    city_images[city] = img_url
                    break
    except Exception as e:
        print(f"Failed for {city}: {e}")
    time.sleep(1)

with open("search.js", "r", encoding="utf-8") as f:
    js = f.read()

for city, img in city_images.items():
    pattern = r'\{ name: "' + city + r'", img: "[^"]+"'
    replacement = f'{{ name: "{city}", img: "{img}"'
    js = re.sub(pattern, replacement, js)

with open("search.js", "w", encoding="utf-8") as f:
    f.write(js)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()
timestamp = int(time.time())
html = re.sub(r'search\.js\?v=\d+', f'search.js?v={timestamp}', html)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Injected Wikipedia images for the rest!")
