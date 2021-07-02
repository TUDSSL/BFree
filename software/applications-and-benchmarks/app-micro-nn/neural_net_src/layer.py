# Copyright (c) 2021 TU Delft Sustainable Systems Laboratory (https://github.com/TUDSSL/BFree/blob/main/LICENSE)

class Layer(object):
    """
    This class represents a dense layer in a neural network

    This layer utilises tensors (https://en.wikipedia.org/wiki/Tensor) - the construct of choice in neural networks.

    Attributes:
        in_size: size of the input tensor.
        out_size: size of the output tensor.
        t_in: the input tensor.
        t_out: the output tensor.
        weights: the weights tensor.
        bias: the bias tensor.
        activator: the activator function which is ran after activation
    """

    # Optional way for Python to optimize variable lookups.
    __slots__ = "t_in", "t_out", "weights", "bias", "activator"

    def __init__(self, in_size, out_size, activator=lambda x: x):
        """
        Method to initialize the neural network layer with the given in tensor size and out tensor size.
        If activator is empty, this layer will be linear.

        Args:
            in_size: the size of the input tensor.
            out_size: the size of the output tensor.
            activator: optional; the activator function. If not supplied, this will be a linear activator
        """

        # Set output tensor (input will be supplied during inference)
        self.t_in = None
        self.t_out = [0] * out_size

        # Set weight tensor
        self.weights = [0] * (in_size * out_size)
        # Set bias tensor
        self.bias = [0] * out_size
        # Set the activation method
        self.activator = activator

    def activate(self):
        """
        Method to activate this layer, runs activator and sets output tensor.
        """

        # Run for each neuron (output)
        out_size = len(self.t_out)
        for n in range(out_size):
            # Sum input of all input neurons (inputs), multiplied by corresponding weight
            input_sum = 0
            for i in range(len(self.t_in)):
                input_sum += self.t_in[i] * self.weights[i * out_size + n]
            input_sum = input_sum + self.bias[n]
            # Run activator on input
            self.t_out[n] = self.activator(input_sum)

    def read_file(self, fh):
        """
        Method to import weights and biases from an input file.

        Args:
            fh: input stream from which this layer's weights and biases are read.
        """

        # Import weight data
        for i in range(len(self.weights)):
            self.weights[i] = eval(fh.readline())
        # Import bias data
        for i in range(len(self.bias)):
            self.bias[i] = eval(fh.readline())
