# SpeechRecognition
Speech Recognition on edge using CMU Sphinx and on cloud using Google Cloud Speech API

Here is the code for Speech Recognition using Sphinx and Google Cloud Speech API with input from micorphone. it's needed a microphone to provide audio input to the program. 

# Environment/ Install packages
- Install Python 2.7.14, https://www.python.org/downloads/
- PyAdudio package,  `$ pip install pyaudio`
- Pocketsphinx package, `$ pip install pocketsphinx`  
- Speech recognition, `$ pip install SpeechRecognition`
- Install Google Speech API client, `$ pip install --upgrade google-cloud-speech`
- Authenticating to the Cloud Speech API, `$ export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_KEY_FILE`, https://cloud.google.com/speech/docs/auth#using_a_service_account

# Note
Replace PATH_TO_KEY_FILE with the path to your JSON service account file. GOOGLE_APPLICATION_CREDENTIALS should be written out as-is (it's not a placeholder in the example above).
If Speech Recognition package fails, try `$ sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev` and `$ sudo apt-get install libpulse-dev`

# Usage
Run following code in the terminal,

`speech_recognition_sphinx_gcp.py`

