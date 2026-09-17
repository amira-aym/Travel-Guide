import os

new_script = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const bookingForm = document.getElementById('bookingForm');
            const bookingFormBody = document.getElementById('bookingFormBody');
            if(bookingForm) {
                bookingForm.addEventListener('submit', function(e) {
                    e.preventDefault();
                    
                    // Save booking to localStorage
                    const checkin = bookingForm.querySelector('input[type="date"]:nth-of-type(1)') ? bookingForm.querySelectorAll('input[type="date"]')[0].value : 'N/A';
                    const checkout = bookingForm.querySelector('input[type="date"]:nth-of-type(2)') ? bookingForm.querySelectorAll('input[type="date"]')[1].value : 'N/A';
                    const adults = bookingForm.querySelectorAll('select')[0].value;
                    const children = bookingForm.querySelectorAll('select')[1].value;
                    const roomType = bookingForm.querySelectorAll('select')[2].value;
                    
                    // Get hotel name from the page title or h1
                    const hotelName = document.querySelector('h1') ? document.querySelector('h1').innerText : 'Hotel Booking';

                    const booking = {
                        hotelName: hotelName,
                        checkin: checkin,
                        checkout: checkout,
                        adults: adults,
                        children: children,
                        roomType: roomType
                    };

                    let myBookings = JSON.parse(localStorage.getItem('myBookings') || '[]');
                    myBookings.push(booking);
                    localStorage.setItem('myBookings', JSON.stringify(myBookings));

                    bookingFormBody.innerHTML = `
                        <div class="text-center py-5">
                            <i class="bi bi-check-circle-fill text-success" style="font-size: 4rem;"></i>
                            <h3 class="fw-bold mt-3">Booking Confirmed!</h3>
                            <p class="text-muted fs-5">Thank you for your reservation. We have sent the details to your email.</p>
                            <a href="../bookings.html" class="btn btn-outline-primary px-4 rounded-pill mt-3 me-2">View My Bookings</a>
                            <button type="button" class="btn btn-primary px-4 rounded-pill mt-3" data-bs-dismiss="modal">Done</button>
                        </div>
                    `;
                });
            }
        });
    </script>
"""

def update_modal_script(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # We replace everything between <script> and </script> at the bottom (which is the modal script)
    import re
    old_script_pattern = r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) {\s*const bookingForm = document\.getElementById\(\'bookingForm\'\);.*?</script>'
    
    html = re.sub(old_script_pattern, new_script, html, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            update_modal_script(os.path.join(hotels_dir, filename))

print("Modal script updated to save bookings")
