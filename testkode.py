import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


motor_pins = {
    'h_front': {'dir': 12, 'ena': 26}, #højre forreste
    'v_b': {'dir': 2, 'ena': 15},
    'h_b': {'dir': 23, 'ena': 24},
    'v_f': {'dir': 4, 'ena': 1},
}


for motor in motor_pins.values():
    GPIO.setup(motor['dir'], GPIO.OUT)
    GPIO.setup(motor['ena'], GPIO.OUT)


pwm = {}
for motor, pins in motor_pins.items():
    pwm[motor] = GPIO.PWM(pins['ena'], 100)  
    pwm[motor].start(0) 


def set_motor(motor, direction, speed):
    if direction == 'forward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.HIGH)
    elif direction == 'backward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.LOW)
    
    pwm[motor].ChangeDutyCycle(speed)

#set_motor('h_front', 'forward', 50) #højre forreste
#set_motor('v_b', 'forward', 50)
#set_motor('h_b', 'forward', 50)
set_motor('v_f', 'forward', 50)

time.sleep(20)


#set_motor('h_front', 'backward', 75)
#set_motor('v_b', 'backward', 75)
#set_motor('h_b', 'backward', 75)
set_motor('v_f', 'backward', 75)

time.sleep(2)


for motor in motor_pins.keys():
    pwm[motor].ChangeDutyCycle(0)

GPIO.cleanup()
