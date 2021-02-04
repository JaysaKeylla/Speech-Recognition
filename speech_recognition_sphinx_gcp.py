import speech_recognition as sr  
from time import time
  
 # obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as source:  
   print("Please wait. Calibrating microphone...")  
   # listen for 5 seconds and create the ambient noise energy level  
   r.adjust_for_ambient_noise(source, duration=5)  
   print("Say something!")  
   audio = r.listen(source)  

print("")
print("Speech Recognition:")


start_time = time()  
 # recognize speech using Sphinx
try:  
   print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
except sr.UnknownValueError:  
   print("Sphinx could not understand audio")  
except sr.RequestError as e:  
   print("Sphinx error; {0}".format(e))  
end_time = time()
time_taken = end_time - start_time 
print ("Time required for Sphinx analysis: " + str(time_taken) + " sec")
# recognize speech using Google API
start_time = time()
try:
    print("Google Speech Recognition thinks you said '" + r.recognize_google(audio) + "'")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
end_time = time()
time_taken = end_time - start_time
print ("Time required for Google Speech Recognition: " + str(time_taken) + " sec")



