import Rpi.GPIO
from time import sleep

class MotorGroup():
    def __init__(self,en,in1,in2):
        # class attributes
        self.en = en
        self.in1 = in1
        self.in2 = in2
        # pin Setup
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)

        # pwm settings
        self.pwm = GPIO.PWM(self.en,100)
        self.pwm.start(0)
    def forward():
        pass

    def backward():
        pass

    def stop():
        pass



    if __name__ == "__main__":
        pass

