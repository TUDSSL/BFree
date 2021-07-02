# Copyright (c) 2021 TU Delft Sustainable Systems Laboratory (https://github.com/TUDSSL/BFree/blob/main/LICENSE)

import math
import gc

from .net import Net


def run_demo(on_change=lambda n: None):
    """
    Method to run the four provided sine models in lib/neural_net/models/.

    Args:
        on_change: optional; a lambda expression or function that is ran with every new output value.
    """

    print("Simple Neural Network for CircuitPython: Running 2*16 neurons neural network")
    run_file(
        file="lib/neural_net/models/sine-16-16.net", on_change=on_change, run_once=True
    )
    print("Simple Neural Network for CircuitPython: Running 3*16 neurons neural network")
    run_file(
        file="lib/neural_net/models/sine-16-16-16.net", on_change=on_change, run_once=True
    )
    print("Simple Neural Network for CircuitPython: Running 2*32 neurons neural network")
    run_file(
        file="lib/neural_net/models/sine-32-32.net", on_change=on_change, run_once=True
    )
    print("Simple Neural Network for CircuitPython: Running 32+64 neurons neural network")
    run_file(
        file="lib/neural_net/models/sine-64-32.net", on_change=on_change, run_once=True
    )


def run_file(
    file, start=0, end=math.pi * 2, steps=100, on_change=lambda n: None, run_once=False
):
    """
    Method to run the given network with inputs from the given start value to the given end value with the given
    step size.

    Also print the (input, output) tuples for the Mu plotter, where input and output are respectively the input
    and the output of the network.

    Args:
        file: a file containing the neural network in neural_net representation, as provided by models.ipynb.
        start: optional; the start input of the loop, start = 0 if not provided,
               which is the minimum value for which the provided models are trained.
        end: optional; the end input of the loop, end = 2*pi if not provided,
             which is the maximum value for which the provided models are trained.
        steps: optional; the amount of steps it will loop, steps = 100 if not provided.
        on_change: optional; a lambda expression or function that is ran with every new output value,
                   on_change = lambda n: None if not provided.
        run_once: optional; if run_once == True, the demo net will be ran only once from 0 to 2*pi and will then stop.
                  If run_once == False or not set, the input will reset to 0 and keep running.
    """

    # Import neural network
    demo_net = Net(file)

    # Initialize loop variables
    step_size = (end - start) / steps
    counter = start
    while True:
        # Run inference
        output = demo_net.infer([counter])[0]
        # Print (input, output) tuple for the Mu plotter - https://codewith.mu/en/tutorials/1.1/plotter
        print((counter, output))
        # Run custom on_change function - if provided
        on_change(output)

        # Update counter
        counter += step_size
        if counter >= end:
            if run_once:
                break
            counter = start
    del demo_net
    # Forcibly collect garbage to free up memory
    gc.collect()
