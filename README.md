# Darwix_AI_Assignment

This repository contains two Django-based features developed as part of the **Darwix AI Assignment**.  
Each feature is implemented independently with its own entry point and Django setup.

---

## 📦 Installation

Ensure you have **Python 3.10** installed on your system.

### 1. Clone the Repository

git clone https://github.com/tejatanush/Darwix_AI_assignment.git
cd Darwix_AI


### 2. Install Dependencies

pip install -r requirements.txt

---

##  Running the Django Features

Both features are standalone Django apps with independent `main.py` files to run servers.

---

### ▶️ Feature 1: Audio Transcription with Speaker Diarization

To run the transcription service:

python Feature1/main.py runserver

**API Endpoint:**

- URL: http://127.0.0.1:8000/transcribe/?audio_file  
- Method: POST  
- Description: Upload an audio file in .wav format using the `audio_file` form field (e.g., via Postman)

---

### ▶️ Feature 2: Title Suggestions using NLP

To run the title suggestion service:

python Feature2/main.py runserver

**API Endpoint:**

- URL: http://127.0.0.1:8000/suggest-titles/  
- Method: POST  
- Description: Submit textual content in the body to get title suggestions generated using NLP models.

---

---

## ✨ Author

**Tanush Teja** – AI/ML Developer  
Seeking to integrate AI into real-world systems.
