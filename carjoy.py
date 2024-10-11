import pygame
import serial
import time

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

# Initialize the serial connection
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace COM3 with your serial port

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
            ser.write(b'forward')  # Send 'forward' command
        elif y_axis > 0:
            ser.write(b'backward')  # Send 'backward' command
    if abs(x_axis) > DEADZONE:
        if x_axis > 0:
            ser.write(b'right')  # Send 'right' command
        elif x_axis < 0:
            ser.write(b'left')  # Send 'left' command

    # Add a delay to avoid flooding the serial connection
    time.sleep(0.1)

pygame.quit()