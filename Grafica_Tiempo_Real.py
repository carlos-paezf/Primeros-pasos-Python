import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import numpy as np


gData = []
gData.append([0.0])
gData.append([0.0])


def getData(out_data):
    with serial.Serial("\\.\COM4", 115200) as ser:
        while True:
            line = ser.readline().decode('utf-8')
            try:
                out_data[1].append(float(line))
                if len(out_data[1]) > 200:
                    out_data[1].pop(0)
            except:
                pass


dataCollector = threading.Thread(target=getData, args=(gData,))
dataCollector.start()


def update_line(num, hl, data):
    dx = np.array(range(len(data[1])))
    dy = np.array(data[1])
    hl.set_data(dx, dy)
    return hl,


fig = plt.figure(figsize=(10, 8))
plt.ylim(-1.5, 1.5)
plt.xlim(0, 200)
hl, = plt.plot(gData[0], gData[1])

line_ani = animation.FuncAnimation(
    fig, update_line, fargs=(hl, gData), interval=50, blit=False
    )

plt.show()

dataCollector.join()
