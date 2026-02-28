import os
import re

html_dir = 'client'
wa_number = '919494333702'

global_elements = """
<style>
  .wa-container { position: fixed; bottom: 20px; left: 20px; z-index: 1000; }
  .wa-float { width: 60px; height: 60px; background: #25D366; color: white; border-radius: 50px; display: flex; align-items: center; justify-content: center; text-decoration: none; transition: transform 0.3s; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); }
  .wa-float:hover { transform: scale(1.1); color: white; }
  .wa-close { background: white; color: black; border-radius: 50%; width: 20px; height: 20px; font-size: 12px; display: flex; align-items: center; justify-content: center; cursor: pointer; border: 1px solid #ccc; position: absolute; top: -5px; right: -5px; z-index: 1001; line-height: 1; padding-bottom: 2px;}
  .scroll-top { position: fixed; bottom: 20px; right: 20px; width: 50px; height: 50px; background: var(--terracotta); color: white; border-radius: 50%; display: none; align-items: center; justify-content: center; font-size: 24px; cursor: pointer; z-index: 1000; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); transition: background 0.3s; }
  .scroll-top:hover { background: var(--terracotta-dark); }
</style>
<div class="wa-container" id="wa-container">
  <div class="wa-close" onclick="document.getElementById('wa-container').style.display='none'">✖</div>
  <a href="https://wa.me/919494333702" class="wa-float" target="_blank" title="Chat with us on WhatsApp">
    <svg style="width:35px;height:35px" viewBox="0 0 24 24"><path fill="currentColor" d="M19.05 4.91A9.816 9.816 0 0 0 12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01zm-7.01 15.24c-1.48 0-2.93-.4-4.2-1.15l-.3-.18l-3.12.82l.83-3.04l-.2-.31a8.264 8.264 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24c2.2 0 4.27.86 5.82 2.42a8.183 8.183 0 0 1 2.41 5.83c.02 4.54-3.68 8.23-8.22 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81c-.23-.08-.39-.12-.56.12c-.17.25-.64.81-.78.97c-.14.17-.29.19-.54.06c-.25-.12-1.05-.39-1.99-1.23c-.74-.66-1.23-1.47-1.38-1.72c-.14-.25-.02-.38.11-.51c.11-.11.25-.29.37-.43s.17-.25.25-.41c.08-.17.04-.31-.02-.43s-.56-1.34-.76-1.84c-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31c-.22.25-.86.85-.86 2.07c0 1.22.89 2.4 1.01 2.56c.12.17 1.75 2.67 4.23 3.74c.59.26 1.05.41 1.41.52c.59.19 1.13.16 1.56.1c.48-.07 1.47-.6 1.67-1.18c.2-.58.2-.1.14-.18c-.06-.09-.23-.15-.48-.28z"/></svg>
  </a>
</div>
<div class="scroll-top" id="scrollTopBtn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">↑</div>
<script>
  window.addEventListener('scroll', function() {
    if (window.scrollY > 300) {
      document.getElementById('scrollTopBtn').style.display = 'flex';
    } else {
      document.getElementById('scrollTopBtn').style.display = 'none';
    }
  });
</script>
"""

