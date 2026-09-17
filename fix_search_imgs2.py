import re

with open("search.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the img tag in search.js
# We'll use loremflickr as the primary image source for dynamically generated cities because it searches by keyword!
old_img_regex = r'<img src="\$\{city\.img\}" class="card-img-top"[^>]*>'
new_img = '<img src="https://loremflickr.com/500/300/${city.name.replace(\' \', \'\')},travel/all" class="card-img-top" alt="${city.name}" style="height: 220px; object-fit: cover;" onerror="this.src=\'https://picsum.photos/seed/${city.name}/500/300\'">'

js = re.sub(old_img_regex, new_img, js)

with open("search.js", "w", encoding="utf-8") as f:
    f.write(js)

print("search.js images fixed to use loremflickr")
