from hscro4 import HCSR04

sensor = HCSR04(trigger_pin=2, echo_pin=3)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')