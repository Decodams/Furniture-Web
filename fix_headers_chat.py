
import os
import re

standard_logo_nav = """            <div class="logo-container">
                <a class="logo-container" href="index.html">
                    <div class="logo-icon">
                        <svg class="text-midnight" fill="none" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"
                            style="color: #020408;">
                            <path d="M6 6H42L36 24L42 42H6L12 24L6 6Z" fill="currentColor"></path>
                        </svg>
                    </div>
                    <h2 class="logo-text">OCHESTRA</h2>
                </a>

                <nav class="nav-menu">
                    <a class="nav-link" href="index.html" id="nav-home">Home</a>
                    <a class="nav-link" href="aboutus.html" id="nav-about">About Us</a>
                    <a class="nav-link" href="services.html" id="nav-services">Service</a>
                    <a class="nav-link" href="collections.html" id="nav-collections">Collection</a>
                    <a class="nav-link" href="contact.html" id="nav-contact">Contact</a>
                </nav>
            </div>"""

standard_chat = """    <!-- Chat Widget -->
    <div class="chat-widget-btn">
        <span class="material-symbols-outlined" style="font-size: 1.5rem;">chat_bubble</span>
    </div>

    <div class="chat-modal-window">
        <div class="chat-header-small">
            <span class="uppercase font-bold text-gold text-xs tracking-widest">Values Concierge</span>
            <span class="material-symbols-outlined text-slate-500 cursor-pointer chat-close">close</span>
        </div>
        <div class="chat-scroll-area">
            <div class="flex flex-col gap-4">
                <div class="message-bubble message-concierge">
                    Welcome to Ochestra. How may we assist you with your collection today?
                </div>
            </div>
        </div>
        <div class="chat-input-area">
            <input type="text" class="chat-input" placeholder="Type a message...">
        </div>
    </div>"""

files = ['index.html', 'aboutus.html', 'services.html', 'product.html', 'contact.html', 'collections.html']

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace logo and nav-menu together if possible
    content = re.sub(r'<div class="logo-container">.*?</div>\s*</nav>\s*</div>', standard_logo_nav, content, flags=re.DOTALL)
    # Sometimes it is structured slightly differently
    content = re.sub(r'<div class="logo-container">.*?<nav class="nav-menu">.*?</nav>\s*</div>', standard_logo_nav, content, flags=re.DOTALL)
    
    # 2. Replace chat widget
    content = re.sub(r'<!-- Chat Widget.*?</div>\s*</div>', standard_chat, content, flags=re.DOTALL)
    
    # 3. Quick check for Portfolio (Extra safety)
    content = re.sub(r'<a class="nav-link" href="js/Admin/portfolio.html".*?</a>', '', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
