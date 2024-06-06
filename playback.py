import numpy as np
import pygame
import random
import queue
import time

from music21 import note

class Playback:
    def __init__(self, bpm=100):
        pygame.mixer.init(frequency=44100, size=-16, channels=2)

        self.bpm = bpm
        self.pause_duration = 0.25 * (60 / bpm)

    def play(self, song_data):
        processed_song = self.process_song(song_data)

        for i in range(len(song_data)):
            for instr in processed_song:
                if instr[i] is not None:
                    self.play_sound(instr[i])

            time.sleep(self.pause_duration)

    def process_song(self, song_data):
        processed_song = []

        COLS_PER_CHANNEL = 2
        NUM_COLS = len(song_data[0])
        NUM_CHANNELS = int(NUM_COLS / COLS_PER_CHANNEL)

        for col in range(0, NUM_COLS, int(NUM_COLS / NUM_CHANNELS)):
            channel_data = np.array(song_data)
            channel_data = channel_data[:, col:col+2]

            processed_song.append(self.process_channel(channel_data))

        return processed_song

    def process_channel(self, channel_data):
        prev_note = None
        prev_note_idx = 0
        duration = 0
        notes = np.full(len(channel_data), None)

        for row in range(len(channel_data)):
            curr_note = channel_data[row][0]

            if curr_note is not None:
                if prev_note is not None:
                    # Complete the previous note
                    freq = self.note_freq(prev_note)
                    wave = self.generate_square_wave(freq, duration * self.pause_duration)
                    notes[prev_note_idx] = wave
                
                # Start a new note
                prev_note = curr_note
                prev_note_idx = row
                duration = 1
            else:
                # Continue the previous note
                duration += 1

        # Handle the last note
        if prev_note is not None:
            freq = self.note_freq(prev_note)
            wave = self.generate_square_wave(freq, duration * self.pause_duration)
            notes[prev_note_idx] = wave

        return notes

    def play_sound(self, waveform, volume=0.5):
        sound = pygame.sndarray.make_sound(waveform)
        sound.play()

    def generate_square_wave(self, freq, duration, sample_rate=44100):
        num_samples = int(sample_rate * duration)
        t = np.linspace(0, duration, num_samples, endpoint=False)
        wave = np.sign(np.sin(2 * np.pi * freq * t))

        # Create an attack envelope
        attack_time = 0.1
        attack_samples = int(sample_rate * attack_time)
        envelope = np.ones(num_samples)
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

        # Apply the envelope to the wave
        wave *= envelope

        # Convert to stereo
        stereo_wave = np.zeros((num_samples, 2), dtype=np.int16)

        MAX_16_BIT = np.iinfo(np.int16).max

        stereo_wave[:, 0] = wave * MAX_16_BIT  # Left channel
        stereo_wave[:, 1] = wave * MAX_16_BIT  # Right channel

        return stereo_wave

    def note_freq(self, note_name):
        return note.Note(note_name).pitch.frequency