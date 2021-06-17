import gc


# Run GC and return free memory
def get_space():
    gc.collect()
    return gc.mem_free()


# Import library and print used memory
s1 = get_space()
from netdemo.net import Net

s2 = get_space()
print("net lib (bytes):", s1 - s2)


# Run the demo
def run_demo(file, onchange=lambda n: None, runonce=False):
    # Load model and print used memory
    space_before = get_space()
    demo_net = Net(file)
    space_after = get_space()
    print("net (bytes):", space_before - space_after)

    # Loop input from 0 to ~2*pi
    counter = 0
    while True:
        # Run inference
        output = demo_net.infer([counter])[0]
        # Output (input, output) tuple for plotter
        print((counter, output))
        # Run custom onchange function
        onchange(output)

        counter += 0.06283
        if counter >= 6.2832:
            if runonce:
                break
            counter = 0
    del demo_net
