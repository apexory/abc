import os, time
from flask import Flask
from threading import Thread, Event
ev = Event()

def rec():
  ev.wait()
  # Записывание микрофона в аудиофайл (audio.wav) (5 с)
  os.system('termux-microphone-record -f audio.wav -l 5')
  time.sleep(5.5)

  os.system('curl -X POST -F "file=@audio.wav" http://192.168.1.65:8080')
  os.system('rm audio.wav')
  rec()

def flask()
  ev.wait()
  app = Flask(__name__)

  @app.route('/volume_up')
  def volume_up():
    print('громкость повышена')
  
  app.run(port=80)

th1 = Thread(target=rec)
th2 = Thread(target=flask)
th1.start()
th2.start()
ev.set()
