from machine import Pin
import time

led = Pin(15, Pin.OUT)
add_a = Pin(2, Pin.IN, Pin.PULL_DOWN)
add_b = Pin(3, Pin.IN, Pin.PULL_DOWN)
add_cin = Pin(4, Pin.IN, Pin.PULL_DOWN)

add_sum = Pin(6, Pin.OUT)
add_cout = Pin(7, Pin.OUT)

while True:
    add_sum.value((add_a.value() + add_b.value() + add_cin.value()) % 2)
    add_cout.value(int((add_a.value() + add_b.value() + add_cin.value()) / 2))