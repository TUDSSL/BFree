import time
import rtc
import board
import busio
import digitalio
import checkpoint

import adafruit_rfm9x
import adafruit_si7021

## The Hardware init (restored after a reset)
i2c = busio.I2C(board.SCL, board.SDA)
temp_humid = adafruit_si7021.SI7021(i2c)

# LoRa
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm_cs = digitalio.DigitalInOut(board.D0)
rfm_reset = digitalio.DigitalInOut(board.D1)

# Benchmark pins
pin_start = digitalio.DigitalInOut(board.D4)
pin_start.pull = digitalio.Pull.DOWN

pin_done = digitalio.DigitalInOut(board.D5)
pin_done.direction = digitalio.Direction.OUTPUT
pin_done.value = False

# Benchmark Settings
SAMPLES_PER_BROADCAST = 100
BROADCASTS_PER_BENCHMARK = 50


def sendPayload(payload):
    #print('[Sending]', payload)
    checkpoint.disable()
    rfm9x = adafruit_rfm9x.RFM9x(spi, rfm_cs, rfm_reset, 868.0, baudrate=1000000)
    rfm9x.tx_power = 5
    rfm9x.send(bytes(payload, "utf-8"))
    checkpoint.enable()

class SampleCollector:
    def __init__(self, nsamples=100):
        self.nsamples = nsamples
        self.clear()

    def clear(self):
        self.count = 0
        self.temp = 0
        self.humid = 0

    def sample(self):
        self.temp = self.temp + temp_humid.temperature
        self.humid = self.humid + temp_humid.relative_humidity
        self.count = self.count + 1

    def getAvg(self):
        return self.temp/self.count, self.humid/self.count

    def isDone(self):
        if self.count >= self.nsamples:
            return True
        else:
            return False

    def broadcast(self, count):
        avg_temp, avg_humid = self.getAvg()
        data_str = str(count) + ',' + '{:.2f}'.format(avg_temp) + ',' + '{:.2f}'.format(avg_humid)+ '\n'
        sendPayload(data_str)

        #sendPayload('Broadcast #' + str(count))
        #sendPayload('↳Samples: ' + str(self.count))
        #sendPayload('↳Temperature: {:.2f}°C'.format(avg_temp))
        #sendPayload('↳Humidity: {:.2f}%'.format(avg_humid))

####
#### Benchmark start
####


# Wait for the start signal
checkpoint.disable()

restore_count_start = checkpoint.restore_count()
checkpoint_count_start = checkpoint.checkpoint_count()

while pin_start.value != True:
    pass

checkpoint.enable()


sample_collector = SampleCollector(SAMPLES_PER_BROADCAST)
broadcast_count = 0
sample_count = 0

while broadcast_count < BROADCASTS_PER_BENCHMARK:
    # Collect the samples
    while sample_collector.isDone() == False:
        sample_collector.sample()
        sample_count = sample_count + 1

    # Send the message
    sample_collector.broadcast(broadcast_count)
    broadcast_count = broadcast_count + 1

    # Reset the collector
    sample_collector.clear()

# The benchmark is done, set the done signal
pin_done.value = True


# Print some info
checkpoint_count = checkpoint.checkpoint_count() - checkpoint_count_start
restore_count = checkpoint.restore_count() - restore_count_start
while True:
    print('Checkpoint count:', checkpoint_count)
    print('Restore count:', restore_count)
    print('Total number of samples', sample_count)
    print('Total number of broadcasts', broadcast_count)
    print(str(checkpoint_count) + ', ' + str(restore_count) + ', ' + str(sample_count) + ', ' + str(broadcast_count))
    time.sleep(1)
