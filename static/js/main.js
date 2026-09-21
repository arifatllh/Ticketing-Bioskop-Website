document.addEventListener('DOMContentLoaded', () => {
    // Sticky Navbar Logic
    const navbar = document.getElementById('navbar');
    const searchInput = document.getElementById('search');
    const navBrand = document.getElementById('nav-brand');
    const navLogin = document.getElementById('nav-login');
    const navUser = document.getElementById('nav-user');
    const navHistory = document.getElementById('nav-history');

    const handleScroll = () => {
        if (window.scrollY > 50) {
            // Scrolled state
            navbar.classList.remove('bg-transparent', 'py-4');
            navbar.classList.add('bg-white/90', 'backdrop-blur-md', 'shadow-sm', 'py-2');
            
            navBrand.classList.remove('text-white');
            navBrand.classList.add('text-cinema-blue-dark');

            if (navLogin) {
                navLogin.classList.remove('text-white', 'hover:text-cinema-yellow');
                navLogin.classList.add('text-gray-700', 'hover:text-cinema-blue');
            }
            if (navUser) {
                navUser.classList.remove('text-white');
                navUser.classList.add('text-gray-700');
            }
            if (navHistory) {
                navHistory.classList.remove('text-white', 'bg-white/20', 'hover:bg-white/30', 'border-white/10');
                navHistory.classList.add('text-cinema-blue', 'bg-blue-50', 'hover:bg-blue-100', 'border-blue-100');
            }

            if (searchInput) {
                searchInput.classList.remove('bg-white/10', 'border-white/20', 'text-white', 'placeholder-gray-300');
                searchInput.classList.add('bg-gray-100', 'border-transparent', 'text-gray-900', 'placeholder-gray-500');
            }

        } else {
            // Top state
            navbar.classList.add('bg-transparent', 'py-4');
            navbar.classList.remove('bg-white/90', 'backdrop-blur-md', 'shadow-sm', 'py-2');
            
            navBrand.classList.add('text-white');
            navBrand.classList.remove('text-cinema-blue-dark');

            if (navLogin) {
                navLogin.classList.add('text-white', 'hover:text-cinema-yellow');
                navLogin.classList.remove('text-gray-700', 'hover:text-cinema-blue');
            }
            if (navUser) {
                navUser.classList.add('text-white');
                navUser.classList.remove('text-gray-700');
            }
            if (navHistory) {
                navHistory.classList.add('text-white', 'bg-white/20', 'hover:bg-white/30', 'border-white/10');
                navHistory.classList.remove('text-cinema-blue', 'bg-blue-50', 'hover:bg-blue-100', 'border-blue-100');
            }

            if (searchInput) {
                searchInput.classList.add('bg-white/10', 'border-white/20', 'text-white', 'placeholder-gray-300');
                searchInput.classList.remove('bg-gray-100', 'border-transparent', 'text-gray-900', 'placeholder-gray-500');
            }
        }
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Init on load

    // Initialize Hero Swiper
    const heroSwiper = new Swiper('.heroSwiper', {
        loop: true,
        effect: 'fade',
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });

    // Initialize Movie Sliders
    const initMovieSlider = (prefix) => {
        new Swiper(`.${prefix}Swiper`, {
            slidesPerView: 'auto',
            spaceBetween: 16,
            freeMode: true,
            navigation: {
                nextEl: `.${prefix}-next`,
                prevEl: `.${prefix}-prev`,
            },
            breakpoints: {
                320: {
                    spaceBetween: 12,
                },
                640: {
                    spaceBetween: 16,
                },
                1024: {
                    spaceBetween: 24,
                }
            }
        });
    };

    initMovieSlider('popular');
    initMovieSlider('indo');
    initMovieSlider('intl');
});
