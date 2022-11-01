import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)

GPIO.setup(38,GPIO.OUT)

GPIO.setup(37,GPIO.OUT)

GPIO.setup(36,GPIO.OUT)


try :

 while(True):

    GPIO.output(40,True)

    time.sleep(1)

    GPIO.output(40,False)

    time.sleep(1)

    GPIO.output(38,True)

    time.sleep(1)

    GPIO.output(38,False)

    time.sleep(1)

    GPIO.output(37,True)

    time.sleep(1)

    GPIO.output(37,False)

    time.sleep(1)

    GPIO.output(36,True)

    time.sleep(1)

    GPIO.output(36,False)

    time.sleep(1)

except:  # 위 TRY문 끝나고 난 후 EXCEPT로 옮겨져서 RESET 하는...

 GPIO.cleanup() # 초기화 (대청소) 