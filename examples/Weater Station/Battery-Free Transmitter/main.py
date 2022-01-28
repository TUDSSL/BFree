import time
import busio
import board
import digitalio
import adafruit_si7021
import adafruit_rfm9x

# The checkpoint bindings
import checkpoint

# The Hardware init (restored after a power failure)

# The temperature/humidity sensor
i2c = busio.I2C(board.SCL, board.SDA)
temp_humid = adafruit_si7021.SI7021(i2c)

# The LoRa transmitter
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm_cs = digitalio.DigitalInOut(board.D0)
rfm_reset = digitalio.DigitalInOut(board.D1)

# Send a string payload over LoRa
def sendPayload(payload):
    # Sending a LoRa message is an 'atomic' action
    # We can NOT continue it halfway through (as we can not make the LoRa module intermittently safe)
    checkpoint.disable()
    
    # Send the message
    rfm9x = adafruit_rfm9x.RFM9x(spi, rfm_cs, rfm_reset, 868.0, baudrate=1000000)
    rfm9x.tx_power = 5
    rfm9x.send(bytes(payload, "utf-8"))
    
    # Re-enable the checkpoints
    checkpoint.enable()

# A sample class holding one sensor reading
class Sample:
    def __init__(self):
        global reading_count
        global temp_humid
        self.temp = temp_humid.temperature
        self.humid = temp_humid.relative_humidity
        
# A class to track the accumulated samples and average them
class SampleGroup:
    def __init__(self, sample_goal=10):
         # The number of samples needed in this group
        self.sample_goal = sample_goal
        
        # Reset the group
        self.reset()
        
    # Reset the group the the initial values
    def reset(self):
        # Sample values
        self.temp = 0.0
        self.humid = 0.0
        # The current number of samples in the group
        self.cnt = 0

    # Update the group with a new sample
    def update(self, s):
        self.temp = self.temp + s.temp
        self.humid = self.humid + s.humid
        self.cnt = self.cnt + 1
        
        # Return 'True' when we reach the desired number of samples
        if (self.cnt == self.sample_goal):
            # Compute the averages
            average_temp = self.temp / self.cnt
            average_humid = self.humid / self.cnt
            # Reset the group
            self.reset()
            # Return the averages
            return average_temp, average_humid
        else:
            # We did not yet collect the required number of samples
            # So we return 'None'
            return None


# Create the group that holds our samples until we collected enough
G = SampleGroup()

# Some interesting values to track
TotalSampleCount = 0
TotalPacketsTransmitted = 0

# Loop this forever
while True:
    # Collect a sample
    s = Sample()
    TotalSampleCount += 1
    
    # Add the sample to the group
    result = G.update(s)
    
    # If we collected enough samples we send them!
    if result != None:
        # Unwrap the average values
        average_temp = result[0] # The first value in the return statement
        average_humid = result[1] # The second value in the return statement
        
        # Build the LoRa message
        PowerFailureCount = checkpoint.restore_count()
        TotalPacketsTransmitted += 1
        lora_payload_string = str(PowerFailureCount) \
            + ',' + str(TotalPacketsTransmitted) \
            + ',' + '{:.2f}'.format(average_temp) \
            + ',' + '{:.2f}'.format(average_humid) \
            + '\n'
        
        # Broadcast the payload over LoRa
        sendPayload(lora_payload_string)
    
        # Print information to the console (only when USB is connected)
        # Can be usefull for debugging the application
        print('Sending LoRa message completed')
        print('\tPower-failure count:', PowerFailureCount)
        print('\tSamples collected:', TotalSampleCount)
        print('\tTransmitted packets:', TotalPacketsTransmitted)
        print('\tAverage temperature:', average_temp)
        print('\tAverage humidity:', average_humid)
        print('')
