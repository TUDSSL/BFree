import math
import gc

from .net import Net


def run_demo(on_change=lambda n: None):
    """
    Runs the provided models, prints 4 sines as fast as possible, with differently sized models.

    Args:
        on_change: Optional; A lambda expression or function that is ran with every new output value.
    """

    print("Simple Neural Network on CircuitPython: Running 2*16 layer model")
    run_file(
        file="lib/neural_net/models/sine-16-16.net", on_change=on_change, run_once=True
    )
    print("Simple Neural Network on CircuitPython: Running 3*16 layer model")
    run_file(
        file="lib/neural_net/models/sine-16-16-16.net", on_change=on_change, run_once=True
    )
    print("Simple Neural Network on CircuitPython: Running 2*32 layer model")
    run_file(
        file="lib/neural_net/models/sine-32-32.net", on_change=on_change, run_once=True
    )
    print("Simple Neural Network on CircuitPython: Running 32+64 layer model")
    run_file(
        file="lib/neural_net/models/sine-64-32.net", on_change=on_change, run_once=True
    )


def run_file(
    file, start=0, end=math.pi * 2, steps=100, on_change=lambda n: None, run_once=False
):
    """
    Runs the given net with inputs from the given start value to the given end value with the given step size
    and print the (input, output) tuples for the Mu plotter.

    Args:
        file: A file containing the neural network in neural_net format.
        start: Optional; The start input of the loop, or 0 if not provided,
               which is the minimum value for which the provided models are trained.
        end: Optional; The end input of the loop, or 2*pi if not provided,
             which is the maximum value for which the provided models are trained.
        steps: Optional; The amount of steps it will loop, default is 100.
        on_change: Optional; A lambda expression or function that is ran with every new output value.
        run_once: Optional; If run_once is True, the demo net will be ran only once from 0 to 2*pi and will then stop.
                  If run_once is False or not set, the input will reset to 0 and keep running.
    """

    # Import neural net
    demo_net = Net(file)

    # Initialize loop variables
    step_size = (end - start) / steps
    counter = start
    while True:
        # Run inference
        output = demo_net.infer([counter])[0]
        # Print (input, output) tuple for the Mu plotter
        print((counter, output))
        # Run custom onchange function
        on_change(output)

        # Update counter
        counter += step_size
        if counter >= end:
            if run_once:
                break
            counter = start
    del demo_net
    # Forcibly collect garbate to free up memory
    gc.collect()
