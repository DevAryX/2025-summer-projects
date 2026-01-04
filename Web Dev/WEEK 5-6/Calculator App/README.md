# SmartCalc – Scientific Calculator Web App

**SmartCalc** is a modern, animated calculator web app with built-in scientific functions, history tracking, dark mode toggle, and offline support via PWA. Designed for responsiveness and ease of use, it’s optimized for both desktop and mobile use.

## Features

- 🔢 **Basic + Scientific Modes** – Toggle advanced scientific buttons (%, (), sqrt, etc.)
- 🌙 **Dark Mode** – Theme switch with saved preference using localStorage
- 🧠 **Smart History** – Auto-tracks up to 50 past calculations with scrollable view
- ⌨️ **Keyboard Support** – Type full expressions directly and hit Enter
- 📱 **PWA Enabled** – Installable on mobile and desktop for offline access
- ⚡ **Smooth UI** – CSS transitions, button glow effects, and grid layout

## 📁 Folder Structure

```
smartcalc/
├── index.html            # Main calculator interface (assumed present)
├── style.css             # Responsive and themed UI styles
├── script.js             # Calculator logic and interactivity
├── manifest.json         # PWA support and app metadata
├── icon-192.png          # App icon for mobile (192x192)
├── icon-512.png          # App icon for splash screens (512x512)
└── README.md             # Project documentation
```

## 🔧 How to Use

1. Clone or download the repository.
2. Open `index.html` in any browser.
3. Use the mouse or keyboard to enter calculations.
4. Click `Toggle Mode` to switch between dark/light themes.
5. Press `Toggle Sci` to reveal/hide scientific functions.
6. Access from your home screen if installed as a PWA.

## 💻 Technologies Used

- **HTML5 / CSS3 / JavaScript**
- **Math.js** (required separately via CDN or script tag)
- **LocalStorage** – for dark mode and history persistence
- **PWA Manifest** – allows installation on supported devices

## 📦 PWA Manifest

The app includes a `manifest.json` file:

```json
{
  "name": "SmartCalc",
  "short_name": "Calculator",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "#121212",
  "theme_color": "#0077b6",
  "icons": [
    { "src": "icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
```

To complete PWA functionality, consider adding:

- A `service-worker.js` file (for offline caching)
- HTTPS hosting (e.g. GitHub Pages or Netlify)

## ✨ Future Improvements

- Add unit conversions (kg to lbs, cm to inches, etc.)
- Graphing functionality with chart libraries
- Voice input using Web Speech API
- Full offline service worker cache
- Accessibility (ARIA labels, screen reader support)

## 👤 Author

**Arham Hamid**  
Location: Larbert, Scotland  
Email: [arhm@gmail.com](mailto:arhm@gmail.com)

---

> “Discipline. Dua. Delivery.”
