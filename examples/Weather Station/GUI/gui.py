# GUI to live plot incoming BFree Weather Station data
# Inspired by: http://www.mikeburdis.com/wp/notes/plotting-serial-port-data-using-python-and-matplotlib/

import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import serial

# Open serial
ser = serial.Serial()
ser.port = '/dev/ttyACM0' #Arduino serial port
ser.timeout = 10 #specify timeout when using readline()
ser.open()
if ser.is_open==False:
    print("Failed to open serial port")
    sys.exit(1)
print("Serial port opened successfully")

# Plot animation function
def animate(i, xs, temp, humid):
    global receive_count

    if (ser.inWaiting() == 0):
        return

    # Get a line of serial data
    byte_line = ser.readline()
    line = byte_line.decode('utf-8')
    
    # Ignore empty lines
    if (line == ''):
        return

    # Check if we want to plot a data line or display text
    if ('Raw packet:' not in line):
        print(line, end='')
        return

    try:
        # Plot raw data lines
        print('Plotting line:', line, end='')

        line_data = line.split(' ')
        line_csv = line_data[2]

        data = line_csv.split(',')
        data_reboots = data[0]
        data_transmitted_messages = data[1]
        data_temp = float(data[2])
        data_humid = float(data[3])

        receive_count += 1

	    ## Add x and y to lists
        #xs.append(receive_count)
        xs.append(datetime.datetime.now())

        temp.append(data_temp)
        humid.append(data_humid)

        # Limit x and y lists to 20 items
        xs = xs[-20:]
        temp = temp[-20:]
        humid = humid[-20:]

        # Draw the updated plot
        ax[0].clear()
        ax[1].clear()
 
        ax[0].set_ylabel('Temperature (°C)')
        ax[1].set_ylabel('Humidity (%)')
        ax[1].set_xlabel('Reception Time')
        ax[0].set_title('Battery-Free Temperature + Humidity Sensor')

        ax[0].plot(xs, temp, marker='.', label="Temperature (°C)", color='orange')
        ax[1].plot(xs, humid, marker='.', label="Humidity (%)", color='blue')

        # Date formatting
        plt.gcf().autofmt_xdate()

    except:
        print('Error during parsing')

# Setup plotting
fig,ax = plt.subplots(2)
xs = []
temp = []
humid = []
receive_count = 0

# Initially set the information (not needed, but looks nicer)
ax[0].set_ylabel('Temperature (°C)')
ax[1].set_ylabel('Humidity (%)')
ax[1].set_xlabel('Reception Time')
ax[0].set_title('Battery-Free Temperature + Humidity Sensor')

# Setup the animation
ani = animation.FuncAnimation(fig, animate, fargs=(xs, temp, humid), interval=100)

# Start the show
plt.show()
