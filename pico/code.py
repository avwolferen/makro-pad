print("Starting")

import board
import supervisor
import digitalio
import storage
import usb_cdc
import usb_hid
import random
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP20, board.GP19)    # Cols
keyboard.row_pins = (board.GP17, board.GP16)    # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# SHORTCUTS for regular keys
LOCKMACHINE = KC.LGUI(KC.L)
MUTE_UNMUTE = KC.LCTRL(KC.LSHIFT(KC.M))
VIDEO_ON_OFF = KC.LCTRL(KC.LSHIFT(KC.O))

macros = Macros()

tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)
keyboard.modules.append(macros)

WEBSITE_TAPDANCE = KC.TD(
    # Tap once for random website
    KC.MACRO(
        Press(KC.LGUI),
        Tap(KC.R),
        Release(KC.LGUI),
        Tap(KC.backspace),
        "iexplore https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        Tap(KC.ENTER)
    ),
    # Tap twice for 2 Belgians
    KC.MACRO(
        Press(KC.LGUI),
        Tap(KC.R),
        Release(KC.LGUI),
        Tap(KC.backspace),
        "iexplore https://de2belgen.wordpress.com/",
        Tap(KC.ENTER)
    ),
    # Tap thrice for Bier Bazaar
    KC.MACRO(
        Press(KC.LGUI),
        Tap(KC.R),
        Release(KC.LGUI),
        Tap(KC.backspace),
        "iexplore https://bierbazaar.be/Bier-van-de-week",
        Tap(KC.ENTER)
    ),
    # Tap four times for Update Faker
    KC.MACRO(
        Press(KC.LGUI),
        Tap(KC.R),
        Release(KC.LGUI),
        Tap(KC.backspace),
        "iexplore https://updatefaker.com/windows10/index.html",
        Tap(KC.ENTER),
    ),
)

keyboard.keymap = [
    [MUTE_UNMUTE, VIDEO_ON_OFF, LOCKMACHINE, WEBSITE_TAPDANCE]
]

if __name__ == '__main__':
    keyboard.go()