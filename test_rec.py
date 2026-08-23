import wave
import sys

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 7
WAVE_OUTPUT_FILENAME = "test_rec.wav"

p = pyaudio.PyAudio()

stream = p.open(channels=CHANNELS, 
                rate=RATE, 
                format=FORMAT, 
                frames_per_buffer=CHUNK, 
                input=True)

print("*** RECORDING ***")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()