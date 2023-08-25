import logging
from abc import ABC

import PySimpleGUI as sg

from simplekeyboard.sounds.sounds import SKSound

logger = logging.getLogger(__name__)


class GuiKeyboardLayoutBuilder(ABC):
    pass


class PySimpleGuiKeyboardLayoutBuilder(GuiKeyboardLayoutBuilder):
    pass


class KeyboardWindow:

    def __init__(self, sounds: dict[str, SKSound]) -> None:
        self.sounds = sounds
        self.layout = [[]]
        for sound in sounds.values():
            self.layout[0].append(sg.Button(sound.name))

    def run(self):
        window = sg.Window('SimpleKeyboard', self.layout) # noqa
        while True:                             # The Event Loop
            event, values = window.read()
            # print(event, values) #debug
            logger.critical(f"EVENT: {event}")
            if event in self.sounds.keys():
                self.sounds[event].play()
            if event in (None, 'Exit', 'Cancel'):
                break

# while True:                             # The Event Loop
#     event, values = window.read()
#     # print(event, values) #debug
#     if event in (None, 'Exit', 'Cancel'):
#         break
