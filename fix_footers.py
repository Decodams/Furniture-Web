
import os

footer_content = """<footer>
            <div class=\"container\">
                <div class=\"grid grid-cols-4 gap-16 flex-col-mobile\">
                    <div>
                        <a class=\"flex items-center gap-2\" href=\"index.html\">
                            <div class=\"logo-icon\" style=\"width: 1.5rem; height: 1.5rem; padding: 0.25rem;\">
                                <svg class=\"text-midnight\" fill=\"none\" viewBox=\"0 0 48 48\"
                                    xmlns=\"http://www.w3.org/2000/svg\" style=\"color: #020408;\">
                                    <path d=\"M6 6H42L36 24L42 42H6L12 24L6 6Z\" fill=\"currentColor\"></path>
                                </svg>
                            </div>
                            <h2 class=\"font-serif\" style=\"font-size: 1.25rem;\">OCHESTRA</h2>
                        </a>
                        <p style=\"margin-top: 2rem; font-size: 0.75rem; color: var(--color-slate-500);\">
                            Preserving the sanctity of the handmade in an age of mass production. Each Ochestra piece is
                            signed by the master artisan who crafted it.
                        </p>
                        <div class=\"social-links\">
                            <a href=\"#\" class=\"social-link\" aria-label=\"Instagram\">
                                <svg viewBox=\"0 0 24 24\">
                                    <path
                                        d=\"M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z\" />
                                </svg>
                            </a>
                            <a href=\"#\" class=\"social-link\" aria-label=\"Facebook\">
                                <svg viewBox=\"0 0 24 24\">
                                    <path
                                        d=\"M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z\" />
                                </svg>
                            </a>
                            <a href=\"#\" class=\"social-link\" aria-label=\"LinkedIn\">
                                <svg viewBox=\"0 0 24 24\">
                                    <path
                                        d=\"M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z\" />
                                </svg>
                            </a>
                        </div>
                    </div>

                    <div>
                        <h5>Archives</h5>
                        <ul>
                            <li><a href=\"collections.html\">The Walnut Series</a></li>
                            <li><a href=\"collections.html\">Gold Collection</a></li>
                            <li><a href=\"collections.html\">Heritage Restored</a></li>
                            <li><a href=\"collections.html\">Atelier Lighting</a></li>
                        </ul>
                    </div>

                    <div>
                        <h5>Maison</h5>
                        <ul>
                            <li><a href=\"aboutus.html\">The Workshop</a></li>
                            <li><a href=\"aboutus.html\">Artisans</a></li>
                            <li><a href=\"aboutus.html\">Sustainability</a></li>
                            <li><a href=\"services.html\">Private Viewing</a></li>
                        </ul>
                    </div>

                    <div>
                        <h5>Newsletter</h5>
                        <p style=\"margin-bottom: 1.5rem; font-size: 0.75rem; color: var(--color-slate-500);\">
                            Receive private collection releases and invitations to studio events.
                        </p>
                        <form
                            style=\"display: flex; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 0.5rem;\">
                            <input type=\"email\" placeholder=\"Email Address\"
                                style=\"background: transparent; border: none; color: white; flex: 1; font-size: 0.75rem;\">
                            <button class=\"uppercase text-gold\"
                                style=\"font-size: 0.625rem; letter-spacing: 0.1em; font-weight: 700;\">Join</button>
                        </form>
                    </div>
                </div>

                <div class=\"text-center\"
                    style=\"margin-top: 6rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 2.5rem;\">
                    <p class=\"uppercase\"
                        style=\"font-size: 0.56rem; letter-spacing: 0.4em; color: var(--color-slate-700);\">© 2024
                        Ochestra Luxury Atelier. Excellence as a Legacy.</p>
                </div>
            </div>
        </footer>"""

files = ['aboutus.html', 'services.html', 'product.html', 'contact.html', 'collections.html']
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    import re
    new_content = re.sub(r'<footer>.*?</footer>', footer_content, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
