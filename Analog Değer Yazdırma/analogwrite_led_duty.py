from machine import Pin,PWM
from time import sleep

frekans=5000 # 1 saniye de ki hertz

led=PWM(Pin(5),5000) #pwm 5 e 

while 1==1:
  for duty_cycle in  range(0,1023):
    led.duty(duty_cycle)
    sleep(0.005)
