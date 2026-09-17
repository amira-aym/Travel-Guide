import os
import re

modal_html = """
    <!-- Booking Modal -->
    <div class="modal fade" id="bookingModal" tabindex="-1" aria-labelledby="bookingModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content border-0 shadow">
                <div class="modal-header bg-primary text-white border-0">
                    <h5 class="modal-title fw-bold" id="bookingModalLabel"><i class="bi bi-calendar-check me-2"></i> Book Your Stay</h5>
                    <button type="button" class="btn-close btn-close-white shadow-none" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body p-4" id="bookingFormBody">
                    <form id="bookingForm">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label fw-bold">Full Name</label>
                                <input type="text" class="form-control" required placeholder="John Doe">
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-bold">Email Address</label>
                                <input type="email" class="form-control" required placeholder="john@example.com">
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-bold">Check-in Date</label>
                                <input type="date" class="form-control" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-bold">Check-out Date</label>
                                <input type="date" class="form-control" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label fw-bold">Adults</label>
                                <select class="form-select">
                                    <option value="1">1 Adult</option>
                                    <option value="2" selected>2 Adults</option>
                                    <option value="3">3 Adults</option>
                                    <option value="4">4 Adults</option>
                                </select>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label fw-bold">Children</label>
                                <select class="form-select">
                                    <option value="0">0 Children</option>
                                    <option value="1">1 Child</option>
                                    <option value="2">2 Children</option>
                                    <option value="3">3 Children</option>
                                </select>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label fw-bold">Room Type</label>
                                <select class="form-select">
                                    <option value="standard">Standard Room</option>
                                    <option value="deluxe">Deluxe Room</option>
                                    <option value="suite">Luxury Suite</option>
                                </select>
                            </div>
                            <div class="col-12 mt-4">
                                <button type="submit" class="btn btn-primary w-100 py-3 fw-bold fs-5 rounded-pill">Confirm Reservation</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const bookingForm = document.getElementById('bookingForm');
            const bookingFormBody = document.getElementById('bookingFormBody');
            if(bookingForm) {
                bookingForm.addEventListener('submit', function(e) {
                    e.preventDefault();
                    bookingFormBody.innerHTML = `
                        <div class="text-center py-5">
                            <i class="bi bi-check-circle-fill text-success" style="font-size: 4rem;"></i>
                            <h3 class="fw-bold mt-3">Booking Confirmed!</h3>
                            <p class="text-muted fs-5">Thank you for your reservation. We have sent the details to your email.</p>
                            <button type="button" class="btn btn-primary px-5 rounded-pill mt-3" data-bs-dismiss="modal">Done</button>
                        </div>
                    `;
                });
            }
        });
    </script>
"""

hotels_dir = "hotels"
if os.path.exists(hotels_dir):
    for filename in os.listdir(hotels_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(hotels_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Make the Book Now button trigger the modal
            old_btn = '<button class="btn btn-primary w-100 py-3 rounded-pill fw-bold">Book Now</button>'
            new_btn = '<button class="btn btn-primary w-100 py-3 rounded-pill fw-bold" data-bs-toggle="modal" data-bs-target="#bookingModal">Book Now</button>'
            content = content.replace(old_btn, new_btn)
            
            # Inject the modal before the body closing tag
            if 'id="bookingModal"' not in content:
                # Need to find floating btn or just insert right before </body>
                content = content.replace('</body>', modal_html + '\n</body>')
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Booking modal added to all hotel pages")
