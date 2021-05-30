# A fully connected layer
class fc_layer(object):
    # Initialize the fully connected layer, default activator is the simple linear one
    def __init__(self, in_size, out_size, activator = lambda x:x):
        # Remember sizes
        self.in_size = in_size
        self.out_size = out_size

        # Set input and output tensors
        self.t_in = [0] * in_size
        self.t_out = [0] * out_size

        # Set weight tensor
        self.weights = [0] * (in_size * out_size)
        # Set bias tensor
        self.bias = [0] * out_size
        # Set the activation method
        self.activator = activator

    # Activate this layer
    def activate(self):
        # Run for each neuron (output):
        for n in range(self.out_size):
            # Sum input of all input neurons (inputs), multiplied by corresponding weight
            inputv = 0
            for i in range(self.in_size):
                inputv += self.t_in[i] * self.weights[i * self.out_size + n]
            inputv = inputv + self.bias[n]
            # Run activator on input
            self.t_out[n] = self.activator(inputv)

    # Read weight and bias data from an input file
    def readFile(self, fh):
        # Import weight data
        for i in range(len(self.weights)):
            self.weights[i] = eval(fh.readline())
        # Import bias data
        for i in range(len(self.bias)):
            self.bias[i] = eval(fh.readline())