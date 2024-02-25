import os, time

# Записывание микрофона в аудиофайл (audio.wav) (5 с)
os.system('termux-microphone-record -f audio.wav -l 5')
time.sleep(6)

print('Готово!')
os.system('ls')
