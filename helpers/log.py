import sys
import os

def log(date, folder, packet_data):
    date = date.replace(" ", "_")
    date = date.replace(".", "_")
    date = date.replace(":", "-")
    newLog = f'{os.getcwd()}\\{folder}\\{date}.txt'
    with open(newLog, 'w+') as file:
        file.write(packet_data.hex())
        print(f'Log saved at {newLog}')

sys.modules[__name__] = log