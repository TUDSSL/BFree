from layer import Layer


class Net(object):
    """
    Net class that represents a neural net, with functions for importing and running inference.

    Attributes:
        layers: A list of the layers in this neural net.
    """

    def __init__(self, file=None):
        """
        Initializes the neural net. Layers, weights and biases are read from the given file.
        If no file is given, it is kept empty and layers can be added manually.

        Args:
            file: Optional; An input file containing a neural network.
        """
        self.layers = []
        # If a file is specified import from it
        if file is not None:
            with open(file, "rt") as fh:
                # First read the amount of layers
                for i in range(eval(fh.readline())):
                    # Create this layer
                    new_layer = eval(fh.readline())
                    # Import layer from file
                    new_layer.read_file(fh)
                    # Add this layer to the net
                    self.layers += [new_layer]

    def infer(self, input_data):
        """
        Runs inference with the input data set as the input tensor of the first layer,
        returns the output tensor of the last layer.

        Args:
            input_data: The input tensor of the first layer.
        Returns:
            The output tensor of the last layer.
        """
        # Set the initial input tensor
        next_input = input_data
        # Activate each layer
        for layer in self.layers:
            # Set input of the layer to initial or output of last layer
            layer.t_in = next_input
            # Activate it
            layer.activate()
            # Set the next input
            next_input = layer.t_out
        # Return the last output
        return [a for a in next_input]