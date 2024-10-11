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
GPIO.setup(17, GPIO.OUT)  # Motor 1 forward
GPIO.setup(23, GPIO.OUT)  # Motor 1 backward
GPIO.setup(24, GPIO.OUT)  # Motor 2 forward
GPIO.setup(25, GPIO.OUT)  # Motor 2 backward

# Motor control functions
def forward():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.LOW)

def backward():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)

def right():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.HIGH)

def left():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.LOW)

def stop():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)

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