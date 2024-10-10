import RPi.GPIO as GPIO
import time
import pygame

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define motor pins
motor_pins = {
    'h_front': {'dir': 12, 'ena': 26},  # right front motor
    'v_b': {'dir': 2, 'ena': 15},
    'h_b': {'dir': 23, 'ena': 24},
    'v_f': {'dir': 3, 'ena': 1}
}

# Set up GPIO outputs
for motor in motor_pins.values():
    GPIO.setup(motor['dir'], GPIO.OUT)
    GPIO.setup(motor['ena'], GPIO.OUT)

# Create PWM objects
pwm = {}
for motor, pins in motor_pins.items():
    pwm[motor] = GPIO.PWM(pins['ena'], 100)  # 100 Hz PWM frequency
    pwm[motor].start(0)  # Initialize PWM with 0% duty cycle

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Get the joystick object
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Define a function to drive the motors
def drive_motors(x_axis, y_axis):
    # Map the joystick axis values to motor speeds
    speed = int((x_axis + 1) * 50)  # Map x-axis to 0-100% speed
    direction = 'forward' if y_axis > 0 else 'backward'

    # Set the motor directions and speeds
    for motor in motor_pins.keys():
        if direction == 'forward':
            GPIO.output(motor_pins[motor]['dir'], GPIO.HIGH)
        else:
            GPIO.output(motor_pins[motor]['dir'], GPIO.LOW)
        pwm[motor].ChangeDutyCycle(speed)

# Main loop
while True:
    # Read the joystick axis values
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

    # Drive the motors based on the joystick input
    drive_motors(x_axis, y_axis)

    # Update the Pygame event queue
    pygame.event.pump()

    # Limit the loop to 60 Hz
    time.sleep(1/60)

# Clean up
GPIO.cleanup()
pygame.quit()