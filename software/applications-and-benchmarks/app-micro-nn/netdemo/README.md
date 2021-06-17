# Simple neural network demo.
A simple full python neural network library. Originally meant for usage on the Adafruit Metro M0.
Currently only supports fully connected layers.

To run, place the `netdemo` folder in the root of the device, then add the following lines to the main:

```
import netdemo
netdemo.run()
```

Optionally, pass a function to runDemo with an additional output handler.
The default main changes the brightness of the NeoLED on the Adafruit Metro M0.

When running using [Mu](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor),
one can automatically connect to serial.
Furthermore, the built-in plotter will plot the input and output values of the network (thus it should show a sine).

Created by Max Groenenboom.

Inspired by https://github.com/can1357/simple_cnn
