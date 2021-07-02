# Simple neural network demo

A simple pure-Python neural network library. Designed for usage on the [Adafruit Metro M0](https://www.adafruit.com/product/3505).

This neural network library provides a simple and fast pure-Python way to run a simple [feedforward neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network).
It features the necessary code to import a neural network from a file which contains the weights and biases for each layer, and to run inference.
[Activation functions](https://en.wikipedia.org/wiki/Activation_function) are present in the form of [lambda expressions](https://www.w3schools.com/python/python_lambda.asp), thus it supports any activation function.

## How to run the demo

To run the demo, place the [neural_net](neural_net) folder in the library folder of the Adafruit Metro M0, and run the `run_demo` function found in [demo.py](neural_net_src/demo.py).
A function can be passed to the `run_demo` call. Every time a result is returned by the network, this function is called with this result as the argument.
The default provided [main.py](main.py) changes the brightness of the [NeoPixel](https://www.adafruit.com/category/168) on the [Adafruit Metro M0](https://www.adafruit.com/product/3505): the brightness will follow the curve of a sine.
Four pre-trained models are present in the library which are imported and ran in the demo.

## Files in this demo

- [README.md](README.md) This file; a description of what was added and how to run it.
- [neural_net](neural_net) The compiled neural network library.
    - [models](neural_net/models) Four pre-trained neural networks of a sine.
- [neural_net_src](neural_net_src) The source code of the neural network library.
    - [demo.py](neural_net_src/demo.py) The demo code of the neural network.
    - [net.py](neural_net_src/net.py) The neural network, net parsing code and inference code.
    - [layer.py](neural_net_src/layer.py) The layer, activation and layer parsing code.
- [main.py](main.py) An example application for running on [BFree](https://github.com/TUDSSL/BFree/).
- [models.ipynb](models.ipynb) The code used for creating the models in [neural_net/models](neural_net/models).

To optimize memory usage, this library is compiled using [mpy-cross](https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library?view=all#mpy-2982472-11).
The [neural_net](neural_net) folder contains the compiled neural network library.

## Testing and development conditions

This library was developed using the [Mu](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor) editor and [PyCharm](https://www.jetbrains.com/pycharm/).

The device used to develop and test the code in this repository on was a [Adafruit Metro M0 Express with ATSAMD21G18](https://www.adafruit.com/product/3505) running Adafruit [CircuitPython 6.3.0](https://circuitpython.org/).

When connected over USB and developing using [Mu](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor) one can connect to the serial console within the IDE.
Furthermore, the [built-in plotter](https://codewith.mu/en/tutorials/1.1/plotter) in Mu will automatically plot the input and output values of the network (thus it shows a sine wave with the provided models in the plotter window).

## Known issues and limitations

Due to the amount of memory on Adafruit Metro M0 and the size of variables in Python, only small models can be used.
However, this proof of concept proves that a simple function can be modelled by a neural network using this library.

Currently, the demo is unable to run without manually ordering the garbage collector (Using a `gc.collect()` call) to collect unused memory after a network has been deleted.
We do not know why the garbage collector is not doing its job.

Adding support for convolutional neural networks could be a future addition, however we are not sure if such a network can run on Adafruit Metro M0 anyway due to memory restrictions.

## Inspirations and contributions

Model generation code based on [Google CoLab](https://colab.research.google.com/) [Tensorflow Lite example](https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/train/train_hello_world_model.ipynb), a notebook detailing how to create a neural network for usage on microcontrollers.

Code written by [Max Groenenboom](https://github.com/MaxGroenenboom).
