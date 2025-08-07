# Speech-to-Text Converter
A real-time speech-to-text converter built in Python that captures microphone input and displays transcribed text both on the command line and a simple user interface (UI). Supports live audio translation in English, Hindi, and Telugu.

✨ # Features
🎧 Live transcription from microphone input

💬 Multilingual support – English, Hindi, and Telugu

🖥️ Real-time display on both the command line and graphical UI

⚡ Built with Python’s SpeechRecognition and other lightweight libraries


📁 Project Structure

speech_to_text/
├── speech_text_org.py     # Main executable script
├── requirements.txt       # List of dependencies (optional)
└── README.md              # This file


🔧 Requirements
Python 3.8 or higher
Required packages:

pip install SpeechRecognition pyaudio tkinter

Optional: If you're running into issues with pyaudio, you may need to install portaudio separately:
Windows: Use precompiled .whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
macOS: brew install portaudio


🚀 How to Run
Make sure your microphone is connected and working.

python speech_text_org.py


The program will:
Start listening to your voice
Transcribe speech to text in real-time
Display the output both on the terminal and in a small GUI window

🌍 Language Support
English
Hindi
Telugu

The program auto-detects the language based on system settings or model behavior. You can modify the script to explicitly set the language if needed.

🧠 Tech Stack
SpeechRecognition
pyaudio – for microphone input
tkinter – for simple UI
Google Web Speech API (default recognizer backend)

❗ Notes
Requires an internet connection to use Google’s speech recognition engine.
Accuracy may vary depending on mic quality and background noise.
For Hindi or Telugu transcription, pronunciation clarity is essential.

🛠️ Future Improvements
File-based transcription support (e.g., WAV/MP3)
Output saving to .txt or .json
Option to choose language from the UI
Offline recognition using models like Whisper or Vosk
