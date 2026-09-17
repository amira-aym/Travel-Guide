const fs = require('fs');

let js = fs.readFileSync('Jave/dark-mode.js', 'utf8');

// Replace the Google UI modification part
const oldLogic = `                userAvatars.forEach(av => {
                    av.src = "https://ui-avatars.com/api/?name=G&background=EA4335&color=fff";
                    av.classList.replace('border-primary', 'border-danger');
                });
                userNames.forEach(n => n.innerHTML = '<i class="bi bi-google text-danger me-1"></i> Google Account');
                userFirstNames.forEach(n => n.innerText = 'Google User');`;

const newLogic = `                userAvatars.forEach(av => {
                    av.src = "https://ui-avatars.com/api/?name=Amira&background=EA4335&color=fff"; // Google Red avatar
                    av.classList.replace('border-primary', 'border-danger');
                });
                userNames.forEach(n => n.innerHTML = '<i class="bi bi-google text-danger me-1"></i> Amira Aym');
                userFirstNames.forEach(n => n.innerText = 'Amira');`;

js = js.replace(oldLogic, newLogic);
fs.writeFileSync('Jave/dark-mode.js', js);
console.log("Updated dark-mode.js");
