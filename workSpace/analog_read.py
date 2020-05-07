from machine import Pin,ADC
from time import sleep
"""
pot = ADC(0)#esp8266

#esp8266 ya göre çalıştık

"""

"""
Bit kısmı okunan değeri map fonksiyonuna göre çevirtmek
için yapılır
"""
"""
ADC.width(ADC.WIDTH_9BIT)# 0 ile 511 arasında 2^9
ADC.width(ADC.WIDTH_10IT)# 0 ile 1023 arasında okuyabildiğmiz veri
ADC.width(ADC.WIDTH_11BIT)#0 ile 2047 arasında""" 
ADC.width(ADC.WIDTH_12BIT)#0 ile 4095 

" Esp32 ye göre yapıyoruz"

pot = ADC(Pin(34))
"""
pot.atten(ADC.ATTN_0DB) #1.2V analog değer okuyor
pot.atten(ADC.ATTN_2_5DB)#1.5v değeri karşılıyor 
pot.atten(ADC.ATTN_6DB) #2.0V"""
pot.atten(ADC.ATTN_11DB)# 3.3v göre 




while True :
  pot_deger=pot.read()
  print(str(pot_deger)+" okunan potasiyometre değeri")
  sleep(0.1)
