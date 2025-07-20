# Vaani - Brain-Computer Interface (BCI)
Vaani (from Sanskrit: voice) is an MVP concept for a Brain-Computer Interface designed to give a voice to individuals with severe motor disabilities like ALS and Locked-in Syndrome. This project demonstrates a complete pipeline from thought to speech, simulating how EEG signals can be decoded into intents and then vocalized using modern technology.

This project was built for the ***"Building for Bharat with the Power of GenAI"*** theme, showcasing how advanced technology can be adapted to meet diverse needs.

## How It Works
The application demonstrates a two-step process:

**Intent Simulation:** The user selects a basic human intent (e.g., "Thirsty, Water"). The application's backend then simulates the corresponding EEG feature data that a real BCI device would capture.

**Decoding & Vocalization:** The backend takes the simulated EEG data, decodes it back into the original intent using a machine learning model, and uses a generative AI model (simulated via a local cache) to convert the simple intent into a natural, human-like sentence. This sentence and a generated audio file are then sent back to the frontend to be displayed and played.

## Tech Stack
**Backend:** Python, Flask

**Machine Learning:** Pandas, Scikit-learn, Joblib

**Frontend:** HTML5, CSS3, JavaScript

**Text-to-Speech:** pyttsx3

## How to Run Locally
This project runs as a dynamic web application using a Python Flask server.

### Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### Set up a Virtual Environment:
It is highly recommended to use a virtual environment to manage project dependencies.

### Create the virtual environment
python -m venv venv

### Activate it (on Windows)
.\venv\Scripts\activate

### Activate it (on macOS/Linux)
source venv/bin/activate

**Install Dependencies:**
Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

**Run the Flask Application:**
Once the dependencies are installed, you can start the web server.

python app.py

**Open in Browser:**
Open your web browser and navigate to the following address:
http://127.0.0.1:5000

The application should now be running locally on your machine.
