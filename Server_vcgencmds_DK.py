#Doyun Kim (100924397)
#Server_vcgencmds
# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/import socket
import os
import json

# Create and bind the socket
s = socket.socket()
host = '192.168.10.111'  # localhost
port = 5000
s.bind((host, port))
s.listen(5)

# Server loop to handle connections
while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # Collect vcgencmd data directly using os.popen
    core_temp = float(os.popen('vcgencmd measure_temp').readline()
    gpu_mem = int(os.popen('vcgencmd get_mem gpu').readline()
    cpu_mem = int(os.popen('vcgencmd get_mem arm').readline()
    cpu_freq = round(int(os.popen('vcgencmd measure_clock arm').readline()
    core_volt = round(float(os.popen('vcgencmd measure_volts core').readline()

    # Create a JSON object with the collected data
    data = {
        "Core Temperature (°C)": round(core_temp, 1),
        "GPU Memory (MB)": gpu_mem,
        "CPU Memory (MB)": cpu_mem,
        "CPU Frequency (MHz)": cpu_freq,
        "Core Voltage (V)": core_volt,
    }

    # Convert the data to a JSON string and send it
    res = json.dumps(data).encode('utf-8')
    c.send(res)
    c.close()
