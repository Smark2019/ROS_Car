import RPi.GPIO as GPIO
from time import sleep

class MotorGroup():
    def __init__(self,en,in1,in2):
        # class attributes
        self.en = en
        self.in1 = in1
        self.in2 = in2
        # pin Setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)

        # pwm settings
        self.pwm = GPIO.PWM(self.en,100)
        self.pwm.start(0)

    def forward(self, pwm = 50):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        self.pwm.ChangeDutyCycle(pwm)

    def backward(self,pwm = 50):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        self.pwm.ChangeDutyCycle(pwm)

    def stop(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)





if __name__ == "__main__":

    motorGroup_left = MotorGroup(22,4,27)
    motorGroup_left.forward()
    sleep(5)
    motorGroup_left.stop()
   # motorGroup_right = MotorGroup(22,4,27)

