import board
import digitalio
import time
import checkpoint

# Benchmark pins
pin_start = digitalio.DigitalInOut(board.D4)
pin_start.pull = digitalio.Pull.DOWN

pin_done = digitalio.DigitalInOut(board.D5)
pin_done.direction = digitalio.Direction.OUTPUT
pin_done.value = False

def bitcount(x):
    m4 = 0x1 | (0x1<<8) | (0x1<<16) | (0x1<<24)
    m1 = 0xFF
    s4 = (x&m4) + ((x>>1)&m4) + ((x>>2)&m4) + ((x>>3)&m4) + ((x>>4)&m4) + ((x>>5)&m4) + ((x>>6)&m4) + ((x>>7)&m4)
    s1 = (s4&m1) + ((s4>>8)&m1) + ((s4>>16)&m1) + ((s4>>24)&m1)
    return s1

num = 2147483647
reult = 0;

####
#### Benchmark start
####

# Uncomment for the trigger benchmark
checkpoint.set_schedule(1)

checkpoint.disable()

restore_count_start = checkpoint.restore_count()
checkpoint_count_start = checkpoint.checkpoint_count()

# Uncomment when using a logic analyzer, comment out if using Teensy power toggler
#pin_done.value = True

while pin_start.value != True:
    pass

# Start signal
pin_done.value = False

checkpoint.enable()

for i in range(0,30000):
    result = bitcount(num)

# The benchmark is done, set the done signal
pin_done.value = True

# Print some info
checkpoint_count = checkpoint.checkpoint_count() - checkpoint_count_start
restore_count = checkpoint.restore_count() - restore_count_start

while True:
    print('Checkpoint count:', checkpoint_count)
    print('Restore count:', restore_count)
    print(str(checkpoint_count) + ', ' + str(restore_count))
    time.sleep(1)
