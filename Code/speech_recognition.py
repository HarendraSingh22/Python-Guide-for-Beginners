import speech_recognition as sr #install SpeechRecognition


r = sr.Recognizer() #recognising
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

#printing output
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
