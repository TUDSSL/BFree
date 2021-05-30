from netdemo.layer import fc_layer

# A neural network
class net(object):
    __slots__ = 'layers'
    # Initialize the network, with empty layer list
    def __init__(self, file = None):
        self.layers = []
        # If a file is specified import from it
        if (file is not None):
            with open(file, 'rt') as fh:
                # First read the amount of layers
                for i in range(eval(fh.readline())):
                    # Create this layer
                    newLayer = eval(fh.readline())
                    # Import layer from file
                    newLayer.readFile(fh)
                    # Add this layer to the net
                    self.addLayer(newLayer)

    # Add a layer to this neural network (does not check sizes)
    def addLayer(self, layer):
        self.layers += [layer]

    # Run inference on this neural net
    def infer(self, input):
        # Set the initial input tensor
        nextInput = input
        # Activate each layer
        for layer in self.layers:
            # Set input of the layer to initial or output of last layer
            layer.t_in = nextInput
            # Activate it
            layer.activate()
            # Set the next input
            nextInput = layer.t_out
        # Return the last output
        return [a for a in nextInput]