import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import spectrogram
import soundfile as sf

file = "FEIN.wav"

form, rate = librosa.load(file, sr = None)

print(f"form is {form}, rate is {rate}")

from IPython.display import Audio

Audio(form, rate=rate)