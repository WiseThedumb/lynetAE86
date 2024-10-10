import RPi.GPIO as GPIO
import time

# 设置GPIO模式
GPIO.setmode(GPIO.BCM)

# 定义GPIO引脚
motor_pins = {
    'left_front': {'dir': 32, 'ena': 37},
    'right_front': {'dir': 3, 'ena': 10},
    'left_rear': {'dir': 16, 'ena': 14},
    'right_rear': {'dir': 12, 'ena': 28}
}

# 设置GPIO引脚为输出模式
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
set_motor('left_front', 'forward', 50)
set_motor('right_front', 'forward', 50)
set_motor('left_rear', 'forward', 50)
set_motor('right_rear', 'forward', 50)

time.sleep(2)

# 示例：后退，速度75%
set_motor('left_front', 'backward', 75)
set_motor('right_front', 'backward', 75)
set_motor('left_rear', 'backward', 75)
set_motor('right_rear', 'backward', 75)

time.sleep(2)

# 停止电机
for motor in motor_pins.keys():
    pwm[motor].ChangeDutyCycle(0)

GPIO.cleanup()
