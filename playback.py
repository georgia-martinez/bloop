import numpy as np
import pygame
import random

from music21 import note

class Playback:
    def __init__(self, bpm=100):
        pygame.mixer.init()

        self.bpm = bpm
        self.pause_duration = 0.25 * (60 / bpm)

    def play(self, song_data):
        processed_song = self.process_song(song_data)
        self.play_sound(processed_song[0])

    def process_song(self, song_data):
        prev_note = None
        duration = 1
        notes = []

        for row in range(len(song_data)):
            curr_note = song_data[row][0]

            if row == 0:
                prev_note = curr_note
                continue

            if curr_note is None and row != len(song_data) - 1:
                duration += 1
                continue

            duration += 1

            freq = self.note_freq(prev_note)
            wave = self.generate_square_wave(freq, duration)
            notes.append(wave)
            prev_note = curr_note

        return notes

    def play_sound(self, waveform, volume=0.5):
        sound = pygame.mixer.Sound(waveform.astype(np.float32))
        sound.set_volume(volume)
        sound.play()

    def generate_square_wave(self, freq, duration, sample_rate=44100):
        num_samples = int(sample_rate * duration)
        t = np.linspace(0, duration, num_samples, endpoint=False)
        wave = np.sign(np.sin(2 * np.pi * freq * t))
        return wave

    def note_freq(self, note_name):
        return note.Note(note_name).pitch.frequency
