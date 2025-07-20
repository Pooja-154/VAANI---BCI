# Vaani - Brain-Computer Interface (BCI)
Vaani (from Sanskrit: voice) is an MVP concept for a Brain-Computer Interface designed to give a voice to individuals with severe motor disabilities like ALS and Locked-in Syndrome. This project demonstrates a complete pipeline from thought to speech, simulating how EEG signals can be decoded into intents and then vocalized using modern technology.

This project was built for the ***"Building for Bharat with the Power of GenAI"*** theme, showcasing how advanced technology can be adapted to meet diverse needs.

## How It Works
The application demonstrates a two-step process:

**Intent Simulation**: The user selects a basic human intent (e.g., "Thirsty, Water"). The application then simulates the corresponding EEG feature data that a real BCI device would capture.

**Decoding & Vocalization**: The application takes the simulated EEG data, decodes it back into the original intent, and uses a generative AI model (simulated via a local cache) to convert the simple intent into a natural, human-like sentence. This sentence is then spoken aloud using the browser's text-to-speech engine.

## Tech Stack
This project uses a combination of technologies to simulate the full BCI pipeline in a web browser:

**Frontend:** HTML5, CSS3, JavaScript (ES6)

**Machine Learning (for development):** Python, Pandas, Scikit-learn

**Web Framework (for development):** Flask

**Deployment:** Render

##How to Run Locally
This project is a static website and can be run directly in your browser without needing a Python server.

1. Clone the repository:

Bash
git clone https://github.com/your-username/your-repo-name.git

2. Navigate to the project directory:
Bash
cd your-repo-name

3. Open index.html:
Simply open the index.html file in your favorite web browser (like Chrome, Firefox, or Edge). You can do this by double-clicking the file in your file explorer.

That's it! The application will run entirely in your browser.
