#!/usr/bin/python3
import logging
import os

from pynput import keyboard

from simplekeyboard.sounds.sounds import MusicNote, SKSound
from simplekeyboard.gui.gui import KeyboardWindow
# from simplekeyboard.config.config import BITRATE

logging.basicConfig(
    # filename='app.log',
    # filemode='w',
    format='%(asctime)s %(name)s [%(levelname)s]: %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S',
    encoding='utf-8',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


def main():
    logger.debug("Running sound keyboard")


sounds: dict[str, SKSound] = {}


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == 'a':
            sounds['A4'].play()
        if key.char == 's':
            sounds['B4'].play()
        if key.char == 'd':
            sounds['C5'].play()
        if key.char == 'f':
            sounds['D5'].play()
        if key.char == 'g':
            sounds['E5'].play()
        if key.char == 'h':
            sounds['F5'].play()
        if key.char == 'j':
            sounds['G5'].play()
        if key.char == 'k':
            sounds['A5'].play()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def test_main():
    logger.debug("Running test sound keyboard")
    for note in MusicNote:
        sounds[note.name] = (SKSound(
            note,
            44100,
            amplitude=0.3,
            duration=0.1,
            name=note.name))
    logger.debug("Running test gui")
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        kwindow = KeyboardWindow(sounds).run()
        listener.join()


main = test_main # noqa

if __name__ == '__main__':
    main()
