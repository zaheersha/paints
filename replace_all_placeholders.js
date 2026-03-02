import fs from 'fs';
import path from 'path';

const htmlDir = 'client';

function updateFile(filepath) {
    let content = fs.readFileSync(filepath, 'utf8');

    // Replace <span class="product-img-placeholder">[ text ]</span>
    content = content.replace(/<span class="product-img-placeholder">\[.*?\]<\/span>/g, '<img src="/images/interior_hero_3.jpg" alt="Product Image" style="width:100%;height:100%;object-fit:cover;">');
    
    // Replace <div class="related-card-image" ...>[ text ]</div>
    content = content.replace(/(<div class="related-card-image"[^>]*>)\[.*?\](<\/div>)/g, '$1<img src="/images/texture_1.jpg" style="width:100%;height:100%;object-fit:cover;">$2');

    // Also the map placeholder
    content = content.replace('<span class="map-label">[ Google Map Embed — Dealer Locations ]</span>', '<img src="/images/distribution_1.jpg" style="width:100%;height:100%;object-fit:cover; position:absolute; top:0; left:0; z-index:0; opacity: 0.5;">');

    fs.writeFileSync(filepath, content, 'utf8');
}

fs.readdirSync(htmlDir).forEach(filename => {
    if (filename.endsWith('.html')) {
        updateFile(path.join(htmlDir, filename));
    }
});
