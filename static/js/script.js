// Smooth scrolling
document.documentElement.style.scrollBehavior = 'smooth';

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme') || 'light-mode';
    const html = document.documentElement;
    
    if (savedTheme === 'dark-mode') {
        html.classList.add('dark-mode');
        updateThemeIcon('light');
    } else {
        html.classList.remove('dark-mode');
        updateThemeIcon('dark');
    }

    // Add animation to cards on scroll
    observeCards();
});

// Theme Toggle
const themeToggle = document.getElementById('theme-toggle');
if (themeToggle) {
    themeToggle.addEventListener('click', function() {
        const html = document.documentElement;
        const isDarkMode = html.classList.toggle('dark-mode');
        
        // Save preference
        const theme = isDarkMode ? 'dark-mode' : 'light-mode';
        localStorage.setItem('theme', theme);
        
        // Update icon
        updateThemeIcon(isDarkMode ? 'light' : 'dark');
    });
}

function updateThemeIcon(theme) {
    const icon = themeToggle.querySelector('i');
    if (theme === 'light') {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    } else {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
    }
}

// Mobile Menu Toggle
const navbarToggle = document.getElementById('navbar-toggle');
const navbarMenu = document.getElementById('navbar-menu');

if (navbarToggle) {
    navbarToggle.addEventListener('click', function(e) {
        e.stopPropagation();
        navbarMenu.classList.toggle('active');
    });
}

// Close menu when a link is clicked
const navbarLinks = document.querySelectorAll('.navbar-menu li a');
navbarLinks.forEach(link => {
    link.addEventListener('click', function() {
        navbarMenu.classList.remove('active');
    });
});

// Close menu when clicking outside
document.addEventListener('click', function(event) {
    if (!event.target.closest('.navbar-container')) {
        navbarMenu.classList.remove('active');
    }
});

// Observe cards for animation
function observeCards() {
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = 'fadeInUp 0.6s ease forwards';
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        });

        document.querySelectorAll('.card').forEach(card => {
            observer.observe(card);
        });
    }
}

// Add fade-in animation style dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .card {
        opacity: 0;
    }
`;
document.head.appendChild(style);
