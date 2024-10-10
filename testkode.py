import RPi.GPIO as GPIO
import time

# 设置GPIO模式
GPIO.setmode(GPIO.BCM)

# 定义GPIO引脚
motor_pins = {
    'h_front': {'dir': 12, 'ena': 26}, #højre forreste
    'v_b': {'dir': 2, 'ena': 15},
    'h_b': {'dir': 23, 'ena': 24},
    'v_f': {'dir': 18, 'ena': 1}
}


for motor in motor_pins.values():
    GPIO.setup(motor['dir'], GPIO.OUT)
    GPIO.setup(motor['ena'], GPIO.OUT)

# 初始化PWM
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

# 示例：前进，速度50%
set_motor('h_front', 'backward', 50) #højre forreste
set_motor('v_b', 'backward', 50)
set_motor('h_b', 'forward', 50)
set_motor('v_f', 'backward', 50)

time.sleep(20)

# 示例：后退，速度75%
set_motor('h_front', 'backward', 75)
set_motor('v_b', 'backward', 75)
set_motor('h_b', 'backward', 75)
set_motor('v_f', 'backward', 75)

time.sleep(2)

# 停止电机
for motor in motor_pins.keys():
    pwm[motor].ChangeDutyCycle(0)

GPIO.cleanup()
