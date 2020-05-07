from machine import Pin,ADC
from time import sleep
"""
pot = ADC(0)#esp8266

#esp8266 ya g枚re 莽al谋艧t谋k

"""

"""
Bit k谋sm谋 okunan de臒eri map fonksiyonuna g枚re 莽evirtmek
i莽in yap谋l谋r
"""
"""
ADC.width(ADC.WIDTH_9BIT)# 0 ile 511 aras谋nda 2^9
ADC.width(ADC.WIDTH_10IT)# 0 ile 1023 aras谋nda okuyabildi臒miz veri
ADC.width(ADC.WIDTH_11BIT)#0 ile 2047 aras谋nda""" 
ADC.width(ADC.WIDTH_12BIT)#0 ile 4095 

" Esp32 ye g枚re yap谋yoruz"

pot = ADC(Pin(34))
"""
pot.atten(ADC.ATTN_0DB) #1.2V analog de臒er okuyor
pot.atten(ADC.ATTN_2_5DB)#1.5v de臒eri kar艧谋l谋yor 
pot.atten(ADC.ATTN_6DB) #2.0V"""
pot.atten(ADC.ATTN_11DB)# 3.3v g枚re 

pot.width(ADC.WIDTH_12BIT)#0 ile 4095 


while True :
  pot_deger=pot.read()
  print(str(pot_deger)+" okunan potasiyometre de臒eri")
  sleep(0.1)
