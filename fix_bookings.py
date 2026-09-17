with open("bookings.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
old_js = r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => {.*?</script>'

new_js = """<script>
    document.addEventListener('DOMContentLoaded', () => {
        const bookingsJSON = localStorage.getItem('myBookings');
        const emptyBookings = document.getElementById('emptyBookings');
        const bookingsContainer = document.getElementById('bookingsContainer');

        if (!bookingsJSON || JSON.parse(bookingsJSON).length === 0) {
            emptyBookings.classList.remove('d-none');
        } else {
            bookingsContainer.classList.remove('d-none');
            const bookings = JSON.parse(bookingsJSON);
            
            bookings.forEach((booking, index) => {
                const col = document.createElement('div');
                col.className = 'col-md-6 col-lg-4';
                col.innerHTML = `
                    <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
                        <div class="bg-primary text-white p-3 d-flex justify-content-between align-items-center">
                            <span class="fw-bold"><i class="bi bi-building"></i> ${booking.hotelName}</span>
                            <span class="badge bg-light text-primary">Confirmed</span>
                        </div>
                        <div class="card-body">
                            <p class="mb-2"><i class="bi bi-box-arrow-in-right text-muted me-2"></i> <strong>Check-in:</strong> ${booking.checkin}</p>
                            <p class="mb-2"><i class="bi bi-box-arrow-left text-muted me-2"></i> <strong>Check-out:</strong> ${booking.checkout}</p>
                            <p class="mb-2"><i class="bi bi-people text-muted me-2"></i> <strong>Guests:</strong> ${booking.adults} Adults, ${booking.children} Children</p>
                            <p class="mb-0"><i class="bi bi-key text-muted me-2"></i> <strong>Room:</strong> <span class="text-capitalize">${booking.roomType}</span></p>
                        </div>
                        <div class="card-footer bg-white border-top-0 pb-3 text-center">
                            <button class="btn btn-outline-danger btn-sm rounded-pill px-3" onclick="cancelBooking(${index})"><i class="bi bi-x-circle"></i> Cancel Booking</button>
                        </div>
                    </div>
                `;
                bookingsContainer.appendChild(col);
            });
        }
    });

    function cancelBooking(index) {
        if(confirm("Are you sure you want to cancel this booking?")) {
            const bookings = JSON.parse(localStorage.getItem('myBookings'));
            bookings.splice(index, 1);
            localStorage.setItem('myBookings', JSON.stringify(bookings));
            window.location.reload();
        }
    }
</script>"""

content = re.sub(old_js, new_js, content, flags=re.DOTALL)
with open("bookings.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed JS in bookings.html")
