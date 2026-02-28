import fs from 'fs';
import path from 'path';

const htmlDir = 'client';
const waNumber = '919494333702';

const imageReplacements = {
    '[ Our Range Built for Every Surface ]': '<img src="/images/interior_hero_1.jpg" alt="Our Range" style="width:100%;height:100%;object-fit:cover;">',
    '[ Distribution Image ]': '<img src="/images/distribution_1.jpg" alt="Distribution" style="width:100%;height:100%;object-fit:cover;">',
    '[ Spaces We\'ve Transformed ]': '<img src="/images/interior_hero_2.jpg" alt="Showcase" style="width:100%;height:100%;object-fit:cover;">',
    '[ Our Story Image ]': '<img src="/images/interior_hero_3.jpg" alt="Our Story" style="width:100%;height:100%;object-fit:cover;">',
    '[ Brand / product / Hyderabad image ]': '<img src="/images/exterior_1.jpg" alt="Hyderabad Branding" style="width:100%;height:100%;object-fit:cover;">',
    '[ Complete the System ]': '<img src="/images/primer_1.jpg" alt="Complete System" style="width:100%;height:100%;object-fit:cover;">',
    '[ Vegam Exterior Emulsion<br>Product Image ]': '<img src="/images/exterior_1.jpg" alt="Vegam Exterior Emulsion" style="width:100%;height:100%;object-fit:cover;">',
    '[ Vegam Enamel Paints<br>Product Image ]': '<img src="/images/texture_1.jpg" alt="Vegam Enamel" style="width:100%;height:100%;object-fit:cover;">'
};

function updateFile(filepath) {
    let content = fs.readFileSync(filepath, 'utf8');

    // Apply specific image replacements
    for (const [placeholder, replacement] of Object.entries(imageReplacements)) {
        if (content.includes(placeholder)) {
            content = content.replaceAll(placeholder, replacement);
        }
    }

    // Animation classes for "every page"
    if (!content.includes('animate-on-scroll')) {
        const animationStyle = `
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
    
    document.querySelectorAll('section, .product-card, .info-card, .hero-content, .brand-card').forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
  });
</script>
`;
        content = content.replace('</head>', animationStyle + '</head>');
    }

    // Request Sample logic
    if (content.includes('Request Sample')) {
        content = content.replace(/<a[^>]*>Request Sample<\/a>/g, (match) => {
            // If it's a link, we change it to a WhatsApp trigger
            const productNameMatch = content.match(/<h1[^>]*>(.*?)<\/h1>/) || content.match(/<h2[^>]*>(.*?)<\/h2>/);
            const productName = productNameMatch ? productNameMatch[1].replace(/<[^>]*>/g, '').trim() : 'a product';
            return `<a href="#" class="btn-sample" onclick="event.preventDefault(); window.open('https://wa.me/${waNumber}?text=' + encodeURIComponent('Hi Vegam Paints, I would like to request a sample for ${productName}. Here are my details:'), '_blank')">Request Sample</a>`;
        });
    }

    // Update form submission to pre-fill details for WhatsApp
    if (filepath.includes('contact.html')) {
        const urlParams = new URLSearchParams(typeof window !== 'undefined' ? window.location.search : '');
        const prefillScript = `
<script>
  window.onload = () => {
    const params = new URLSearchParams(window.location.search);
    const product = params.get('product');
    if (product) {
      const msgArea = document.querySelector('.form-textarea');
      if (msgArea) msgArea.value = 'I am interested in ' + product + '. Please provide more details.';
    }
  };
</script>
`;
        if (!content.includes('window.location.search')) {
            content = content.replace('</body>', prefillScript + '</body>');
        }
    }

    fs.writeFileSync(filepath, content, 'utf8');
}

fs.readdirSync(htmlDir).forEach(filename => {
    if (filename.endsWith('.html')) {
        updateFile(path.join(htmlDir, filename));
    }
});
