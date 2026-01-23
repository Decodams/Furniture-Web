// Video Modal Logic for Collections Page
window.playVideo = function (videoUrl) {
    const modal = document.getElementById('video-modal');
    const player = document.getElementById('gallery-video-player');
    if (modal && player) {
        player.src = videoUrl;
        modal.style.display = 'flex';
        player.play();
    }
}

window.closeVideo = function () {
    const modal = document.getElementById('video-modal');
    const player = document.getElementById('gallery-video-player');
    if (modal && player) {
        modal.style.display = 'none';
        player.pause();
        player.src = '';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Shared Asset Arrays
    const serviceImages = [
        'Image/Bedroom.jpg',
        'Image/Bedroom2.jpg',
        'Image/Children.jpg',
        'Image/Class.jpg',
        'Image/Console.jpg',
        'Image/Dinning.jpg',
        'Image/Frame.jpg',
        'Image/Mattress.jpg',
        'Image/Office.jpg',
        'Image/Outdoor.jpg',
        'Image/Pillow.jpg',
        'Image/Setup.jpg',
        'Image/Shelf.jpg',
        'Image/Tv.jpg'
    ];

    const serviceDescriptionTexts = [
        "Experience the pinnacle of artisanal mastery with our dedicated team of craftsmen, bringing centuries of tradition to modern living.",
        "Our approach combines sustainable materials with visionary design, ensuring every piece reflects your unique lifestyle and legacy.",
        "Where meticulous attention to detail meets the soul of raw timber. We don't just create furniture; we craft stories in wood.",
        "Transforming spatial concepts into architectural realities. Our commitment to excellence is reflected in every joint and finish.",
        "A legacy of luxury, hand-finished with 24k gold leaf and curated for the most discerning collectors of fine furniture."
    ];

    // Active Nav Indicator
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href) {
            const linkPath = href.split('/').pop();
            if (linkPath === currentPath) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        }
    });

    // Mobile Menu Logic
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            const icon = mobileToggle.querySelector('.material-symbols-outlined');
            if (icon) {
                if (navMenu.classList.contains('active')) {
                    icon.textContent = 'close';
                } else {
                    icon.textContent = 'menu';
                }
            }
        });
    }

    // Chat Widget Logic
    const chatBtn = document.querySelector('.chat-widget-btn');
    const chatWindow = document.querySelector('.chat-modal-window');
    const chatClose = document.querySelector('.chat-close');

    if (chatBtn && chatWindow) {
        chatBtn.addEventListener('click', () => {
            chatWindow.classList.toggle('active');
            const icon = chatBtn.querySelector('.material-symbols-outlined');
            if (chatWindow.classList.contains('active')) {
                icon.textContent = 'expand_more';
            } else {
                icon.textContent = 'chat_bubble';
            }
        });
    }

    if (chatClose) {
        chatClose.addEventListener('click', () => {
            chatWindow.classList.remove('active');
            if (chatBtn) {
                const icon = chatBtn.querySelector('.material-symbols-outlined');
                if (icon) icon.textContent = 'chat_bubble';
            }
        });
    }

    // Quick View Modal Logic
    const productModal = document.getElementById('product-modal');
    const quickViewButtons = document.querySelectorAll('.quick-view-btn');
    const modalClose = document.querySelector('.modal-close');
    const modalOverlay = document.querySelector('.modal-overlay');

    if (productModal && quickViewButtons) {
        quickViewButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                productModal.classList.add('active');
            });
        });

        if (modalClose) {
            modalClose.addEventListener('click', () => {
                productModal.classList.remove('active');
            });
        }

        if (modalOverlay) {
            modalOverlay.addEventListener('click', (e) => {
                if (e.target === modalOverlay) {
                    productModal.classList.remove('active');
                }
            });
        }
    }

    // Gallery Logic (Filters, Search)
    const galleryGrid = document.getElementById('gallery-grid');
    const filterButtons = document.querySelectorAll('.filter-btn');
    const clearFiltersBtn = document.getElementById('clear-filters');
    const gallerySearch = document.getElementById('gallery-search');

    if (galleryGrid) {
        // Filter Functionality
        function filterGallery(category) {
            const items = galleryGrid.querySelectorAll('.masonry-item');
            items.forEach(item => {
                const itemCat = item.getAttribute('data-category');
                if (category === 'all' || itemCat === category) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
        }

        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                filterGallery(btn.getAttribute('data-filter'));
            });
        });

        // Clear Selections
        if (clearFiltersBtn) {
            clearFiltersBtn.addEventListener('click', () => {
                filterButtons.forEach(b => b.classList.remove('active'));
                const allBtn = document.querySelector('.filter-btn[data-filter="all"]');
                if (allBtn) allBtn.classList.add('active');
                filterGallery('all');
                if (gallerySearch) gallerySearch.value = '';
                const items = galleryGrid.querySelectorAll('.masonry-item');
                items.forEach(item => {
                    item.classList.remove('hidden');
                });
            });
        }

        // Search Functionality
        const globalSearch = document.querySelector('.search-input');
        const searchInput = gallerySearch || globalSearch;

        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                const query = e.target.value.toLowerCase();
                const items = galleryGrid.querySelectorAll('.masonry-item');
                items.forEach(item => {
                    const titleElement = item.querySelector('h3');
                    const title = titleElement ? titleElement.textContent.toLowerCase() : '';
                    const cat = item.getAttribute('data-category') ? item.getAttribute('data-category').toLowerCase() : '';
                    if (title.includes(query) || cat.includes(query)) {
                        item.classList.remove('hidden');
                    } else {
                        item.classList.add('hidden');
                    }
                });
            });
        }
    }

    // Video Slider Logic
    const sliderWrapper = document.getElementById('video-grid');
    const prevBtn = document.getElementById('slider-prev');
    const nextBtn = document.getElementById('slider-next');

    if (sliderWrapper && prevBtn && nextBtn) {
        const cardWidth = () => {
            const card = sliderWrapper.querySelector('.video-card');
            return card ? card.offsetWidth + parseFloat(getComputedStyle(sliderWrapper).gap) : 0;
        };

        const updateControls = () => {
            const maxScroll = sliderWrapper.scrollWidth - sliderWrapper.clientWidth;
            prevBtn.disabled = sliderWrapper.scrollLeft <= 0;
            nextBtn.disabled = sliderWrapper.scrollLeft >= maxScroll - 5;
        };

        nextBtn.addEventListener('click', () => {
            sliderWrapper.scrollBy({ left: cardWidth(), behavior: 'smooth' });
            setTimeout(updateControls, 500);
        });

        prevBtn.addEventListener('click', () => {
            sliderWrapper.scrollBy({ left: -cardWidth(), behavior: 'smooth' });
            setTimeout(updateControls, 500);
        });

        sliderWrapper.addEventListener('scroll', updateControls);
        window.addEventListener('resize', updateControls);
        setTimeout(updateControls, 500);
    }

    // Service Page Tab Logic
    const serviceBtns = document.querySelectorAll('.service-nav-btn');
    const serviceSections = document.querySelectorAll('.service-section');

    if (serviceBtns.length > 0 && serviceSections.length > 0) {
        serviceBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.getAttribute('data-service');

                // Update buttons
                serviceBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // Show target section, hide others
                serviceSections.forEach(section => {
                    if (section.id === `service-${target}`) {
                        section.classList.remove('hidden');

                        // Pick random image and text
                        const randomImg = serviceImages[Math.floor(Math.random() * serviceImages.length)];
                        const randomText = serviceDescriptionTexts[Math.floor(Math.random() * serviceDescriptionTexts.length)];

                        const img = section.querySelector('img');
                        if (img) {
                            img.src = randomImg;
                            img.style.filter = 'none'; // Remove grayscale for more impact
                        }

                        const p = section.querySelector('p');
                        if (p) {
                            p.textContent = randomText;
                        }
                    } else {
                        section.classList.add('hidden');
                    }
                });
            });
        });
    }

    // Product Pagination Logic
    const productGrid = document.getElementById('product-grid');
    const paginationContainer = document.getElementById('product-pagination');
    const itemsPerPage = 9;
    let currentPage = 1;

    if (productGrid && paginationContainer) {
        const products = Array.from(productGrid.children);
        const totalPages = Math.ceil(products.length / itemsPerPage);

        function showPage(page) {
            currentPage = page;
            const start = (page - 1) * itemsPerPage;
            const end = start + itemsPerPage;

            products.forEach((product, index) => {
                if (index >= start && index < end) {
                    product.classList.remove('hidden');
                } else {
                    product.classList.add('hidden');
                }
            });

            updatePaginationUI();
        }

        function updatePaginationUI() {
            const numbersContainer = document.getElementById('page-numbers');
            const prevBtn = document.getElementById('prev-page');
            const nextBtn = document.getElementById('next-page');

            if (numbersContainer) {
                numbersContainer.innerHTML = '';
                for (let i = 1; i <= totalPages; i++) {
                    const btn = document.createElement('button');
                    btn.className = `page-num ${i === currentPage ? 'active' : ''}`;
                    btn.textContent = i;
                    btn.addEventListener('click', () => showPage(i));
                    numbersContainer.appendChild(btn);
                }
            }

            if (prevBtn) prevBtn.disabled = currentPage === 1;
            if (nextBtn) nextBtn.disabled = currentPage === totalPages;
        }

        const prevBtn = document.getElementById('prev-page');
        const nextBtn = document.getElementById('next-page');

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentPage > 1) showPage(currentPage - 1);
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (currentPage < totalPages) showPage(currentPage + 1);
            });
        }

        // Initialize first page
        if (products.length > 0) {
            showPage(1);
        } else {
            paginationContainer.style.display = 'none';
        }
    }

    // Modal Trigger for all pages
    const quickViewTriggers = document.querySelectorAll('.quick-view-btn, .product-card img');
    quickViewTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            const modal = document.getElementById('product-modal');
            if (modal) {
                modal.classList.add('active');
                // You could dynamically update modal content here if data attributes were present
            }
        });
    });
});
