import RPi.GPIO as GPIO
import time

# Brug BCM-nummerering til at referere til GPIO-pins
GPIO.setmode(GPIO.BCM)
#h

# Definer motorens pins (BCM nummerering)
motor_pins = {
    'h_front': {'dir': 18, 'ena': 26},  # Højre forreste - dir=BCM 18 (Physical Pin 12), ena=BCM 26
    'v_b': {'dir': 2, 'ena': 15},       # Venstre bageste - dir=BCM 2 (Physical Pin 3), ena=BCM 15
    'h_b': {'dir': 23, 'ena': 24},      # Højre bageste - dir=BCM 23 (Physical Pin 16), ena=BCM 24
    'v_f': {'dir': 3, 'ena': 1}         # Venstre forreste - dir=BCM 3 (Physical Pin 5), ena=BCM 1
}

# Initialiser motorens pins som output
for motor in motor_pins.values():
    GPIO.setup(motor['dir'], GPIO.OUT)
    GPIO.setup(motor['ena'], GPIO.OUT)

# Opret PWM-objekter for hver motor
pwm = {}
for motor, pins in motor_pins.items():
    pwm[motor] = GPIO.PWM(pins['ena'], 100)  # PWM med 100 Hz frekvens
    pwm[motor].start(0)  # Start PWM med duty cycle 0 (motorerne står stille)

# Funktion til at styre motorerne
def set_motor(motor, direction, speed):
    if direction == 'forward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.HIGH)  # Kør fremad
    elif direction == 'backward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.LOW)   # Kør baglæns
    
    pwm[motor].ChangeDutyCycle(speed)  # Sæt motorhastigheden

# Sæt motorerne til at køre fremad og baglæns
set_motor('h_front', 'forward', 50)  # Højre forreste kører fremad
set_motor('v_b', 'backward', 50)     # Venstre bageste kører baglæns
set_motor('h_b', 'backward', 50)     # Højre bageste kører baglæns
set_motor('v_f', 'forward', 50)      # Venstre forreste kører fremad

time.sleep(20)  # Kør i 20 sekunder

# Skift retning for alle motorer og øg hastigheden
set_motor('h_front', 'backward', 75)  # Højre forreste kører baglæns
set_motor('v_b', 'backward', 75)      # Venstre bageste kører baglæns
set_motor('h_b', 'backward', 75)      # Højre bageste kører baglæns
set_motor('v_f', 'backward', 75)      # Venstre forreste kører baglæns

time.sleep(2)  # Kør i 2 sekunder

# Stop alle motorer ved at sætte duty cycle til 0
for motor in motor_pins.keys():
    pwm[motor].ChangeDutyCycle(0)

# Ryd op efter brug
GPIO.cleanup()

#lalal
