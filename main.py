#!/usr/bin/python3
import RPi.GPIO as GPIO

thermal_cat = '/sys/class/thermal/thermal_zone0/temp'
timer_delay = 1
gpio_port = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_port, GPIO.OUT)


def get_thermal(cmd):
    t_file = open(cmd)
    temp = float(t_file.read())
    t_file.close()
    return temp / 1000


def gpio_control(temp):
    if temp >= 40.0:
        GPIO.output(gpio_port, 1)
        print("Temperature exceeded", str(temp), "GPIO port", gpio_port, "now is active")
    else:
        GPIO.output(gpio_port, 0)
        print("Temperature is", str(temp) + ". Not advisable to turn on the fan.")


if __name__ == '__main__':
    import time
    while True:
        try:
            gpio_control(get_thermal(thermal_cat))

        except:
            GPIO.cleanup()

        time.sleep(timer_delay)
