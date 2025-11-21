// Generowanie realistycznego tła kosmicznego 3D
function createStarsBackground() {
    const starsContainer = document.getElementById('starsBackground');
    
    // Tworzenie gwiazd 3D lecących do przodu
    for (let i = 0; i < 300; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        
        // Pozycjonowanie w kole wokół centrum (perspektywa tunelu)
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.random() * 400 + 100;
        const x = Math.cos(angle) * radius + window.innerWidth / 2;
        const y = Math.sin(angle) * radius + window.innerHeight / 2;
        
        star.style.left = x + 'px';
        star.style.top = y + 'px';
        
        // Różne rozmiary gwiazd
        const size = Math.random() * 3 + 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        
        // Różne prędkości
        const duration = Math.random() * 3 + 2;
        star.style.animationDuration = duration + 's';
        star.style.animationDelay = Math.random() * 3 + 's';
        
        starsContainer.appendChild(star);
    }
    
    // Tworzenie tunelu warp speed
    for (let i = 0; i < 12; i++) {
        const tunnelLine = document.createElement('div');
        tunnelLine.className = 'warp-tunnel';
        
        const angle = (i / 12) * Math.PI * 2;
        const radius = 300;
        const x = Math.cos(angle) * radius + window.innerWidth / 2;
        const y = Math.sin(angle) * radius + window.innerHeight / 2;
        
        tunnelLine.style.left = x + 'px';
        tunnelLine.style.top = '0px';
        tunnelLine.style.transformOrigin = `0 ${window.innerHeight / 2}px`;
        tunnelLine.style.transform = `rotateZ(${angle}rad)`;
        
        const duration = Math.random() * 2 + 3;
        tunnelLine.style.animationDuration = duration + 's';
        tunnelLine.style.animationDelay = Math.random() * 2 + 's';
        
        starsContainer.appendChild(tunnelLine);
    }
    
    // Tworzenie mgławic w tle
    for (let i = 0; i < 8; i++) {
        const nebula = document.createElement('div');
        nebula.className = 'nebula';
        
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.random() * 600 + 200;
        const x = Math.cos(angle) * radius + window.innerWidth / 2;
        const y = Math.sin(angle) * radius + window.innerHeight / 2;
        
        nebula.style.left = x + 'px';
        nebula.style.top = y + 'px';
        
        const size = Math.random() * 150 + 100;
        nebula.style.width = size + 'px';
        nebula.style.height = size + 'px';
        
        const duration = Math.random() * 10 + 10;
        nebula.style.animationDuration = duration + 's';
        nebula.style.animationDelay = Math.random() * 5 + 's';
        
        starsContainer.appendChild(nebula);
    }
}

// Animacja logo przy załadowaniu strony
document.addEventListener('DOMContentLoaded', function() {
    // Inicjalizacja tła kosmicznego
    createStarsBackground();
    
    const logo = document.querySelector('.logo');
    const companyName = document.querySelector('.company-name');
    const heroContent = document.querySelector('.hero-content');
    const serviceCards = document.querySelectorAll('.service-card');
    
    // Animacja wejścia logo
    setTimeout(() => {
        logo.style.opacity = '0';
        logo.style.transform = 'scale(0.8)';
        logo.style.transition = 'all 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55)';
        
        setTimeout(() => {
            logo.style.opacity = '1';
            logo.style.transform = 'scale(1)';
        }, 100);
    }, 200);
    
    // Animacja tekstu
    setTimeout(() => {
        heroContent.style.opacity = '0';
        heroContent.style.transform = 'translateY(30px)';
        heroContent.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            heroContent.style.opacity = '1';
            heroContent.style.transform = 'translateY(0)';
        }, 100);
    }, 800);
    
    // Animacja kart usług
    serviceCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            card.style.transition = 'all 0.6s ease';
            
            setTimeout(() => {
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, 100);
        }, 1200 + (index * 200));
    });
    
    // Efekt świecenia logo przy hover
    const logoContainer = document.querySelector('.logo-container');
    
    logoContainer.addEventListener('mouseenter', function() {
        logo.style.boxShadow = `
            0 0 30px rgba(220, 38, 38, 0.8),
            0 0 60px rgba(220, 38, 38, 0.6),
            0 0 90px rgba(220, 38, 38, 0.4),
            inset 0 0 30px rgba(220, 38, 38, 0.2)
        `;
    });
    
    logoContainer.addEventListener('mouseleave', function() {
        logo.style.boxShadow = `
            0 0 20px rgba(220, 38, 38, 0.5),
            0 0 40px rgba(220, 38, 38, 0.3),
            inset 0 0 20px rgba(220, 38, 38, 0.1)
        `;
    });
    
    // Płynne przewijanie do sekcji
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Animacja przy scrollu
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);
    
    // Obserwuj wszystkie elementy do animacji
    const animatedElements = document.querySelectorAll('.service-card, .hero-content');
    animatedElements.forEach(el => observer.observe(el));
});

// Funkcja do dynamicznej zmiany koloru akcentu (dla przyszłego użytku)
function changeAccentColor(color) {
    const root = document.documentElement;
    root.style.setProperty('--accent-color', color);
}

// Konsola powitalna
console.log(`
🏢 Witamy na stronie firmy GREDA!
🚀 Strona została załadowana pomyślnie.
💡 Gotowi do rozwoju biznesu? Skontaktuj się z nami!
`);