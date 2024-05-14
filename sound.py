import numpy as np
import pygame
import random

pygame.mixer.init()

def generate_square_wave(freq, duration, sample_rate=44100):
    num_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    wave = np.sign(np.sin(2 * np.pi * freq * t))
    return wave

def generate_triangle_wave(freq, duration, sample_rate=44100):
    num_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    wave = 2 * np.abs(t * freq - np.floor(t * freq + 0.5))
    wave = 2 * (wave - 0.5)
    return wave

def generate_noise(duration, sample_rate=44100):
    num_samples = int(sample_rate * duration)
    noise = np.random.uniform(low=-1.0, high=1.0, size=num_samples)
    return noise

def play_sound(waveform, volume=0.5):
    sound = pygame.mixer.Sound(waveform.astype(np.float32))
    sound.set_volume(volume)
    sound.play()

if __name__ == "__main__":
    square_wave = generate_square_wave(freq=440, duration=1.0)

    c = generate_square_wave(freq=261.63, duration=3.0)
    e = generate_square_wave(freq=329.63, duration=3.0)
    g = generate_square_wave(freq=392.00, duration=3.0)

    play_sound(c)
    play_sound(e)
    play_sound(g)

    # freq = [440, 440, 330, 550, 440, 220, 330]
    # freq2 = [330, 300, 330, 550, 440, 220, 330]

    # melody_duration = 0.2
    # for f in freq:
    #     melody_wave = generate_square_wave(freq=f, duration=melody_duration)
    #     melody_wave2 = generate_square_wave(freq=freq2[0], duration=melody_duration)
        
    #     play_sound(melody_wave, volume=0.5)
    #     play_sound(melody_wave2, volume=0.5)
    #     pygame.time.wait(int(melody_duration * 1000))  # Wait between notes

    while pygame.mixer.get_busy():
        pygame.time.wait(10)

    pygame.quit()
