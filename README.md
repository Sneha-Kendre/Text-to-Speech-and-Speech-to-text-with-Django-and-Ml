Text to Speech (TTS) and Speech to Text (STT) using Django and Machine Learning
This project showcases how to implement Text to Speech (TTS) and Speech to Text (STT) functionalities using the pyttsx3 library for TTS and speech_recognition for STT. The project is built using Django, which provides a web interface to convert text to speech and recognize speech from audio input.
Features
•	Text to Speech (TTS): Converts user input text into speech using the pyttsx3 library.
•	Speech to Text (STT): Recognizes speech from audio input and converts it to text using the speech_recognition library.
•	User-friendly Web Interface: Built with Django, allowing users to interact with the application via a web browser.
Tech Stack
•	Backend: Django (Python)
•	Libraries:
o	pyttsx3: For text-to-speech conversion.
o	speech_recognition: For speech-to-text conversion.
•	Frontend: HTML, CSS, JavaScript (for the user interface)
Installation
1.	Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/tts-stt-django.git
cd tts-stt-django
2.	Install dependencies:
bash
Copy code
pip install -r requirements.txt
3.	Set up the Django application:
bash
Copy code
python manage.py migrate
python manage.py runserver
Libraries Used
•	pyttsx3: A text-to-speech conversion library in Python that works offline.
•	speech_recognition: A Python library that enables the recognition of spoken words into text.
Usage
1.	Text to Speech: Enter text in the input box and press the "Speak" button to hear the converted speech.
2.	Speech to Text: Upload an audio file or record your voice to convert it into text.
How it Works
•	Text to Speech (TTS): The user enters text in the browser. Upon submitting, the backend uses pyttsx3 to process the text and convert it into audio, which is played for the user.
•	Speech to Text (STT): The user uploads an audio file or speaks directly. The backend uses speech_recognition to transcribe the audio into text and display it in the browser.
Contributing
Feel free to submit pull requests and suggest features!
License
This project is licensed under the MIT License.


