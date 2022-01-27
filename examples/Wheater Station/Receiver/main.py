import board
import busio
import digitalio
import adafruit_rfm9x

def prettyPrintMessage(payload):
    payload_fields = payload.split(',')
    #print(payload_fields)

    reboot_count = payload_fields[0]
    transmitted_messages = payload_fields[1]
    average_temperature = payload_fields[2]
    average_humidity = payload_fields[3]

    print('Raw packet:', payload, end='')
    print('Message content:')
    print('  Reboot count =', reboot_count)
    print('  Transmitted messages =', transmitted_messages)
    print('  Average temperature (C) =', average_temperature)
    print('  Average humidity (%) =', average_humidity)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.D0)
reset = digitalio.DigitalInOut(board.D1)

rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 868.0, baudrate=1000000)

print('Start receiving packets')
while True:
    packet = rfm9x.receive()  # Wait for a packet to be received (up to 0.5 seconds)
    if packet is not None:
        message = str(packet, 'ascii')
        prettyPrintMessage(message)
   # try:
   #     packet = rfm9#.receive()  # Wait for a packet to be received (up to 0.5 seconds)
   #     if packet is #ot None:
   #         message =#str(packet, 'ascii')
   #         prettyPri#tMessage(message)
   # except:
   #     print('malformed packet received')
   #     pass
