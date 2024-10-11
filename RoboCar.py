import RPi.GPIO as GPIO
import time
from sshkeyboard import listen_keyboard
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

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




def Goforward():
    print("going forward")
    set_motor('h_front', 'forward', 100) 
    set_motor('v_b', 'forward', 100)
    set_motor('h_b', 'forward', 100)
    set_motor('v_f', 'forward', 100)

def Gobackward():
    print ("Going Backwards")
    set_motor('h_front', 'backward', 50)
    set_motor('v_b', 'backward', 50)
    set_motor('h_b', 'backward', 50)
    set_motor('v_f', 'backward', 50)
def Goleft():
    print ("Going Left")
    set_motor('h_front', 'forward', 60)
    set_motor('v_b', 'backward', 40)
    set_motor('h_b', 'forward', 60)
    set_motor('v_f', 'backward', 40)
def Goright():
    print ("Going Right")
    set_motor('h_front', 'backward', 40) 
    set_motor('v_b', 'forward', 60)
    set_motor('h_b', 'backward', 40)
    set_motor('v_f', 'forward', 60)

def press(key):
    switch = {
        'w': Goforward,
        's': Gobackward,
        'a': Goleft,
        'd': Goright
    }
    if key in switch:
        switch[key]()
    elif key == 'esc':  # press esc to stop
        return False



while True:
    listen_keyboard(on_press=press)
