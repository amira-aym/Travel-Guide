// Apply immediately to prevent flash
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-bs-theme', savedTheme);

document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const darkModeIcon = document.getElementById('darkModeIcon');
    const htmlElement = document.documentElement;

    updateIcon(savedTheme);

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            if (htmlElement.getAttribute('data-bs-theme') === 'dark') {
                htmlElement.setAttribute('data-bs-theme', 'light');
                localStorage.setItem('theme', 'light');
                updateIcon('light');
            } else {
                htmlElement.setAttribute('data-bs-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                updateIcon('dark');
            }
        });
    }

    function updateIcon(theme) {
        if (!darkModeIcon) return;
        if (theme === 'dark') {
            darkModeIcon.classList.remove('bi-moon-fill');
            darkModeIcon.classList.add('bi-sun-fill');
            if (darkModeToggle) darkModeToggle.title = 'Light Mode';
        } else {
            darkModeIcon.classList.remove('bi-sun-fill');
            darkModeIcon.classList.add('bi-moon-fill');
            if (darkModeToggle) darkModeToggle.title = 'Dark Mode';
        }
    }

    // Fix for Offcanvas Auto-Close without breaking navigation
    const navLinks = document.querySelectorAll('.offcanvas-body .nav-link');
    const offcanvasNavbar = document.getElementById('offcanvasNavbar');
    
    if (offcanvasNavbar) {
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (link.getAttribute('href') && link.getAttribute('href').includes('#')) {
                    if (offcanvasNavbar.classList.contains('show')) {
                        const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvasNavbar) || new bootstrap.Offcanvas(offcanvasNavbar);
                        bsOffcanvas.hide();
                    }
                }
            });
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const guestLinks = document.getElementById('guestLinks');
    const userLinks = document.getElementById('userLinks');
    const signOutBtn = document.getElementById('signOutBtn');

    if (localStorage.getItem('isLoggedIn') === 'true') {
        if (guestLinks) guestLinks.classList.add('d-none');
        if (guestLinks) guestLinks.classList.remove('d-flex');
        if (userLinks) userLinks.classList.remove('d-none');
        if (userLinks) userLinks.classList.add('d-flex');
    }

    if (signOutBtn) {
        signOutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            localStorage.setItem('isLoggedIn', 'false');
            window.location.reload();
        });
    }
});
// Auth logic to toggle guest/user links
document.addEventListener('DOMContentLoaded', () => {
    const guestLinks = document.getElementById('guestLinks');
    const userLinks = document.getElementById('userLinks');
    const signOutBtn = document.getElementById('signOutBtn');

    if (localStorage.getItem('isLoggedIn') === 'true') {
        if (guestLinks) {
            guestLinks.classList.add('d-none');
            guestLinks.classList.remove('d-flex');
        }
        if (userLinks) {
            userLinks.classList.remove('d-none');
            userLinks.classList.add('d-flex');
            
            // Check if Google Login
            if (localStorage.getItem('loginType') === 'google') {
                const userAvatars = document.querySelectorAll('.user-avatar');
                const userNames = document.querySelectorAll('.user-name');
                const userFirstNames = document.querySelectorAll('.user-first-name');
                
                const googleName = localStorage.getItem('googleName') || 'User';
                const firstLetter = googleName.charAt(0).toUpperCase();
                
                userAvatars.forEach(av => {
                    av.src = "https://ui-avatars.com/api/?name=" + firstLetter + "&background=2563eb&color=fff"; // Normal blue avatar
                });
                userNames.forEach(n => n.innerHTML = googleName);
                userFirstNames.forEach(n => n.innerText = googleName.split(' ')[0]);
                
                // Also update settings page email to match the name
                const settingsEmail = document.getElementById('settingsEmail');
                if(settingsEmail) {
                    settingsEmail.value = googleName.split(' ').join('.').toLowerCase() + '@gmail.com';
                }
            }
        }
    }

    if (signOutBtn) {
        signOutBtn.addEventListener('click', (e) => {
            e.preventDefault();
            localStorage.setItem('isLoggedIn', 'false');
            localStorage.removeItem('loginType');
            window.location.reload();
        });
    }
});
