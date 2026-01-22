document.addEventListener('DOMContentLoaded', () => {
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
            // Optional: Toggle icon
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
            const icon = chatBtn.querySelector('.material-symbols-outlined');
            icon.textContent = 'chat_bubble';
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
                // In a real app, you'd fetch data here. 
                // For now, we simulate by just showing the modal.
                productModal.classList.add('active');
            });
        });

        if (modalClose) {
            modalClose.addEventListener('click', () => {
                productModal.classList.remove('active');
            });
        }

        // Close on background click
        if (modalOverlay) {
            modalOverlay.addEventListener('click', (e) => {
                if (e.target === modalOverlay) {
                    productModal.classList.remove('active');
                }
            });
        }
    }
});
