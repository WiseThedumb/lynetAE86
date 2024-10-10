import RPi.GPIO as GPIO
import time
from time import sleep

# Pins til hastighed (PWM)
SpeedPin = 37   # Højre forreste hjul
SpeedPin1 = 10  # Venstre forreste hjul
SpeedPin2 = 28  # Højre bagerste hjul (tilføjet)
SpeedPin3 = 14  # Venstre bagerste hjul (tilføjet)

# Pins til retning
DirectionPin = 32   # Højre forreste
DirectionPin1 = 12  # Venstre forreste
DirectionPin2 = 3   # Højre bagerste
DirectionPin3 = 16  # Venstre bagerste

# Pins til line-followere
linefollower1 = 16
linefollower2 = 18

# Opsætning af GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Ryd tidligere opsætning
GPIO.cleanup()

# Opsætning af pins som output
GPIO.setup(SpeedPin, GPIO.OUT)
GPIO.setup(SpeedPin1, GPIO.OUT)
GPIO.setup(SpeedPin2, GPIO.OUT)  # Ny PWM-pin
GPIO.setup(SpeedPin3, GPIO.OUT)  # Ny PWM-pin

GPIO.setup(DirectionPin, GPIO.OUT)
GPIO.setup(DirectionPin1, GPIO.OUT)
GPIO.setup(DirectionPin2, GPIO.OUT)
GPIO.setup(DirectionPin3, GPIO.OUT)

# Opret PWM-instanser for alle hjul
pi_pwm = GPIO.PWM(SpeedPin, 1000)
pi_pwm1 = GPIO.PWM(SpeedPin1, 1000)
pi_pwm2 = GPIO.PWM(SpeedPin2, 1000)  # Ny PWM-instans
pi_pwm3 = GPIO.PWM(SpeedPin3, 1000)  # Ny PWM-instans

# Start PWM for alle hjul
pi_pwm.start(0)
pi_pwm1.start(0)
pi_pwm2.start(0)
pi_pwm3.start(0)

# Funktion til at få alle hjul til at køre fremad
def koer():
    GPIO.output(DirectionPin, True)   # Højre forreste hjul frem
    GPIO.output(DirectionPin1, True)  # Venstre forreste hjul frem
    GPIO.output(DirectionPin2, True)  # Højre bagerste hjul frem
    GPIO.output(DirectionPin3, True)  # Venstre bagerste hjul frem

    # Ændre duty cycle for alle fire hjul
    pi_pwm.ChangeDutyCycle(95)
    pi_pwm1.ChangeDutyCycle(95)
    pi_pwm2.ChangeDutyCycle(95)  # Tilføjet for bagerste hjul
    pi_pwm3.ChangeDutyCycle(95)  # Tilføjet for bagerste hjul

# Funktion til venstresving (to højre hjul fremad)
def dven():
    GPIO.output(DirectionPin, False)
    GPIO.output(DirectionPin1, False)
    GPIO.output(DirectionPin2, True)
    GPIO.output(DirectionPin3, True)

    pi_pwm.ChangeDutyCycle(80)
    pi_pwm1.ChangeDutyCycle(80)
    pi_pwm2.ChangeDutyCycle(80)  # Tilføjet for bagerste hjul
    pi_pwm3.ChangeDutyCycle(80)  # Tilføjet for bagerste hjul
    sleep(0.05)

# Funktion til højresving (to venstre hjul fremad)
def dhoej():
    GPIO.output(DirectionPin, True)
    GPIO.output(DirectionPin1, True)
    GPIO.output(DirectionPin2, False)
    GPIO.output(DirectionPin3, False)

    pi_pwm.ChangeDutyCycle(80)
    pi_pwm1.ChangeDutyCycle(80)
    pi_pwm2.ChangeDutyCycle(80)  # Tilføjet for bagerste hjul
    pi_pwm3.ChangeDutyCycle(80)  # Tilføjet for bagerste hjul
    sleep(0.05)

# Opsætning af line-follower sensorer
GPIO.setup(linefollower1, GPIO.IN)
GPIO.setup(linefollower2, GPIO.IN)

# Hovedprogram til at styre kørslen
try:
    while True:
        Venstre = int(GPIO.input(linefollower1))
        print("Venstre sensor:", Venstre)
        Højre = int(GPIO.input(linefollower2))
        print("Højre sensor:", Højre)

        if (Venstre == 1 and Højre == 1):
            koer()  # Begge hjul fremad
        elif (Venstre == 1 and Højre == 0):
            dhoej()  # Højresving
        elif (Venstre == 0 and Højre == 0):
            koer()  # Kør lige frem
        elif (Venstre == 0 and Højre == 1):
            dven()  # Venstresving
        else:
            koer()  # Standard tilstand
            print("FEJL")
except KeyboardInterrupt:
    pass

# Ryd opsætning, når programmet stopper
GPIO.cleanup()
