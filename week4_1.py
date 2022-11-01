import RPi.GPIO as GPIO # GPIO 라이브러리 버전 출력

import time 

GPIO.setmode(GPIO.BOARD) # BOARD의 핀번호로 설정

GPIO.setup(40,GPIO.OUT) # 자동차 판에있는 번호가 아닌 배정되어있는 핀번호

GPIO.setup(38,GPIO.OUT) # 위와동일

GPIO.setup(37,GPIO.OUT) # "

GPIO.setup(36,GPIO.OUT) # "


while(True):  #반복문

    GPIO.output(40,True)

    time.sleep(1)                     # 40번 ON, 1초 대기 

    GPIO.output(40,False)

    time.sleep(1)                    # 40번 OFF, 1초 대기  아래도 똑같음

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