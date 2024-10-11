import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

motor_pins = {
    'h_front': {'dir': 12, 'ena': 26}, #højre forreste
    'v_b': {'dir': 2, 'ena': 15},
    'h_b': {'dir': 23, 'ena': 24},
    'v_f': {'dir': 4, 'ena': 1},
}
sensor_pins = {
    'left': 5,
    'right': 6
}
for sensor in sensor_pins.values():
    GPIO.setup(sensor, GPIO.IN)
for motor in motor_pins.values():
    GPIO.setup(motor['dir'], GPIO.OUT)
    GPIO.setup(motor['ena'], GPIO.OUT)

pwm = {}
for motor, pins in motor_pins.items():
    pwm[motor] = GPIO.PWM(pins['ena'], 100)  # 频率设置为100Hz
    pwm[motor].start(0)  # 初始占空比为0

# 定义电机控制函数
def set_motor(motor, direction, speed):
    if direction == 'forward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.HIGH)
    elif direction == 'backward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.LOW)
    
    pwm[motor].ChangeDutyCycle(speed)



def set_motor(motor, direction, speed):
    if direction == 'forward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.HIGH)
    elif direction == 'backward':
        GPIO.output(motor_pins[motor]['dir'], GPIO.LOW)
    
    pwm[motor].ChangeDutyCycle(speed)
try:
    while True:
        left_sensor = GPIO.input(sensor_pins['left'])
        right_sensor = GPIO.input(sensor_pins['right'])

        if left_sensor == 0 and right_sensor == 0:
            # 前进
            set_motor('left_front', 'forward', 15)
            set_motor('right_front', 'forward', 15)
            set_motor('left_rear', 'forward', 15)
            set_motor('right_rear', 'forward', 15)
        elif left_sensor == 1 and right_sensor == 0:
            set_motor('left_front', 'forward', 15)
            set_motor('right_front', 'backward', 15)
            set_motor('left_rear', 'forward', 15)
            set_motor('right_rear', 'backward', 15)
        elif left_sensor == 0 and right_sensor == 1:
            # 向左转
            set_motor('left_front', 'backward', 15)
            set_motor('right_front', 'forward', 15)
            set_motor('left_rear', 'backward', 15)
            set_motor('right_rear', 'forward', 15)
        else:
            # 停止
            for motor in motor_pins.keys():
                pwm[motor].ChangeDutyCycle(0)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
