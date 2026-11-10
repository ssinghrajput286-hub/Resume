// Copies fonts + PDF libraries from node_modules into www/ so the app works fully offline.
const fs = require('fs');
const path = require('path');

const fams = {
  'outfit': 'Outfit',
  'poppins': 'Poppins',
  'montserrat': 'Montserrat',
  'lora': 'Lora',
  'playfair-display': 'Playfair Display',
  'dm-serif-display': 'DM Serif Display',
  'bebas-neue': 'Bebas Neue',
  'space-grotesk': 'Space Grotesk',
  'jetbrains-mono': 'JetBrains Mono',
};
const weights = [300, 400, 500, 600, 700, 800];

fs.mkdirSync('www/fonts', { recursive: true });
fs.mkdirSync('www/lib', { recursive: true });

let css = '';
let n = 0;
for (const [pkg, fam] of Object.entries(fams)) {
  for (const w of weights) {
    const file = `${pkg}-latin-${w}-normal.woff2`;
    const src = path.join('node_modules', '@fontsource', pkg, 'files', file);
    if (fs.existsSync(src)) {
      fs.copyFileSync(src, path.join('www/fonts', file));
      css += `@font-face{font-family:'${fam}';font-style:normal;font-weight:${w};font-display:block;src:url(${file}) format('woff2')}\n`;
      n++;
    }
  }
}
fs.writeFileSync('www/fonts/fonts.css', css);
console.log(`fonts: ${n} files`);

fs.copyFileSync('node_modules/html2canvas/dist/html2canvas.min.js', 'www/lib/html2canvas.min.js');
fs.copyFileSync('node_modules/jspdf/dist/jspdf.umd.min.js', 'www/lib/jspdf.umd.min.js');
console.log('libs copied');
