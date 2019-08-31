import json
import matplotlib.pyplot as plt
import numpy as np
import os
import socket
import sys
from datetime import datetime

exception_text = """
    Argument(s) missing.
    Script usage: python UDP_stats.py IP_mode(0: local, 1: ethernet)
"""
if len(sys.argv) < 2:
    raise Exception(exception_text)
elif sys.argv[1] not in set({"0", "1"}):
    raise Exception(exception_text)

# change IP and choose modes properly
UDP_IP = "127.0.0.1"  # local IP
if sys.argv[1] == "1":
    UDP_IP = "169.254.143.183"  # ethernet IP
UDP_PORT = 11000

MODULE_NAME = "stats"

x = []
y = []
c = []

tot_count = 0
cur_level = 0.0
cur_count = 0

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
# release right after program finishes
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

plt.axis([0, 1, 0, 1.0])
plt.ion()
axes = plt.gca()
line, = axes.plot(x, y, 'b-')
plt.show()

print("Starting - {}".format(MODULE_NAME))
counter = 1 
marker_size = 36
while True:
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    except KeyboardInterrupt:
        # save figure and exit
        dir_path = "stats"
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_name = "ReKnobPerfStream " + str(datetime.now()) + ".jpg"
        plt.savefig(os.path.join(dir_path, file_name))
        sys.exit()
    print("[{}]".format(MODULE_NAME), "R", data.decode())
    msg = data.decode()
    obj = json.loads(msg)
    x.append(counter)
    level = obj["difficulty"]
    y.append(level)
    c.append(obj["isCorrect"])
    axes.set_xlim(0, len(x) + 2)
    line.set_xdata(x)
    line.set_ydata(y)

    if level != cur_level:
        cur_count = 0
        cur_level = level
    tot_count += 1
    cur_count += 1
    print("Summary Total [{}], Cur [{}], Level [{}]\n".format(tot_count, cur_count, cur_level))

    if counter % 8 == 0:
        if marker_size > 6:
            marker_size -= 6
            # print("marker downsize", marker_size)

    for xp, yp, m in zip(x, y, c):
        if m == 1:
            mark = "s"
            color = "green"
        else:
            color = "red"
            mark = "o" 
        axes.scatter([xp],[yp], marker=mark, color=color, s=marker_size)

    axes.plot()
    plt.draw()
    plt.pause(0.001)
    counter += 1
