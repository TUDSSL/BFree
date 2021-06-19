# Simple neural network demo

A simple pure-Python neural network library. Designed for usage on the [Adafruit Metro M0](https://www.adafruit.com/product/3505).

This neural network library provides a simple and fast pure-Python way to run a neural network. It features the necessary code to read a neural net from a file, and to run inference. Activation functions are present in the form of lambda expressions, thus it supports any activation function.

Adding support for convolutional neural networks could be a future addition, however I am unsure if this is able to run on the Adafruit Metro M0 anyway due to memory and speed restrictions. Furthermore, I am unsure how to test this without a camera module.

## How to run

To run, place the [neural_net](neural_net) folder in the lib folder, and run the `run_demo` function found in [demo.py](neural_net_src/demo.py):

Optionally, pass a function to the `run_demo` function with an additional output handler. This output handler is a function with one parameter - the network output - and without a return value.
The default provided [main.py](main.py) changes the brightness of the [NeoPixel](https://www.adafruit.com/category/168) on the [Adafruit Metro M0](https://www.adafruit.com/product/3505): the brightness will follow the curve of a sine, thus it will slowly pulse in brightness.
Five pre-trained models are present in the library of which one is unable to run due to memory restrictions.

## Files in this demo

- [README.md](README.md) A description of what was added and how to run it.
- [neural_net](neural_net) Contains the compiled library.
    - [models](neural_net/models) Contains pre-trained models.
- [neural_net_src](neural_net_src) Contains the source code of the library.
    - [demo.py](neural_net_src/demo.py) Contains the demo code.
    - [net.py](neural_net_src/net.py) Contains the neural net, net parsing code and inference code.
    - [layer.py](neural_net_src/layer.py) Contains the layer, activation and layer parsing code.
- [main.py](main.py) An example application for running on the BFree.
- [models.ipynb](models.ipynb) The code used for creating the models in [neural_net/models](neural_net/models).

## Testing and development conditions

This library was developed using the [Mu](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor) editor and [PyCharm](https://www.jetbrains.com/pycharm/).

The device used to develop and test on was a [Adafruit Metro M0 Express with samd21g18](https://www.adafruit.com/product/3505) running Adafruit CircuitPython 6.1.0.

When running using [Mu](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor), one can automatically connect to serial.
Furthermore, the built-in plotter will plot the input and output values of the network (thus it should show a sine with the provided models).

## Known issues and limitations

Currently the demo is unable to run without manually ordering the garbage collector to collect after a network has been deleted. I am unsure why the garbage collector is not doing its job.

Due to the added size of documentation, it is now necessary to crosscompile the library using [mpy-cross](https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library?view=all#mpy-2982472-11), however I have not yet been able to get this to work, so the 32+64 layer model is not working now.

## Inspirations and contributions

Model generation code based on this [Google CoLab](https://colab.research.google.com/) [Tensorflow Lite example](https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/train/train_hello_world_model.ipynb), a notebook 

Code written by [Max Groenenboom](https://github.com/MaxGroenenboom).
