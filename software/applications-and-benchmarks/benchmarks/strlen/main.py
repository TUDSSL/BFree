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

def strlen(s):
    i = 0
    while (s[i] != '\0'):
        i = i+1;
    return i

test_str = "These are reserved words in C language. \0"
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

for i in range(0,10000):
    result = strlen(test_str)


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
