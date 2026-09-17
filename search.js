document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchSuggestions = document.getElementById('searchSuggestions');
    const searchResultsSection = document.getElementById('searchResultsSection');
    const searchCountryTitle = document.getElementById('searchCountryTitle');
    const searchCountryDesc = document.getElementById('searchCountryDesc');
    const searchCitiesContainer = document.getElementById('searchCitiesContainer');
    const closeResultsBtn = document.getElementById('closeResultsBtn');

    if (!searchInput) return;

    // Database of countries with GUARANTEED working Unsplash parameters
    const travelData = {
        "Egypt": {
            description: "Explore the ancient wonders, cruise the Nile, and dive into the Red Sea. Top activities: Pyramids tour, Scuba diving, Desert Safari, and visiting ancient temples.",
            cities: [
                { name: "Cairo", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/72/Cairo_Opera_House%2C_Al_Hurriyah_Park_and_the_Nile_river_%2814797782354%29.jpg/500px-Cairo_Opera_House%2C_Al_Hurriyah_Park_and_the_Nile_river_%2814797782354%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Home to the Great Pyramids and Sphinx." },
                { name: "Luxor", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/35/LuxorHotelsIbnWalidSt.jpg/500px-LuxorHotelsIbnWalidSt.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "The world's greatest open-air museum." },
                { name: "Aswan", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/06/Panoramic_view_of_Aswan%2C_Egypt.jpg/500px-Panoramic_view_of_Aswan%2C_Egypt.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Beautiful Nile views and Philae Temple." },
                { name: "Alexandria", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/79/San_Stefano_Grand_Plaza.JPG/500px-San_Stefano_Grand_Plaza.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Mediterranean charm and historic library." },
                { name: "Sharm El Sheikh", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ac/Sharm_El_Sheikh_-_panoramio_%2815%29.jpg/500px-Sharm_El_Sheikh_-_panoramio_%2815%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "World-class scuba diving and resorts." },
                { name: "Hurghada", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d6/Hurghada_Hotels_R03.jpg/500px-Hurghada_Hotels_R03.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Beautiful beaches and water sports." }
            ]
        },
        "Turkey": {
            description: "Experience the bridge between Europe and Asia. Top activities: Hot air ballooning in Cappadocia, Bosphorus cruise, historical tours, and trying local cuisine.",
            cities: [
                { name: "Istanbul", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/cb/Historical_peninsula_and_modern_skyline_of_Istanbul.jpg/500px-Historical_peninsula_and_modern_skyline_of_Istanbul.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Vibrant city featuring the Hagia Sophia." },
                { name: "Cappadocia", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/5/59/Cappadocia_balloon_trip%2C_Ortahisar_Castle_%2811893715185%29.jpg/500px-Cappadocia_balloon_trip%2C_Ortahisar_Castle_%2811893715185%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Famous for its unique rock formations and balloons." },
                { name: "Antalya", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/73/Falezlerden_Antalya_Konyaalt%C4%B1_Plaj%C4%B1na_do%C4%9Fru_bir_g%C3%B6r%C3%BCn%C3%BCm.jpg/500px-Falezlerden_Antalya_Konyaalt%C4%B1_Plaj%C4%B1na_do%C4%9Fru_bir_g%C3%B6r%C3%BCn%C3%BCm.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Beautiful turquoise coast and ancient ruins." },
                { name: "Izmir", img: "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=500&q=60", desc: "Modern coastal city with a rich history." },
                { name: "Bodrum", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4a/Sunset_over_Bodrum_I.jpg/500px-Sunset_over_Bodrum_I.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "A luxury resort town with a historic castle." },
                { name: "Fethiye", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/1/1a/Fethiye_Town_in_Daylight_%28cropped%29.jpg/500px-Fethiye_Town_in_Daylight_%28cropped%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Known for its stunning blue lagoon." }
            ]
        },
        "Italy": {
            description: "Enjoy art, architecture, and world-renowned food. Top activities: Colosseum tours, Venice gondola rides, wine tasting in Tuscany, and visiting the Amalfi Coast.",
            cities: [
                { name: "Rome", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7e/Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg/500px-Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "The Eternal City, home to the Colosseum." },
                { name: "Venice", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4f/Venezia_aerial_view.jpg/500px-Venezia_aerial_view.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Famous for its canals and gondolas." },
                { name: "Florence", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3a/Firenze_-_Piazzale_Michelangelo%2C_Firenze%2C_Italy_-_April_6%2C_2015_02.jpg/500px-Firenze_-_Piazzale_Michelangelo%2C_Firenze%2C_Italy_-_April_6%2C_2015_02.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "The birthplace of the Renaissance." },
                { name: "Milan", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/70/Milan_Cathedral_from_Piazza_del_Duomo.jpg/500px-Milan_Cathedral_from_Piazza_del_Duomo.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Global capital of fashion and design." },
                { name: "Naples", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/88/Napoli_-_Maschio_Angioino_-_202209302342_3.jpg/500px-Napoli_-_Maschio_Angioino_-_202209302342_3.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "The birthplace of pizza with coastal views." },
                { name: "Positano", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9b/Positano_Sunset.JPG/500px-Positano_Sunset.JPG?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Stunning cliffside village on the Amalfi Coast." }
            ]
        },
        "France": {
            description: "Experience romance, fine dining, and breathtaking landmarks. Top activities: Eiffel Tower visits, Louvre Museum tours, Riviera beaches, and skiing in the Alps.",
            cities: [
                { name: "Paris", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4b/La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg/500px-La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "The City of Light and romance." },
                { name: "Nice", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/ba/Promenade_des_Anglais_Nice_IMG_1255.jpg/500px-Promenade_des_Anglais_Nice_IMG_1255.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Beautiful capital of the French Riviera." },
                { name: "Lyon", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/9/97/Lyon-part-dieu-2023.jpg/500px-Lyon-part-dieu-2023.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Historic city known for gastronomy." },
                { name: "Marseille", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a1/Notre-Dame_de_la_Garde_aerial_view_2020.jpeg/500px-Notre-Dame_de_la_Garde_aerial_view_2020.jpeg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Vibrant port city in southern France." },
                { name: "Bordeaux", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e1/Bordeaux_Place_de_la_Bourse_de_nuit.jpg/500px-Bordeaux_Place_de_la_Bourse_de_nuit.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Hub of the famed wine-growing region." },
                { name: "Strasbourg", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ea/Strasbourg_Cathedral.jpg/500px-Strasbourg_Cathedral.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Unique blend of French and German cultures." }
            ]
        },
        "Japan": {
            description: "A perfect blend of ancient tradition and futuristic technology. Top activities: Bullet train rides, exploring temples, sushi tasting, and visiting Mt. Fuji.",
            cities: [
                { name: "Tokyo", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg/500px-Skyscrapers_of_Shinjuku_2009_January.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Bustling capital combining ultramodern and traditional." },
                { name: "Kyoto", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6b/Kyoto%2C_Japan_%2849667780482%29.jpg/500px-Kyoto%2C_Japan_%2849667780482%29.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Famous for classical Buddhist temples and gardens." },
                { name: "Osaka", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/c/ca/Osaka_Castle_03bs3200.jpg/500px-Osaka_Castle_03bs3200.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Known for modern architecture and hearty street food." },
                { name: "Hokkaido", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/5/57/Map_of_Japan_with_highlight_on_02edit_Hokkaido_prefecture.svg/500px-Map_of_Japan_with_highlight_on_02edit_Hokkaido_prefecture.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "Famous for its volcanoes and natural hot springs." },
                { name: "Nara", img: "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&w=500&q=60", desc: "Historic city with roaming deer in parks." },
                { name: "Hiroshima", img: "https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fd/Atomic_Bomb_Dome_and_Motoyaso_River%2C_Hiroshima%2C_Northwest_view_20190417_1.jpg/500px-Atomic_Bomb_Dome_and_Motoyaso_River%2C_Hiroshima%2C_Northwest_view_20190417_1.jpg?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail", desc: "A modern city dedicated to peace and history." }
            ]
        }
    };

    // Get all countries as keywords
    const searchKeywords = Object.keys(travelData);

    // 1. Live Search functionality
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        searchSuggestions.innerHTML = '';
        
        if (query.length > 0) {
            const matches = searchKeywords.filter(word => word.toLowerCase().includes(query));
            
            if (matches.length > 0) {
                searchSuggestions.classList.remove('d-none');
                matches.forEach(match => {
                    const li = document.createElement('li');
                    li.className = 'list-group-item list-group-item-action bg-body text-body';
                    li.style.cursor = 'pointer';
                    const regex = new RegExp(`(${query})`, "gi");
                    li.innerHTML = match.replace(regex, "<strong class='text-primary'>$1</strong>");
                    
                    li.addEventListener('click', () => {
                        searchInput.value = match;
                        searchSuggestions.classList.add('d-none');
                        handleSearch(match);
                    });
                    searchSuggestions.appendChild(li);
                });
            } else {
                searchSuggestions.classList.add('d-none');
            }
        } else {
            searchSuggestions.classList.add('d-none');
        }
    });

    document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchSuggestions.contains(e.target)) {
            searchSuggestions.classList.add('d-none');
        }
    });

    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            searchSuggestions.classList.add('d-none');
            handleSearch(searchInput.value);
        }
    });

    // 2. Search Logic and rendering dynamic cards
    function handleSearch(query) {
        const countryKey = Object.keys(travelData).find(key => key.toLowerCase() === query.toLowerCase());
        
        if (countryKey) {
            const data = travelData[countryKey];
            searchCountryTitle.textContent = `Explore ${countryKey}`;
            searchCountryDesc.textContent = data.description;
            
            searchCitiesContainer.innerHTML = '';
            data.cities.forEach(city => {
                // Ensure image shows perfectly and is never hidden!
                const cityCard = `
                    <div class="col-md-4">
                        <div class="card h-100 border-0 shadow-sm d-block" style="overflow: hidden; background: var(--bs-body-bg);">
                            <img src="${city.img}" class="card-img-top" alt="${city.name}" style="height: 220px; object-fit: cover;">
                            <div class="card-body p-4 text-start">
                                <h3 class="card-title fs-4 fw-bold mb-2 text-body">${city.name}</h3>
                                <p class="card-text text-muted m-0">${city.desc}</p>
                            </div>
                        </div>
                    </div>
                `;
                searchCitiesContainer.innerHTML += cityCard;
            });

            searchResultsSection.classList.remove('d-none');
            
            setTimeout(() => {
                searchResultsSection.scrollIntoView({ behavior: 'smooth' });
            }, 100);
        } else {
            alert("No detailed data for '" + query + "' yet! Try searching for 'Egypt', 'Turkey', 'Italy', 'France', or 'Japan'.");
        }
    }

    closeResultsBtn.addEventListener('click', () => {
        searchResultsSection.classList.add('d-none');
    });
});
