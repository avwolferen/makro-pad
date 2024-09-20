print("Starting")

import board
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP20, board.GP19)    # Cols
keyboard.row_pins = (board.GP17, board.GP16)    # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# SHORTCUTS
LOCKMACHINE = KC.LGUI(KC.L)
UNDO = KC.LCTRL(KC.Z)
COPY = KC.LCTRL(KC.C)
PASTE = KC.LCTRL(KC.V)

keyboard.keymap = [
    [LOCKMACHINE, UNDO, COPY, PASTE]
]

if __name__ == '__main__':
    keyboard.go()