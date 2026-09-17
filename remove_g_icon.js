const fs = require('fs');
let js = fs.readFileSync('Jave/dark-mode.js', 'utf8');

// Remove the red G icon logic. We just make the Google login look exactly like a normal login, 
// maybe just using their name or a default name without the G logo.
const oldLogic = `                const googleName = localStorage.getItem('googleName') || 'Google User';
                const firstLetter = googleName.charAt(0).toUpperCase();
                
                userAvatars.forEach(av => {
                    av.src = "https://ui-avatars.com/api/?name=" + firstLetter + "&background=EA4335&color=fff"; // Google Red avatar
                    av.classList.replace('border-primary', 'border-danger');
                });
                userNames.forEach(n => n.innerHTML = '<i class="bi bi-google text-danger me-1"></i> ' + googleName);
                userFirstNames.forEach(n => n.innerText = googleName.split(' ')[0]);
                
                // Also update settings page email to match the name
                const settingsEmail = document.getElementById('settingsEmail');
                if(settingsEmail) {
                    settingsEmail.value = googleName.split(' ').join('.').toLowerCase() + '@gmail.com';
                    settingsEmail.disabled = true;
                }`;

const newLogic = `                const googleName = localStorage.getItem('googleName') || 'User';
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
                }`;

js = js.replace(oldLogic, newLogic);
fs.writeFileSync('Jave/dark-mode.js', js);
console.log("Removed Google G icon from dark-mode.js");
