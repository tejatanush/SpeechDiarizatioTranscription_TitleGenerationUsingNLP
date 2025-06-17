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
- Description: Upload an audio file in .wav format using the `audio_file` form field and click send button. Now after some time around 2 to 3 minutes you will get the json format of speaker,start,end and transcription. (e.g., via Postman)
- Example Input: Just use the audio_file.wav in  Feature1 folder. Please upload the file in value column and make key name as audio_file. 
- Example Output:
  ```json
  [
  {
    "speaker": "SPEAKER_00",
    "text": "transcription...",
    "start": 0.0,
    "end": 5.0
  },
  ]
---

### ▶️ Feature 2: Title Suggestions using NLP

To run the title suggestion service:

python Feature2/main.py runserver

**API Endpoint:**

- URL: http://127.0.0.1:8000/suggest-titles/  
- Method: POST  
- Description: Submit textual content in the body to get title suggestions generated using NLP models.
- Example Input:
  ```json
  {
  "blog_content": "Artificial Intelligence is transforming the healthcare industry by enabling faster diagnosis, improving patient outcomes, and reducing the burden on medical professionals. AI-driven tools can analyze medical images, predict disease risk, and assist doctors in making more informed decisions."}

- Example Output:
```json
{
    "titles": [
        "Revolutionizing Healthcare: How AI is Transforming Patient Care",
        "The Future of Medicine: Unlocking the Power of Artificial Intelligence",
        "Healing with Code: The Impact of AI on Healthcare and Beyond"]}

