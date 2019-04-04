
import speech_recognition as sr
#import googlemaps
from datetime import datetime
sr.__version__
r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')#audio file storted in harvard.wav
with harvard as source:
     r.adjust_for_ambient_noise(source)
     audio = r.record(source)
type(audio)
print("Content of audio file is :",r.recognize_houndify(audio,client_id="LsU9cd4-ZJc43qhrrGjVyA==",client_key="ulOt3jAEFhqNQ2ltkNWEPMMK0LtTpF92LtLMsNTCfhsrDTv-aGr9PS1ZmcGs3xILEhL57uzOxmlbnr9sJCmPjQ=="))
