import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.5)

def setBrightness(n):
    dot[0] = [(n+1) * a for a in [63,0,0]]

import netdemo
print("test small model")
netdemo.runDemo(file='netdemo/models/sine-16-16.py', onchange=setBrightness, runonce=True)
print("test three layer model")
netdemo.runDemo(file='netdemo/models/sine-16-16-16.py', onchange=setBrightness, runonce=True)
print("test medium model")
netdemo.runDemo(file='netdemo/models/sine-32-32.py', onchange=setBrightness, runonce=True)
print("test large model")
netdemo.runDemo(file='netdemo/models/sine-64-32.py', onchange=setBrightness, runonce=True)
print("test larger model")
#netdemo.runDemo(file='netdemo/models/sine-64-64.py', onchange=setBrightness, runonce=True)