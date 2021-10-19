from functools import wraps, total_ordering
from math import log2
from numbers import Integral
import re

@total_ordering
class Pitch:
    # class attribute
    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self, spn_str):
        spn_str = spn_str.upper()
        if not spn_str[-1].isdigit():
            raise ValueError
        self.octave = int(spn_str[-1])
        self.semitone = Pitch.keys.index(spn_str[0:-1])

    def __add__(self, other):
        if isinstance(other, int):
            octave = int((self.octave * 12 + self.semitone + other) / 12)
            semitone = (self.octave * 12 + self.semitone + other) % 12
            spn_str = Pitch.keys[semitone] + str(octave)
            return Pitch(spn_str)
        else:
            raise TypeError(NotImplemented)

    def __iadd__(self, other):
        if isinstance(other, int):
            octave = int((self.octave * 12 + self.semitone + other) / 12)
            semitone = (self.octave * 12 + self.semitone + other) % 12
            self.octave = octave
            self.semitone = semitone
            return self
        else:
            raise TypeError(NotImplemented)

    def __sub__(self, other):
        if isinstance(other, int):
            octave = int((self.octave * 12 + self.semitone - other) / 12)
            semitone = (self.octave * 12 + self.semitone - other) % 12
            spn_str = Pitch.keys[semitone] + str(octave)
            return Pitch(spn_str)
        elif isinstance(other, Pitch):
            semitones = int((self.octave * 12 + self.semitone) - (other.octave * 12 + other.semitone))
            return semitones
        else:
            raise TypeError(NotImplemented)

    def __isub__(self, other):
        if isinstance(other, int):
            octave = int((self.octave * 12 + self.semitone - other) / 12)
            semitone = (self.octave * 12 + self.semitone - other) % 12
            self.octave = octave
            self.semitone = semitone
            return self
        else:
            raise TypeError(NotImplemented)

    def __eq__(self, other):
        return Pitch.frequency(self) == Pitch.frequency(other)

    def __lt__(self, other):
        return Pitch.frequency(self) < Pitch.frequency(other)

    def __repr__(self):
        spn_str = Pitch.keys[self.semitone] + str(self.octave)
        return spn_str

    def frequency(self):
        semitones = self - Pitch('A4')
        frequency = 440 * pow(2, (semitones) / 12)
        return frequency

    @classmethod
    def from_frequency(cls, frequency):
        p = Pitch('A4') + round(12 * log2(frequency / 440))
        return p

#1h