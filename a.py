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
  # Записывание микрофона в аудиофайл (audio.wav) (0 с)
  os.system('termux-microphone-record -f audio.wav -l 0')
  time.sleep(2)
  os.system('termux-microphone-record -q')

  os.system('curl -X POST -F "file=@audio.wav" http://192.168.1.65:8080')
  os.system('rm audio.wav')
  rec()

def flask():
  ev.wait()
  app = Flask(__name__)

  @app.route('/volume_up')
  def volume_up():
    print('Действие: volume_up')
    media.volume_up()
    return 'ok'

  @app.route('/volume_down')
  def volume_down():
    print('Действие: volume_down')
    media.volume_down()
    return 'ok'

  @app.route('/volume_get')
  def volume_get():
    print('Действие: volume_get')
    volume = media.get_volume()['volume']
    os.system(f'termux-tts-speak Громкость: {volume}')
    return 'ok'

  @app.route('/pause')
  def pause():
    print('Действие: pause')
    media.pause()
    return 'ok'

  @app.route('/resume')
  def resume():
    print('Действие: resume')
    media.play()
    return 'ok'
  
  app.run(port=8080, host='192.168.1.64')

th1 = Thread(target=rec)
th2 = Thread(target=flask)
th1.start()
th2.start()
ev.set()
