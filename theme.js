
// Immediately apply the saved theme to avoid flashing
const savedTheme = localStorage.getItem('travelGuideTheme');
if (savedTheme) {
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
}

document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const darkModeIcon = document.getElementById('darkModeIcon');
    const htmlElement = document.documentElement;

    // Set correct icon on load
    if (darkModeIcon) {
        if (htmlElement.getAttribute('data-bs-theme') === 'dark') {
            darkModeIcon.classList.remove('bi-moon-fill');
            darkModeIcon.classList.add('bi-sun-fill');
            if(darkModeToggle) darkModeToggle.title = 'Light Mode';
        } else {
            darkModeIcon.classList.remove('bi-sun-fill');
            darkModeIcon.classList.add('bi-moon-fill');
            if(darkModeToggle) darkModeToggle.title = 'Dark Mode';
        }
    }

    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            if (htmlElement.getAttribute('data-bs-theme') === 'dark') {
                htmlElement.setAttribute('data-bs-theme', 'light');
                localStorage.setItem('travelGuideTheme', 'light');
                if (darkModeIcon) {
                    darkModeIcon.classList.remove('bi-sun-fill');
                    darkModeIcon.classList.add('bi-moon-fill');
                }
                darkModeToggle.title = 'Dark Mode';
            } else {
                htmlElement.setAttribute('data-bs-theme', 'dark');
                localStorage.setItem('travelGuideTheme', 'dark');
                if (darkModeIcon) {
                    darkModeIcon.classList.remove('bi-moon-fill');
                    darkModeIcon.classList.add('bi-sun-fill');
                }
                darkModeToggle.title = 'Light Mode';
            }
        });
    }
});
