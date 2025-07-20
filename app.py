import os
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, render_template, jsonify
import pyttsx3
import time
import random
import json

app = Flask(__name__)

print("Loading model and data...")
model = joblib.load('eeg_model.joblib')
label_encoder = joblib.load('label_encoder.joblib')
df = pd.read_csv('eeg_dummy_dataset.csv')
intents = df['intent'].unique().tolist()
feature_columns = df.drop('intent', axis=1).columns
print("Model and data loaded successfully.")

HF_API_TOKEN = "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"
MODEL_URL = "https://api-inference.huggingface.co/models/google/gemma-2b-it"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

SPEECHIFY_API_KEY = "gywkoRQPF6u2cUrSrJ4rOtPD5gLZrfSaPEH3U91LMmg="
SPEECHIFY_CLONE_URL = "https://api.speechify.com/v1/voice/clone"

def clone_voice_with_speechify(text, voice_sample_url):
    payload = {
        "text": text,
        "voice_sample_url": voice_sample_url
    }
    headers = {
        "Authorization": f"Bearer {SPEECHIFY_API_KEY}"
    }
    try:
        print("Demonstrating voice cloning API call (not active).")
        return None
    except Exception as e:
        print(f"Voice cloning API call failed: {e}")
        return None


GENAI_SENTENCE_CACHE = {
    "thirsty, water": [
        "I'm feeling very thirsty, could I please get some water?",
        "Could you please give me a glass of water?",
        "My throat is getting dry, I think I need some water."
    ],
    "yes, pain": [
        "Yes, it's hurting a little bit.",
        "I am feeling some pain, yes.",
        "Yes, there is definitely some discomfort."
    ],
    "no, pain": [
        "No, I'm not feeling any pain right now.",
        "I'm feeling alright, there's no pain.",
        "No, it's not hurting."
    ],
    "urgent, washroom": [
        "I need to use the washroom, it's quite urgent.",
        "Could you please help me to the toilet? It's an emergency.",
        "I need to go to the washroom. "
    ],
    "hungry, food": [
        "I'm starting to feel hungry, is it time to eat soon?",
        "Could I please have some food? I'm feeling quite hungry.",
        "I think I'm ready for my meal now."
    ],
    "tired, rest": [
        "I feel very tired, I think I need to rest for a bit.",
        "I'm feeling quite exhausted, could I lie down and rest?",
        "I think it's time for me to take a nap."
    ]
}

def get_genai_sentence(intent):
    lookup_key = intent.lower()
    if lookup_key in GENAI_SENTENCE_CACHE:
        return random.choice(GENAI_SENTENCE_CACHE[lookup_key])
    else:
        return f"The decoded intent is: {intent}"

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id) 

        engine.setProperty('rate', 150)
        speech_file = f"static/output_{int(time.time())}.mp3"
        engine.save_to_file(text, speech_file)
        engine.runAndWait()
        return f"/static/{speech_file}"
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html', intents=intents)

@app.route('/generate_eeg', methods=['POST'])
def generate_eeg():
    try:
        data = request.get_json()
        selected_intent = data['intent']
        
        eeg_features_row = df[df['intent'] == selected_intent].iloc[0]
        features_list = eeg_features_row[feature_columns].tolist()

        return jsonify({
            'success': True,
            'eeg_features': features_list
        })
    except Exception as e:
        print(f"An error occurred in /generate_eeg: {e}")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/decode_process', methods=['POST'])
def decode_process():
    try:
        data = request.get_json()
        eeg_features = json.loads(data['eeg_features'])
        features_for_prediction = pd.DataFrame([eeg_features], columns=feature_columns)
        predicted_label_encoded = model.predict(features_for_prediction)[0]
        decoded_intent = label_encoder.inverse_transform([predicted_label_encoded])[0]

        generated_sentence = get_genai_sentence(decoded_intent)
        audio_path = text_to_speech(generated_sentence)

        return jsonify({
            'success': True,
            'decoded_intent': decoded_intent,
            'generated_sentence': generated_sentence,
            'audio_path': audio_path
        })
    except Exception as e:
        print(f"An error occurred in /decode_process: {e}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
