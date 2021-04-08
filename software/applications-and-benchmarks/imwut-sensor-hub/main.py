import board
import busio
import digitalio
import adafruit_rfm9x

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.D0)
reset = digitalio.DigitalInOut(board.D1)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 868.0, baudrate=1000000)

print('Start receiving packets')
while True:
    packet = rfm9x.receive()  # Wait for a packet to be received (up to 0.5 seconds)
    if packet is not None:
        packet_text = str(packet, 'ascii')
        print(packet_text)
        #print('Received: {0}'.format(packet_text))

