import os

hotels = [
    {
        "id": "paris",
        "title": "Le Grand Paris Hotel",
        "location": "Paris, France",
        "img": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
        "rating": "4.8",
        "address": "12 Avenue Montaigne, 75008 Paris, France",
        "desc": "Experience luxury like never before. Located just steps away from the Eiffel Tower, our hotel offers classic French elegance, world-class dining, and breathtaking rooftop views."
    },
    {
        "id": "kyoto",
        "title": "Traditional Ryokan & Spa",
        "location": "Kyoto, Japan",
        "img": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
        "rating": "4.9",
        "address": "Gion District, Kyoto, Japan",
        "desc": "Immerse yourself in authentic Japanese culture. Enjoy soothing hot springs, tatami mat rooms, and kaiseki dining in the heart of Kyoto's historic district."
    },
    {
        "id": "santorini",
        "title": "Caldera View Resort",
        "location": "Santorini, Greece",
        "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80",
        "rating": "4.7",
        "address": "Oia, Santorini 847 02, Greece",
        "desc": "Perched on the famous cliffs of Oia, our resort offers uninterrupted panoramic views of the Aegean Sea, infinity pools, and spectacular sunset dining."
    },
    {
        "id": "cairo",
        "title": "Nile Ritz-Carlton",
        "location": "Cairo, Egypt",
        "img": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
        "rating": "4.8",
        "address": "1113 Corniche El Nil, Cairo, Egypt",
        "desc": "A luxurious oasis in the bustling city. Overlooking the majestic Nile River and right next to the Egyptian Museum, offering unparalleled service and comfort."
    },
    {
        "id": "rome",
        "title": "Hotel de Russie",
        "location": "Rome, Italy",
        "img": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?auto=format&fit=crop&w=1200&q=80",
        "rating": "4.9",
        "address": "Via del Babuino 9, 00187 Rome, Italy",
        "desc": "A favorite among travelers and celebrities. Known for its extensive secret garden, luxurious rooms, and prime location near the Spanish Steps."
    },
    {
        "id": "newyork",
        "title": "The Plaza Hotel",
        "location": "New York, USA",
        "img": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=1200&q=80",
        "rating": "4.6",
        "address": "768 5th Ave, New York, NY 10019, USA",
        "desc": "The ultimate New York experience. An iconic 19th-century luxury hotel situated perfectly at the southern edge of Central Park in Manhattan."
    }
]

template = """<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Travel Guide</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        .hero-header {{
            height: 60vh;
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), url('{img}');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
        }}
        .rating i {{ color: #ffc107; }}
    </style>
</head>
<body class="bg-body">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg border-bottom py-3 bg-body">
        <div class="container">
            <a class="navbar-brand fw-bold text-body" href="../index.html"><i class="bi bi-airplane-fill text-primary"></i> travel guide</a>
            <a href="../index.html" class="btn btn-outline-primary btn-sm rounded-pill px-4"><i class="bi bi-arrow-left"></i> Back to Home</a>
        </div>
    </nav>

    <!-- Hero -->
    <header class="hero-header">
        <div class="container">
            <span class="badge bg-primary mb-3 px-3 py-2 rounded-pill fs-6"><i class="bi bi-geo-alt-fill"></i> {location}</span>
            <h1 class="display-3 fw-bold mb-3">{title}</h1>
            <div class="rating fs-4 mb-4">
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-fill"></i>
                <i class="bi bi-star-half"></i>
                <span class="text-light ms-2 fs-5">({rating} / 5)</span>
            </div>
        </div>
    </header>

    <!-- Details -->
    <section class="py-5 container">
        <div class="row g-5">
            <div class="col-lg-8">
                <h3 class="fw-bold mb-4">About The Hotel</h3>
                <p class="fs-5 text-muted lh-lg">{desc}</p>
                
                <h4 class="fw-bold mt-5 mb-4">Amenities</h4>
                <div class="row g-3 text-muted">
                    <div class="col-sm-6"><i class="bi bi-wifi text-primary me-2"></i> Free High-Speed WiFi</div>
                    <div class="col-sm-6"><i class="bi bi-cup-hot-fill text-primary me-2"></i> Complimentary Breakfast</div>
                    <div class="col-sm-6"><i class="bi bi-water text-primary me-2"></i> Swimming Pool & Spa</div>
                    <div class="col-sm-6"><i class="bi bi-car-front-fill text-primary me-2"></i> Free Parking</div>
                </div>
            </div>
            
            <div class="col-lg-4">
                <div class="card border-0 shadow-sm p-4 bg-body-tertiary">
                    <h5 class="fw-bold mb-4">Location</h5>
                    <p class="text-muted"><i class="bi bi-geo-alt text-danger me-2"></i> {address}</p>
                    <hr>
                    <p class="fs-4 fw-bold text-success mb-1">$240 <span class="fs-6 text-muted fw-normal">/ night</span></p>
                    <p class="small text-muted mb-4">Taxes and fees included</p>
                    <button class="btn btn-primary w-100 py-3 rounded-pill fw-bold">Book Now</button>
                </div>
            </div>
        </div>
    </section>

</body>
</html>"""

os.makedirs("hotels", exist_ok=True)

for h in hotels:
    content = template.format(**h)
    with open(f"hotels/{h['id']}.html", "w", encoding="utf-8") as f:
        f.write(content)

print("Created hotel details pages in 'hotels' directory.")
