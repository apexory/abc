import os, time, threading
import speech_recognition as sr

recognizer = sr.Recognizer()

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def rec():
  # Записывание микрофона в аудиофайл (audio.wav) (5 с)
  os.system('termux-microphone-record -f audio.wav -l 5')
  time.sleep(5)

  with sr.AudioFile("audio.wav") as source:
    audio_data = recognizer.record(source)
      
  try:
    text = recognizer.recognize_google(audio_data, language="ru-RU")
    if "привет" in text:
    	print('шо')
  except sr.UnknownValueError:
    print("Не удалось распознать речь")
  except sr.RequestError as e:
    print("Ошибка сервиса распознавания: {0}".format(e))

setInterval(rec, 5)
