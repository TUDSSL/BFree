# Run GC and return free memory
def getSpace():
    gc.collect()
    return gc.mem_free()

# Import library and print used memory
import gc
s1 = getSpace()
from netdemo.net import net
s2 = getSpace()
print ("net lib (bytes):", s1 - s2)

# Run the demo
def runDemo(file, onchange=lambda n : None, runonce=False):
    # Load model and print used memory
    s1 = getSpace()
    demoNet = net(file)
    s2 = getSpace()
    print ("net (bytes):", s1 - s2)

    # Loop input from 0 to ~2*pi
    counter = 0
    while True:
        # Run inference
        output = demoNet.infer([counter])[0]
        # Output (input, output) tuple for plotter
        print((counter, output))
        # Run custom onchange function
        onchange(output)

        counter += 0.06283
        if (counter >= 6.2832):
            if (runonce):
                break
            counter = 0
    del demoNet
