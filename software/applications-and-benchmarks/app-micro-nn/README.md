# Simple neural network demo

A simple pure-Python neural network library. Designed for usage on the [Adafruit Metro M0](https://www.adafruit.com/product/3505).

This neural network library provides a simple and fast pure-Python way to run a neural network. It features the necessary code to read a neural net from a file, and to run inference. Activation functions are present in the form of lambda expressions, thus it supports any activation function.

Adding support for convolutional neural networks could be a future addition, however I am unsure if this is able to run on the Adafruit Metro M0 anyway due to memory and speed restrictions. Furthermore, I am unsure how to test this without a camera module.

## How to run

To run, place the [neural_net](neural_net) folder in the lib folder, and run the `run_demo` function found in [demo.py](neural_net/demo.py):

Optionally, pass a function to the `run_demo` function with an additional output handler. This output handler is a function with one parameter - the network output - and without a return value.
The default provided [main.py](main.py) changes the brightness of the [NeoPixel](https://www.adafruit.com/category/168) on the [Adafruit Metro M0](https://www.adafruit.com/product/3505): the brightness will follow the curve of a sine, thus it will slowly pulse in brightness.
Five pre-trained models are present in the library of which one is unable to run due to memory restrictions.

## Running with Mu

When running using [Mu](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor), one can automatically connect to serial.
Furthermore, the built-in plotter will plot the input and output values of the network (thus it should show a sine with the provided models).

## Files in this demo

- [README.md](README.md) A description of what was added and how to run it
- [neural_net](neural_net) Contains the net library
    - [models](neural_net/models) Contains pre-trained models
    - [demo.py](neural_net/demo.py) Contains the demo code
    - [net.py](neural_net/net.py) Contains the neural net, net parsing code and inference code.
    - [layer.py](neural_net/layer.py) Contains the layer, activation and layer parsing code.
- [main.py](main.py) An example application for running on the BFree.
- [models.ipynb](models.ipynb) The code used for creating the models in [neural_net/models](neural_net/models)

## Inspirations and contributions

Model generation code based on this [Google CoLab](https://colab.research.google.com/) [Tensorflow Lite example](https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/train/train_hello_world_model.ipynb), a notebook 

Code written by [Max Groenenboom](https://github.com/MaxGroenenboom).
