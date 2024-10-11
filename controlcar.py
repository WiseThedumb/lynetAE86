
import pygame
import time
import RPi.GPIO as GPIO

# Initialize Pygame and joystick
pygame.init()
pygame.joystick.init()

# Check if a controller is connected
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("PlayStation controller connected:", joystick.get_name())
else:
    print("No controller found")
    exit()

# Set deadzone value
DEADZONE = 0.1

# Set up GPIO pins for motor control
GPIO.setmode(GPIO.BCM)
motor_pins = {
    'h_front': {'dir': 12, 'ena': 26}, #højre forreste
    'v_back': {'dir': 2, 'ena': 15},
    'h_back': {'dir': 23, 'ena': 24},
    'v_front': {'dir': 4, 'ena': 1},
}

for motor in motor_pins.values():
    GPIO.setup(motor['dir'], GPIO.OUT)
    GPIO.setup(motor['ena'], GPIO.OUT)

pwm = {}
for motor, pins in motor_pins.items():
    pwm[motor] = GPIO.PWM(pins['ena'], 100)  
    pwm[motor].start(0)  

# Motor control functions
def forward():
    GPIO.output(motor_pins['h_front']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['v_back']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['h_back']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['v_front']['dir'], GPIO.HIGH)
    pwm['h_front'].ChangeDutyCycle(75)
    pwm['v_back'].ChangeDutyCycle(75)
    pwm['h_back'].ChangeDutyCycle(75)
    pwm['v_front'].ChangeDutyCycle(75)

def backward():
    GPIO.output(motor_pins['h_front']['dir'], GPIO.LOW)
    GPIO.output(motor_pins['v_back']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['h_back']['dir'], GPIO.LOW)
    GPIO.output(motor_pins['v_front']['dir'], GPIO.HIGH)
    pwm['h_front'].ChangeDutyCycle(75)
    pwm['v_back'].ChangeDutyCycle(75)
    pwm['h_back'].ChangeDutyCycle(75)
    pwm['v_front'].ChangeDutyCycle(75)

def right():
    GPIO.output(motor_pins['h_front']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['v_back']['dir'], GPIO.LOW)
    GPIO.output(motor_pins['h_back']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['v_front']['dir'], GPIO.HIGH)
    pwm['h_front'].ChangeDutyCycle(50)
    pwm['v_back'].ChangeDutyCycle(50)
    pwm['h_back'].ChangeDutyCycle(50)
    pwm['v_front'].ChangeDutyCycle(50)

def left():
    GPIO.output(motor_pins['h_front']['dir'], GPIO.LOW)
    GPIO.output(motor_pins['v_back']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['h_back']['dir'], GPIO.HIGH)
    GPIO.output(motor_pins['v_front']['dir'], GPIO.LOW)
    pwm['h_front'].ChangeDutyCycle(50)
    pwm['v_back'].ChangeDutyCycle(50)
    pwm['h_back'].ChangeDutyCycle(50)
    pwm['v_front'].ChangeDutyCycle(50)

def stop():
    pwm['h_front'].ChangeDutyCycle(0)
    pwm['v_back'].ChangeDutyCycle(0)
    pwm['h_back'].ChangeDutyCycle(0)
    pwm['v_front'].ChangeDutyCycle(0)

# Main loop
running = True
while running:
    for event in pygame.event.get():  # Get events from joystick
        if event.type == pygame.JOYAXISMOTION:
            pass

    # Read joystick inputs
    x_axis = joystick.get_axis(0)  # Left stick, X-axis
    y_axis = joystick.get_axis(1)  # Left stick, Y-axis

    # Control the car's movement based on joystick inputs
    if abs(y_axis) > DEADZONE:
        if y_axis < 0:
            forward()  # Move forward
        elif y_axis > 0:
            backward()  # Move backward
    else:
        stop()  # Stop the car

    if abs(x_axis) > DEADZONE:
        if x_axis > 0:
            right()  # Turn right
        elif x_axis < 0:
            left()  # Turn left
    else:
        stop()  # Stop the car

    # Add a delay to avoid flooding the console
    time.sleep(0.1)

pygame.quit()
GPIO.cleanup()