import RPi.GPIO as GPIO
import time
#핀번호
PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

SW1 =5
SW2 = 6
SW3 = 13
SW4 = 19


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA,GPIO.OUT) #pwma설정
GPIO.setup(AIN1,GPIO.OUT) #왼쪽앞바퀴 설정
GPIO.setup(AIN2,GPIO.OUT) #왼쪽 뒷바퀴설정
GPIO.setup(PWMB,GPIO.OUT) #pwmb설정
GPIO.setup(BIN1,GPIO.OUT) #오른쪽앞바퀴설정
GPIO.setup(BIN2,GPIO.OUT) #오른쪽뒷바퀴설정
GPIO.setup(SW1, GPIO.IN) #스위치설정 아래 동일
GPIO.setup(SW2, GPIO.IN) 
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #스위치제어문
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

try:
    while True:
        value = GPIO.input(SW1) #SW1번 앞으로 이동할때 코드 
        if value == True :
            print("SW1 input") #스위치 눌렸을때 출력되는 문구 
            L_Motor.ChangeDutyCycle(100) #속도
            R_Motor.ChangeDutyCycle(100)
            GPIO.output(AIN1,0) #왼쪽앞모터
            GPIO.output(AIN2,1) #왼쪽뒤모터
            GPIO.output(BIN1,0) #오른쪽앞모터
            GPIO.output(BIN2,1) #오른쪽뒤모터
            time.sleep(1.0)
            L_Motor.ChangeDutyCycle(0) #속도
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
        
        value1 = GPIO.input(SW2) #SW2번 오른쪽으로 이동할때 코드 
        if value1 == True :
            L_Motor.ChangeDutyCycle(100) #속도
            R_Motor.ChangeDutyCycle(100)
            GPIO.output(AIN1,0) #왼쪽앞모터
            GPIO.output(AIN2,1) #왼쪽뒤모터
            GPIO.output(BIN1,1) #오른쪽앞모터
            GPIO.output(BIN2,0) #오른쪽뒤모터 
            time.sleep(1.0)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
            print("SW2 input") #스위치 눌렸을때 출력되는 문구 
        value2 = GPIO.input(SW3) #SW3번 왼쪽으로 이동할때 코드 
        if value2 == True :
            L_Motor.ChangeDutyCycle(100) #속도
            R_Motor.ChangeDutyCycle(100)
            GPIO.output(AIN1,1) #왼쪽앞모터
            GPIO.output(AIN2,0) #왼쪽뒤모터
            GPIO.output(BIN1,0) #오른쪽앞모터
            GPIO.output(BIN2,1) #오른쪽뒤모터
            time.sleep(1.0) 
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
            print("SW3 input")
        value3 = GPIO.input(SW4) #SW4번 뒤쪽으로 이동할때 코드 
        if value3 == True :
            L_Motor.ChangeDutyCycle(100) #속도
            R_Motor.ChangeDutyCycle(100)
            GPIO.output(AIN1,1) #왼쪽앞모터
            GPIO.output(AIN2,0) #왼쪽뒤모터
            GPIO.output(BIN1,1) #오른쪽앞모터
            GPIO.output(BIN2,0) #오른쪽뒷모터 
            time.sleep(1.0)
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)
            time.sleep(1.0)
            print("SW4 input")        
            time.sleep(1.0)
            
except KeyboardInterrupt:
    pass
GPIO.cleanup()


