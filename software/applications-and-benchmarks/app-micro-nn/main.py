import board
import neopixel
import netdemo

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.5)


def setBrightness(n):
    dot[0] = [(n + 1) * a for a in [63, 0, 0]]


print("test 2*16 layer model")
netdemo.run_demo(file='netdemo/models/sine-16-16.py', onchange=setBrightness, runonce=True)
print("test 3*16 layer model")
netdemo.run_demo(file='netdemo/models/sine-16-16-16.py', onchange=setBrightness, runonce=True)
print("test 2*32 layer model")
netdemo.run_demo(file='netdemo/models/sine-32-32.py', onchange=setBrightness, runonce=True)
print("test 32+64 layer model")
netdemo.run_demo(file='netdemo/models/sine-64-32.py', onchange=setBrightness, runonce=True)
print("test 2*64 layer model (Disabled because of insufficient memory on the Metro M0)")
# netdemo.run_demo(file='netdemo/models/sine-64-64.py', onchange=setBrightness, runonce=True)
