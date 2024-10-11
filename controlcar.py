import pygame
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

# Motor control functions
def forward():
    print("Moving forward")

def backward():
    print("Moving backward")

def right():
    print("Turning right")

def left():
    print("Turning left")

def stop():
    print("Stopping")

# Main loop
running = True
while running:
    for event in pygame.event.get():  # Get events from joystick
        if event.type == pygame.JOYAXISMOTION:
            pass

    # Read joystick inputs
    x_axis = joystick.get_axis(0)  # Left stick, X-axis
    y_axis = joystick.get_axis(1)  # Left stick, Y-axis

    # Check if joystick axes are within deadzone range
    if abs(x_axis) <= DEADZONE and abs(y_axis) <= DEADZONE:
        stop()  # Stop the car if joystick is not moved
    else:
        # Control the car's movement based on joystick inputs
        if abs(y_axis) > DEADZONE:
            if y_axis < 0:
                forward()  # Move forward
            elif y_axis > 0:
                backward()  # Move backward
        if abs(x_axis) > DEADZONE:
            if x_axis > 0:
                right()  # Turn right
            elif x_axis < 0:
                left()  # Turn left

    # Add a delay to avoid flooding the console
    time.sleep(0.1)

pygame.quit()