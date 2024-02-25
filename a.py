import os, time
from flask import Flask
from pywebostv.discovery import * 
from pywebostv.connection import *
from pywebostv.controls import *
from threading import Thread, Event
ev = Event()

store = {'client_key': '490331cd44c8820b19dd17bdebb924ba'}

client = WebOSClient("192.168.1.67")
client.connect()

media = MediaControl(client)
system = SystemControl(client)
app = ApplicationControl(client)
inp = InputControl(client)

for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("LG: Примите соединение на подключение")
    elif status == WebOSClient.REGISTERED:
        print("LG: Регистрация была завершена")

def rec():
  ev.wait()
  # Записывание микрофона в аудиофайл (audio.wav) (5 с)
  os.system('termux-microphone-record -f audio.wav -l 5')
  time.sleep(5.5)

  os.system('curl -X POST -F "file=@audio.wav" http://192.168.1.65:8080')
  os.system('rm audio.wav')
  rec()

def flask():
  ev.wait()
  app = Flask(__name__)

  @app.route('/volume_up')
  def volume_up():
    return media.volume_up()

  @app.route('/volume_down')
  def volume_down():
    return media.volume_down()
  
  app.run(port=8080, host='192.168.1.64')

th1 = Thread(target=rec)
th2 = Thread(target=flask)
th1.start()
th2.start()
ev.set()
