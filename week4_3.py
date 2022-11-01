import RPi.GPIO as GPIO #

import time

import random  # 랜덤함수지정


GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)

GPIO.setup(38,GPIO.OUT)

GPIO.setup(37,GPIO.OUT)

GPIO.setup(36,GPIO.OUT)

for i in range(10):    #10번 반복
   
 arrs = [40,38,37,36]  # 배열 

 list = random.choice(arrs)

 GPIO.output(list,True)   # random choice LED 점등 

 time.sleep(0.5)
 
 GPIO.output(list,False)  # LED 소등

 time.sleep(0.5)
