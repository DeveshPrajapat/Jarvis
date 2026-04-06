🎙️ Jarvis Voice Assistant (Python)

A simple voice-controlled desktop assistant built using Python.
It can listen to your voice commands, speak responses, and perform basic tasks like opening websites, searching on Google/YouTube, and playing songs.

🚀 Features

🎤 Speech Recognition (using microphone input)

🔊 Text-to-Speech response

🌐 Open websites like Google and YouTube

🔎 Search anything on Google and YouTube

🎵 Play songs on YouTube automatically

🖱️ Auto-click video play using PyAutoGUI

👋 Exit assistant with voice command ("bye")

🛠️ Technologies Used

Python

speech_recognition

pyttsx3

webbrowser

pyautogui

time

📂 Project Structure
Jarvis-Voice-Assistant/
│── jarvis.py
│── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate it:

👉 On Windows
venv\Scripts\activate
👉 On Mac/Linux
source venv/bin/activate
3️⃣ Install Required Libraries
pip install pyttsx3 SpeechRecognition pyautogui pyaudio

👉 If pyaudio gives error, install using:

pip install pipwin
pipwin install pyaudio
▶️ How to Run
python jarvis.py

Then speak commands like:

"Hi"

"Open Google"

"Search on Google Python tutorials"

"Open YouTube"

"Play song Believer"

"Bye"

🧠 Example Commands
Command	Action
Hi	                        | Greets you
Open                        | Google	Opens Google homepage
Search on Google AI tools	  | Searches topic on Google
Open YouTube	              | Opens YouTube
Search on YouTube songs	    | Searches videos
Play song shape of you      |	Plays song on YouTube
Bye	Stops assistant
⚠️ Notes

Make sure your microphone is working properly

Speak clearly for better recognition

Internet connection is required for speech recognition and browsing

🔮 Future Improvements

Add weather updates

Add system control (shutdown, restart)

Add WhatsApp/email sending

GUI version using Tkinter

AI chatbot integration

⭐ Support

If you like this project, give it a ⭐ on GitHub!
