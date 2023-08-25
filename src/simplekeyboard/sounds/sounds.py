from enum import Enum
from functools import cached_property
import logging

import numpy as np
import sounddevice as sd

logger = logging.getLogger(__name__)


class MusicNote(Enum):
    A4 = 440
    A4_sharp = 466
    B4 = 494
    C5 = 523
    C5_sharp = 554
    D5 = 587
    D5_sharp = 622
    E5 = 659
    F5 = 698
    F5_sharp = 740
    G5 = 784
    G5_sharp = 830
    A5 = 880


class Scale:
    pass


class SKSound:
    def __init__(self,
                 note: MusicNote,
                 bitrate: int,
                 amplitude: float = 1,
                 duration: float = 1.0):
        self.note = note
        self.bitrate = bitrate
        self.amplitude = amplitude
        self.duration = duration

    def play(self) -> None:
        logger.warning(f"Sound {self.note} is played")
        logger.warning(f"Sound frequency {self.note.value}")
        sd.play(self._sound_data)
        sd.wait()

    @cached_property
    def _sound_data(self):
        t = np.arange(self.duration * self.bitrate) / self.bitrate
        sound_data = self.amplitude * np.cos(2 * np.pi * self.note.value * t)
        return sound_data
