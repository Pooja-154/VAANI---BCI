# test_gemini.py
import google.generativeai as genai
import os

# --- IMPORTANT ---
# Paste your new API key here
API_KEY = "AIzaSyBri505Q09fS_kEnxgLuXmxxiLyZvJehZo"
# -----------------

print("Attempting to configure Gemini API...")

try:
    genai.configure(api_key=API_KEY)
    
    print("✅ Configuration successful!")
    
    print("\nAttempting to create a model instance...")
    model = genai.GenerativeModel('gemini-pro')
    
    print("✅ Model instance created successfully!")
    
    print("\nAttempting to generate content...")
    response = model.generate_content("Hello, world.")
    
    print("✅ Content generated successfully!")
    print("\n--- TEST PASSED ---")
    print("Response from Gemini:", response.text)
    
except Exception as e:
    print("\n--- ❌ TEST FAILED ---")
    print("An error occurred. This means the issue is with your API key or Google Cloud project setup.")
    print("\nError details:", e)