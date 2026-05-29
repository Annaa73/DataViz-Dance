# Dance Origins of the World 🌍💃

An interactive 3D globe visualization exploring the origins of 141 dance styles across history and cultures.

---

## Prerequisites

Before running the project, make sure you have the following installed:

- [Visual Studio Code](https://code.visualstudio.com/)
- **Live Server** extension for VS Code
  - Open VS Code → go to the **Extensions** tab (or press `Ctrl+Shift+X`)
  - Search for **"Live Server"** by Ritwick Dey
  - Click **Install**

---

## Getting Started

1. **Clone the repository**
```bash
   git clone https://github.com/Annaa73/DataViz-Dance.git
```

2. **Open the project folder in VS Code**
```bash
   cd DataViz-Dance
   code .
```

3. **Launch the visualization**
   - In the VS Code file explorer, find `dance-origins-globe.html`
   - Right-click on the file
   - Select **"Open with Live Server"**
   - The visualization will open automatically in your browser

> **Note:** The globe relies on external 3D libraries and data files, so it must be served through Live Server — simply double-clicking the HTML file will not work correctly.

---

## How to Use

### Search & Filter (left sidebar)
- Use the **search bar** on the left to look up dance styles by name or origin
- For example, typing `pol` will surface results like **Pole Dance**, **Polonaise** and **Mazurka**
- Use the **category filter buttons** below the search bar to narrow results by dance type

### Exploring the Globe
- **Click and move** to rotate the globe
- **Scroll** to zoom in and out
- Each colored dot represents a dance style, positioned at its country of origin
- **Click any dot** to open the detail panel for that dance

### Dance Detail Panel (right sidebar)
Clicking a dot or a dance name in the list opens a side panel showing:
- Country and era of origin
- Cultural significance
- Notable characteristics
- Formation, tempo, difficulty, and age group
- Instruments, notable practitioners, and health benefits
- Initial descriptive visualizations
- A link to the **main Tableau dashboard** with extended visualizations

###  Timeline Playback
- At the bottom of the page there is a **timeline bar** spanning from **1000 BC to 2013**
- Press the **▶ Play button** to animate the timeline — dots will appear on the globe as you travel through history, showing when each dance style emerged
- You can also **drag the slider** manually to jump to any point in time

---

## Project Structure

```
DataViz-Dance/
├── dance-origins-globe.html   # Main application file
├── data/
│   └── dances.js              # Dataset of 141 dance styles
└── README.md
```
---

## Team

| Member                | ITU email   |
| --------------------- | ----------- |
| Marta Zuzanna Richert | mazr@itu.dk |
| Anna Weronika Lekston | awle@itu.dk |

---

## Data

The dataset covers **141 dance styles** from across the world, ranging from ancient ceremonial dances to modern street dance, spanning over 3000 years of human movement and culture.

---

## Built With

- [Three.js](https://threejs.org/) — 3D globe rendering
- [Tableau Embedding API](https://help.tableau.com/current/api/embedding_api/en-us/index.html) — dashboard visualizations
- Vanilla JavaScript, HTML & CSS
- Tableau Public for creating visualizations