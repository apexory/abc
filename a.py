import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, 
				        channels=1, 
				        rate=16000, 
				        input=True, 
				        frames_per_buffer=8192)
stream.start_stream()

def listenAudio():
	while True:
		data = stream.read(4096)
		yield data

for text in listenAudio():
  print(text)
