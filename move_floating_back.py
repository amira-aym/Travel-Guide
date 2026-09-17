import os

hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(hotels_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            content = content.replace('right: 30px;', 'left: 30px;')
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Moved floating button to the left side")
