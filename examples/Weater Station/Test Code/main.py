import time

# Setting the counter to 0 will only happen the very first boot
counter = 0

# The battery-free program should continue counting somewhere in the while loop
while True:
    counter += 1
    print('Counter =', counter)
    time.sleep(1)
