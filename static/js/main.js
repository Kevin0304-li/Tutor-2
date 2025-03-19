// Main JavaScript file for AI Explainer

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl, {
            html: true
        });
    });
    
    // Handle language toggle in persistent way
    const languageButtons = document.querySelectorAll('.language-toggle .btn, [href*="set_language"]');
    languageButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Store language preference in local storage (optional)
            const language = this.getAttribute('href').includes('english') ? 'english' : 'chinese';
            localStorage.setItem('preferredLanguage', language);
            
            // Add animation when changing language
            document.querySelectorAll('.card, .hero, section').forEach(el => {
                el.classList.add('fade-in');
                setTimeout(() => {
                    el.classList.remove('fade-in');
                }, 500);
            });
        });
    });
    
    // Handle explanation level toggle in persistent way
    const levelButtons = document.querySelectorAll('.level-toggle .btn, [href*="set_level"]');
    levelButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Store level preference in local storage
            const level = this.getAttribute('href').includes('normal') ? 'normal' : 'simple';
            localStorage.setItem('preferredLevel', level);
        });
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if(this.getAttribute('href') !== '#') {
                e.preventDefault();
                
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Animate elements on scroll
    const animateOnScroll = () => {
        const animatableElements = document.querySelectorAll('.card, .feature-card, section');
        
        animatableElements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.2;
            
            if (elementPosition < screenPosition) {
                element.classList.add('animated');
            }
        });
    };
    
    // Call animation function on scroll
    window.addEventListener('scroll', animateOnScroll);
    
    // Call once on page load
    animateOnScroll();
    
    // Add hover effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.2)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });
    
    // Handle like buttons in community page
    const likeButtons = document.querySelectorAll('.like-button');
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.classList.toggle('active');
            
            const postId = this.getAttribute('data-post-id');
            const likeCount = document.querySelector(`.badge[data-post-id="${postId}"]`);
            
            if (likeCount) {
                let count = parseInt(likeCount.textContent);
                
                if (this.classList.contains('active')) {
                    count++;
                    this.innerHTML = '<i class="fas fa-heart me-1"></i> Liked';
                } else {
                    count--;
                    this.innerHTML = '<i class="far fa-heart me-1"></i> Like';
                }
                
                likeCount.textContent = count;
                
                // Add animation to the like counter
                likeCount.classList.add('animate__animated', 'animate__heartBeat');
                setTimeout(() => {
                    likeCount.classList.remove('animate__animated', 'animate__heartBeat');
                }, 1000);
            }
        });
    });
    
    // Navbar active state
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentPath === linkPath || (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        }
    });
    
    // Add dark mode toggle (optional)
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (darkModeToggle) {
        const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const storedDarkMode = localStorage.getItem('darkMode');
        
        // Set initial dark mode state
        if (storedDarkMode === 'enabled' || (storedDarkMode === null && prefersDarkMode)) {
            document.body.classList.add('dark-mode');
            darkModeToggle.checked = true;
        }
        
        darkModeToggle.addEventListener('change', function() {
            if (this.checked) {
                document.body.classList.add('dark-mode');
                localStorage.setItem('darkMode', 'enabled');
            } else {
                document.body.classList.remove('dark-mode');
                localStorage.setItem('darkMode', 'disabled');
            }
        });
    }
    
    // Add search functionality (optional)
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const searchResults = document.getElementById('search-results');
            
            if (searchTerm.length > 2) {
                // In a real app, you would make an AJAX call to search the content
                // This is just a placeholder
                searchResults.innerHTML = `<div class="p-3">
                    <p>Search results for "${searchTerm}" would appear here.</p>
                    <div class="list-group">
                        <a href="#" class="list-group-item list-group-item-action">
                            <strong>Machine Learning</strong> - Basic concepts
                        </a>
                        <a href="#" class="list-group-item list-group-item-action">
                            <strong>Neural Networks</strong> - Architecture explained
                        </a>
                    </div>
                </div>`;
                
                searchResults.style.display = 'block';
            } else {
                searchResults.style.display = 'none';
            }
        });
        
        // Close search results when clicking outside
        document.addEventListener('click', function(e) {
            const searchResults = document.getElementById('search-results');
            if (searchResults && !searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                searchResults.style.display = 'none';
            }
        });
    }
    
    // Add scroll-to-top button behavior
    const scrollTopButton = document.getElementById('scroll-top-btn');
    if (scrollTopButton) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                scrollTopButton.classList.add('show');
            } else {
                scrollTopButton.classList.remove('show');
            }
        });
        
        scrollTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // Handle explanation topic switching with animation
    const topicLinks = document.querySelectorAll('.list-group-item-action');
    topicLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.id.startsWith('topic-')) {
                e.preventDefault();
                
                // Remove active class from all links
                topicLinks.forEach(l => l.classList.remove('active'));
                
                // Add active class to clicked link
                this.classList.add('active');
                
                // Get the topic ID
                const topicId = this.id.replace('topic-', '');
                
                // Update content with animation
                const contentDivs = document.querySelectorAll('[id^="content-"]');
                contentDivs.forEach(div => {
                    div.style.display = 'none';
                });
                
                const targetContent = document.getElementById(`content-${topicId}`);
                if (targetContent) {
                    targetContent.style.display = 'block';
                    targetContent.classList.add('slide-in-right');
                    setTimeout(() => {
                        targetContent.classList.remove('slide-in-right');
                    }, 500);
                }
                
                // Update title
                const topicTitle = document.getElementById('topic-title');
                if (topicTitle) {
                    topicTitle.textContent = this.textContent.trim();
                }
            }
        });
    });
}); 