# Image replacements mapping
image_replacements = {
    '[ Your Hero Image Here ]': '<img src="/images/interior_hero_1.jpg" alt="Hero Image" style="width:100%;height:100%;object-fit:cover;">',
    '[ Showroom / Experience<br>Centre Photo ]': '<img src="/images/interior_hero_2.jpg" alt="Showroom" style="width:100%;height:100%;object-fit:cover;">',
    '[ Interior Emulsion<br>Product Image ]': '<img src="/images/interior_hero_3.jpg" alt="Interior Emulsion" style="width:100%;height:100%;object-fit:cover;">',
    '[ Exterior Emulsion<br>Product Image ]': '<img src="/images/exterior_1.jpg" alt="Exterior Emulsion" style="width:100%;height:100%;object-fit:cover;">',
    '[ Ceiling White<br>Product Image ]': '<img src="/images/interior_hero_1.jpg" alt="Ceiling White" style="width:100%;height:100%;object-fit:cover;">',
    '[ Interior Primer<br>Product Image ]': '<img src="/images/primer_1.jpg" alt="Interior Primer" style="width:100%;height:100%;object-fit:cover;">',
    '[ Exterior Primer<br>Product Image ]': '<img src="/images/primer_2.jpg" alt="Exterior Primer" style="width:100%;height:100%;object-fit:cover;">',
    '[ Texture Fine<br>Product Image ]': '<img src="/images/texture_1.jpg" alt="Texture Fine" style="width:100%;height:100%;object-fit:cover;">',
    '[ Texture Rustic<br>Product Image ]': '<img src="/images/texture_2.jpg" alt="Texture Rustic" style="width:100%;height:100%;object-fit:cover;">',
    '[ Wallcare Putty<br>Product Image ]': '<img src="/images/primer_1.jpg" alt="Wallcare Putty" style="width:100%;height:100%;object-fit:cover;">',
    '[ Insp 1 ]': '<img src="/images/interior_hero_1.jpg" alt="Inspiration" style="width:100%;height:100%;object-fit:cover;">',
    '[ Insp 2 ]': '<img src="/images/exterior_1.jpg" alt="Inspiration" style="width:100%;height:100%;object-fit:cover;">',
    '[ Insp 3 ]': '<img src="/images/interior_hero_2.jpg" alt="Inspiration" style="width:100%;height:100%;object-fit:cover;">',
    '[ Dist ]': '<img src="/images/distribution_1.jpg" alt="Distribution" style="width:100%;height:100%;object-fit:cover;">',
    '[ Dist Lg ]': '<img src="/images/distribution_2.jpg" alt="Distribution" style="width:100%;height:100%;object-fit:cover;">',
    # products page placeholders (generic replace)
    '<span class="card-image-label">[': '<img src="/images/interior_hero_1.jpg" alt="Product" style="width:100%;height:100%;object-fit:cover; position:absolute; top:0; left:0; z-index:0;"> <span style="display:none" class="card-image-label">[',
}

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add global elements before </body>
    if 'id="wa-container"' not in content:
        content = content.replace('</body>', f'{global_elements}\n</body>')

    # Replace placeholders
    for placeholder, replacement in image_replacements.items():
        if placeholder in content:
            content = content.replace(placeholder, replacement)
    
    # Also replace class bg-interior etc with actual images if needed, but let's just replace the text placeholders
    content = content.replace('<div class="hero-image-placeholder">', '<div class="hero-image-placeholder" style="padding:0;">')
    
    # Products script modifications
    if 'products.html' in filepath:
        # We need to add logic for filtering and whatsapp chat
        # Let's inject a script at the end of the body
        filter_script = """
<script>
  // Products filtering and WhatsApp
  document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.filter-checkbox');
    const cards = document.querySelectorAll('.product-card');
    
    // Add WhatsApp Know More button to all cards
    cards.forEach(card => {
        const nameEl = card.querySelector('.card-name');
        if (nameEl) {
            const prodName = nameEl.innerText.trim();
            const actions = card.querySelector('.card-actions');
            if (actions) {
                // Change Details to Know More with WhatsApp
                const detailsBtn = actions.querySelector('.btn-card-secondary');
                if (detailsBtn) {
                    detailsBtn.innerText = 'Know More';
                    detailsBtn.onclick = (e) => {
                        e.preventDefault();
                        const msg = `Hi Vegam Paints, I want to know more about ${prodName}.`;
                        window.open(`https://wa.me/919494333702?text=${encodeURIComponent(msg)}`, '_blank');
                    };
                }
            }
        }
    });

    checkboxes.forEach(cb => {
        cb.addEventListener('change', () => {
            // Very basic filtering: if any checkbox is checked, we just show/hide cards that match text
            const checkedLabels = Array.from(checkboxes).filter(c => c.checked).map(c => c.nextElementSibling.innerText.trim().toLowerCase());
            
            if (checkedLabels.length === 0) {
                cards.forEach(c => c.style.display = 'block');
                return;
            }

            cards.forEach(c => {
                const text = c.innerText.toLowerCase();
                // Check if card contains at least one of the checked labels
                const matches = checkedLabels.some(label => {
                    // special handling for some categories
                    if (label === 'emulsions' && text.includes('emulsion')) return true;
                    if (label === 'primers' && text.includes('primer')) return true;
                    if (label === 'textured finishes' && text.includes('texture')) return true;
                    if (label === 'wallcare' && text.includes('putty')) return true;
                    return text.includes(label);
                });
                c.style.display = matches ? 'block' : 'none';
            });
        });
    });
    
    const clearBtn = document.querySelector('.clear-filters');
    if (clearBtn) {
        clearBtn.addEventListener('click', () => {
            checkboxes.forEach(cb => cb.checked = false);
            cards.forEach(c => c.style.display = 'block');
        });
    }
  });
</script>
"""
        if '// Products filtering and WhatsApp' not in content:
            content = content.replace('</body>', filter_script + '\n</body>')
    
    # Contact form modifications
    if 'contact.html' in filepath:
        contact_script = """
<script>
  function handleSubmit() {
    const name = document.querySelectorAll('.form-input')[0].value || '';
    const phone = document.querySelectorAll('.form-input')[1].value || '';
    const email = document.querySelectorAll('.form-input')[2].value || '';
    const city = document.querySelectorAll('.form-input')[3].value || '';
    const role = document.querySelectorAll('.form-select')[0].value || '';
    const interest = document.querySelectorAll('.form-select')[1].value || '';
    const msg = document.querySelector('.form-textarea').value || '';
    
    if (!name || !email) {
        alert('Please fill out Name and Email');
        return;
    }
    
    const text = `*New Contact Enquiry*
Name: ${name}
Phone: ${phone}
Email: ${email}
City: ${city}
I am a: ${role}
Enquiring about: ${interest}
Message: ${msg}`;

    window.open(`https://wa.me/919494333702?text=${encodeURIComponent(text)}`, '_blank');
    
    document.getElementById('success-msg').style.display = 'block';
    setTimeout(() => { document.getElementById('success-msg').style.display = 'none'; }, 5000);
  }
</script>
"""
        # remove existing handle submit if any
        if 'function handleSubmit()' not in content:
            content = content.replace('</body>', contact_script + '\n</body>')
            # ensure button has onclick
            if 'onclick="handleSubmit()"' not in content:
                content = content.replace('class="form-submit"', 'class="form-submit" onclick="handleSubmit()"')

    # Index page animations
    if 'index.html' in filepath:
        # User requested animation for 'Vegam Premium section' chart and 'Distribution'
        # Let's add some AOS (animate on scroll) classes or just write simple IntersectionObserver
        animation_css = """
<style>
  .animate-on-scroll { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease-out, transform 0.8s ease-out; }
  .animate-on-scroll.is-visible { opacity: 1; transform: translateY(0); }
  
  .flex-bar-fill { width: 0 !important; transition: width 1.5s ease-out; }
  .flex-bar-fill.is-visible { width: var(--target-width) !important; }
</style>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        }
      });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.animate-on-scroll, .flex-bar-fill').forEach(el => observer.observe(el));
    
    // Set target width for bars
    document.querySelectorAll('.flex-bar-fill').forEach(el => {
        el.style.setProperty('--target-width', el.style.width || '100%');
        el.style.width = '0';
    });
  });
</script>
"""
        if 'animate-on-scroll' not in content:
            content = content.replace('</head>', animation_css + '\n</head>')
            # Add class to relevant sections
            content = content.replace('class="brand-card ', 'class="brand-card animate-on-scroll ')
            content = content.replace('class="dealer-inner"', 'class="dealer-inner animate-on-scroll"')
            content = content.replace('class="insp-grid"', 'class="insp-grid animate-on-scroll"')

    # About page animations
    if 'about.html' in filepath:
        # "in about us 'The Problem We Solved' keep some animagetions for the text and section"
        animation_css = """
<style>
  .animate-on-scroll { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease-out, transform 0.8s ease-out; }
  .animate-on-scroll.is-visible { opacity: 1; transform: translateY(0); }
</style>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        }
      });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.problem-card, .problem-title, .problem-text').forEach(el => observer.observe(el));
    document.querySelectorAll('.problem-card').forEach(el => el.classList.add('animate-on-scroll'));
  });
</script>
"""
        if 'animate-on-scroll' not in content:
            content = content.replace('</head>', animation_css + '\n</head>')


    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        update_file(os.path.join(html_dir, filename))

