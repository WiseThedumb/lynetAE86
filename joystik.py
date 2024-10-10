import pygame

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

# Main loop
running = True
while running:
    for event in pygame.event.get():  # Get events from joystick
        if event.type == pygame.JOYAXISMOTION:
            pass
    x_axis = joystick.get_axis(0)  # Left stick, X-axis
    y_axis = joystick.get_axis(1)  # Left stick, Y-axis

    # Check direction
    if abs(y_axis) > DEADZONE:
        if y_axis < 0:
            print("Moving forward")
        elif y_axis > 0:
            print("Moving backward")

    if abs(x_axis) > DEADZONE:
        if x_axis > 0:
            print("Turning right")
        elif x_axis < 0:
            print("Turning left")

    pygame.time.delay(100)  # Add a delay to avoid flooding the console

pygame.quit()