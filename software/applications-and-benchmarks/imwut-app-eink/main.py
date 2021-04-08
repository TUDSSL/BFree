import time
import rtc
import busio
import board
import digitalio
import checkpoint
import adafruit_pcf8523
import adafruit_si7021

import epd_temperature

# Constant lookup for the days
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# The Hardware init (restored after a reset)
i2c = busio.I2C(board.SCL, board.SDA)
rtc_ext = adafruit_pcf8523.PCF8523(i2c)
temp_humid = adafruit_si7021.SI7021(i2c)
rtc.set_time_source(rtc_ext)

# Benchmark pins
pin_start = digitalio.DigitalInOut(board.D4)
pin_start.pull = digitalio.Pull.DOWN

pin_done = digitalio.DigitalInOut(board.D5)
pin_done.direction = digitalio.Direction.OUTPUT
pin_done.value = False

# Benchmark Settings
SECONDS_PER_REFRESH = 10
REFRESHES_PER_BENCHMARK = 25

def timestr(timestamp):
    if timestamp == None:
        return None
    t = time.localtime(timestamp)
    time_str = '{:d}-{:02d}-{:02d} ({}) {:02d}:{:02d}:{:02d}'.format(t.tm_year, t.tm_mon, t.tm_mday, days[t.tm_wday], t.tm_hour, t.tm_min, t.tm_sec)
    return time_str

class Sample:
    def __init__(self):
        global reading_count
        global rtc
        global temp_humid
        self.temp = temp_humid.temperature
        self.humid = temp_humid.relative_humidity
        self.time_end = time.time()

class PeriodSample:
    def __init__(self):
        self.temp = 0.0
        self.humid = 0.0
        self.cnt = 0

    def update(self, s):
        self.temp = self.temp + s.temp
        self.humid = self.humid + s.humid
        self.cnt = self.cnt + 1

    def calc(self):
        self.temp = self.temp / self.cnt
        self.humid = self.humid / self.cnt

# Draw the base image on the e-ink
epd_temperature.draw_base()


####
#### Benchmark start
####

checkpoint.disable()

restore_count_start = checkpoint.restore_count()
checkpoint_count_start = checkpoint.checkpoint_count()

while pin_start.value != True:
    pass

checkpoint.enable()


refresh_count = 0
sample_count = 0

start_time = time.time()
#print('Start time:', timestr(start_time))

pstart = start_time
s = Sample()

# Draw the intial temperature as the starting temperature to the e-ink
epd_temperature.draw_temperature(int(s.temp))
pend = pstart

while refresh_count < REFRESHES_PER_BENCHMARK:
    #pend = pstart + SECONDS_PER_REFRESH
    pend = pend + SECONDS_PER_REFRESH
    pdone = False
    ps = PeriodSample()
    #print('End of period:', timestr(pend))
    while pdone == False:
        ps.update(s)
        sample_count = sample_count + 1
        #print('sample time:', timestr(s.time_end), 'Temperature:', s.temp)
        if s.time_end > pend:
            pdone = True
            pstart = s.time_end
        #time.sleep(1)
        s = Sample()
    ps.calc()

    temp_int = int(ps.temp)
    #print('Period complete, avg temp:', ps.temp)
    epd_temperature.draw_temperature(temp_int)
    refresh_count = refresh_count + 1

# The benchmark is done, set the done signal
pin_done.value = True

# Print some info
checkpoint_count = checkpoint.checkpoint_count() - checkpoint_count_start
restore_count = checkpoint.restore_count() - restore_count_start
while True:
    print('Start time:', timestr(start_time))
    print('Checkpoint count:', checkpoint_count)
    print('Restore count:', restore_count)
    print('Total number of samples', sample_count)
    print('Total number of refreshes', refresh_count)
    print(str(checkpoint_count) + ', ' + str(restore_count) + ', ' + str(sample_count) + ', ' + str(refresh_count))
    time.sleep(1)
