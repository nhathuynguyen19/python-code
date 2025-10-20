import time
import platform
import os

def clearTerminal():
    if platform.system == "Windows":
        os.system('cls')
    else:
        os.system('clear')

i = 0
minute = 0
hour = 0
while True:
    clearTerminal()
    minute = i % 60
    if (minute % 59 == 0):
        hour += 1
    print(f"{hour}:{minute}")
    time.sleep(1)
    i += 1
