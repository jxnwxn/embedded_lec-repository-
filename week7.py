import threading
import serial
import RPi.GPIO as GPIO
import time
#핀번호
PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA,GPIO.OUT) #pwma설정
GPIO.setup(AIN1,GPIO.OUT) #왼쪽앞바퀴 설정
GPIO.setup(AIN2,GPIO.OUT) #왼쪽 뒷바퀴설정
GPIO.setup(PWMB,GPIO.OUT) #pwmb설정
GPIO.setup(BIN1,GPIO.OUT) #오른쪽앞바퀴설정
GPIO.setup(BIN2,GPIO.OUT) #오른쪽뒷바퀴설정


L_Motor = GPIO.PWM(PWMA,500)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)


bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.1)

gData = ""

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def main():
    global gData
    try:
        while True:
            if gData.find("go") >= 0:
                gData = ""
                
                GPIO.output(AIN1,0) #왼쪽앞모터
                GPIO.output(AIN2,1) #왼쪽뒤모터
                GPIO.output(BIN1,0) #오른쪽앞모터
                GPIO.output(BIN2,1) #오른쪽뒤모터   
                L_Motor.ChangeDutyCycle(100) #속도
                R_Motor.ChangeDutyCycle(100)          
                print("ok go")

            elif gData.find("back") >= 0:
                gData = ""
                GPIO.output(AIN1,1) #왼쪽앞모터
                GPIO.output(AIN2,0) #왼쪽뒤모터
                GPIO.output(BIN1,1) #오른쪽앞모터
                GPIO.output(BIN2,0) #오른쪽뒤모터   
                L_Motor.ChangeDutyCycle(100) #속도
                R_Motor.ChangeDutyCycle(100)   
                print("ok back")


            elif gData.find("left") >= 0:
                gData = ""
                GPIO.output(AIN1,1) #왼쪽앞모터
                GPIO.output(AIN2,0) #왼쪽뒤모터
                GPIO.output(BIN1,0) #오른쪽앞모터
                GPIO.output(BIN2,1) #오른쪽뒤모터
                L_Motor.ChangeDutyCycle(100) #속도
                R_Motor.ChangeDutyCycle(100)
                print("ok left")            

            elif gData.find("right") >= 0:
                gData = ""
                GPIO.output(AIN1,0) #왼쪽앞모터
                GPIO.output(AIN2,1) #왼쪽뒤모터
                GPIO.output(BIN1,1) #오른쪽앞모터
                GPIO.output(BIN2,0) #오른쪽뒤모터 
                L_Motor.ChangeDutyCycle(100) #속도
                R_Motor.ChangeDutyCycle(100)
                print("ok right")

            elif gData.find("stop") >= 0:
                gData = ""            
                GPIO.output(AIN1,0) #왼쪽앞모터
                GPIO.output(AIN2,0) #왼쪽뒤모터
                GPIO.output(BIN1,0) #오른쪽앞모터
                GPIO.output(BIN2,0) #오른쪽뒷모터 
                L_Motor.ChangeDutyCycle(0) #속도
                R_Motor.ChangeDutyCycle(0)
                print("ok stop") 

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    task1 = threading.Thread(target = serial_thread)
    task1.start()
    main()
    bleSerial.close()
