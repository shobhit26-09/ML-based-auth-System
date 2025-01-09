import sounddevice as sd
import librosa
import numpy as np

DURATION = 5
FS = 44100

def record_audio(duration=DURATION, fs=FS):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    print("Recording complete")
    return np.squeeze(audio)

def augment_audio(audio, sr=FS):
    audio_pitch_shifted = librosa.effects.pitch_shift(audio, sr=sr, n_steps=2)
    audio_time_stretched = librosa.effects.time_stretch(audio, rate=1.2)
    noise = np.random.randn(len(audio))
    audio_noisy = audio + 0.005 * noise
    return [audio, audio_pitch_shifted, audio_time_stretched, audio_noisy]
