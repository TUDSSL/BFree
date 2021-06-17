class FCLayer(object):
    """Represents a fully connected layer"""
    __slots__ = "in_size", "out_size", "t_in", "t_out", "weights", "bias", "activator"

    def __init__(self, in_size, out_size, activator=lambda x: x):
        """Initialize the layer with the given in tensor size and out tensor size.
        If activator is empty, this layer will be linear."""

        # Remember sizes
        self.in_size = in_size
        self.out_size = out_size

        # Set output tensor (input will be copied from the previous layer)
        self.t_out = [0] * out_size

        # Set weight tensor
        self.weights = [0] * (in_size * out_size)
        # Set bias tensor
        self.bias = [0] * out_size
        # Set the activation method
        self.activator = activator

    def activate(self):
        """Activate this layer, runs activator and sets output tensor"""

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
        """Import weight and bias data from an input file"""

        # Import weight data
        for i in range(len(self.weights)):
            self.weights[i] = eval(fh.readline())
        # Import bias data
        for i in range(len(self.bias)):
            self.bias[i] = eval(fh.readline())
