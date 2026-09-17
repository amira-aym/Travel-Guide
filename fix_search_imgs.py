import re

with open("search.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the custom img tag with standard Bootstrap card-img-top
old_img = '<img src="${city.img}" alt="${city.name}" style="width: 100%; height: 220px; object-fit: cover; display: block;">'
new_img = '<img src="${city.img}" class="card-img-top" alt="${city.name}" style="height: 220px; object-fit: cover;" onerror="this.src=\'https://placehold.co/500x300?text=Image+Not+Found\'">'

js = js.replace(old_img, new_img)

with open("search.js", "w", encoding="utf-8") as f:
    f.write(js)

print("search.js images fixed")
