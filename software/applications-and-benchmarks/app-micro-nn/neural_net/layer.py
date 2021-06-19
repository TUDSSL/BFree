class Layer(object):
    """
    Represents a dense layer

    Attributes:
        in_size: Size of the input tensor.
        out_size: Size of the output tensor.
        t_in: The input tensor.
        t_out: The output tensor.
        weights: The weights tensor.
        bias: The bias tensor.
        activator: The activator function which is ran after activation.
    """

    # Optional way for Python to optimize variable lookups.
    __slots__ = "in_size", "out_size", "t_in", "t_out", "weights", "bias", "activator"

    def __init__(self, in_size, out_size, activator=lambda x: x):
        """
        Initialize the layer with the given in tensor size and out tensor size.
        If activator is empty, this layer will be linear.

        Args:
            in_size: The size of the input tensor.
            out_size: The size of the output tensor.
            activator: Optional; the activator function. If not supplied, this will be a linear activator.
        """

        # Remember sizes
        self.in_size = in_size
        self.out_size = out_size

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
        Activate this layer, runs activator and sets output tensor.
        """

        # Run for each neuron (output):
        for n in range(self.out_size):
            # Sum input of all input neurons (inputs), multiplied by corresponding weight
            input_sum = 0
            for i in range(self.in_size):
                input_sum += self.t_in[i] * self.weights[i * self.out_size + n]
            input_sum = input_sum + self.bias[n]
            # Run activator on input
            self.t_out[n] = self.activator(input_sum)

    def read_file(self, fh):
        """
        Imports weight and bias data from an input file.

        Args:
            fh: Input stream from which this layer's weights and biases are read.
        """

        # Import weight data
        for i in range(len(self.weights)):
            self.weights[i] = eval(fh.readline())
        # Import bias data
        for i in range(len(self.bias)):
            self.bias[i] = eval(fh.readline())
