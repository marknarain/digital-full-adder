from machine import Pin

a = Pin(2, Pin.IN, Pin.PULL_DOWN)
b = Pin(3, Pin.IN, Pin.PULL_DOWN)
cin = Pin(4, Pin.IN, Pin.PULL_DOWN)

s = Pin(9, Pin.OUT)
cout = Pin(10, Pin.OUT)

while True:
    sum_val = a.value() + b.value() + cin.value()
    s.value(sum_val & 1)
    cout.value(sum_val >> 1)