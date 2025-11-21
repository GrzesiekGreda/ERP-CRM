// Animacja logo przy załadowaniu strony
document.addEventListener('DOMContentLoaded', function() {
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