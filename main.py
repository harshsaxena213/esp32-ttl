from machine import UART
import sys
import select

uart = UART(2, baudrate=115200, bits=8, parity=None, stop=1, timeout=100)

while True:
    
    if uart.any():
        data = uart.read(uart.any())
        sys.stdout.buffer.write(data)

   
    if select.select([sys.stdin], [], [], 0)[0]:
        key = sys.stdin.buffer.read(1)
        if key:
            uart.write(key)
