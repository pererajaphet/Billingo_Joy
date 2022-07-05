#These are function that will modify our audios, thus augment our data to better our speech recognition model 

import numpy as np
import librosa

#This function adds background white noise
def add_white_noise(signal, noise_percentage_factor=0.005):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_percentage_factor
    return augmented_signal

#Speeds up the audio by 1.5
def time_stretch(signal):
    return librosa.effects.time_stretch(signal, rate=1.5)

#Slows the audio by 0.5
def time_cut(signal):
    return librosa.effects.time_stretch(signal, rate=0.5)

#These 3 functions change the pitch of the sound
#PS: when calling these function we should change the argument sr with the sample rate of the audio when reading it
def pitch_scale_1(signal):
    return librosa.effects.pitch_shift(signal, sr=16000, n_steps=4)

def pitch_scale_2(signal):
    return librosa.effects.pitch_shift(signal, sr=16000, n_steps=6)

def pitch_scale_3(signal):
    return librosa.effects.pitch_shift(signal, sr=16000, n_steps=3,bins_per_octave=24)
