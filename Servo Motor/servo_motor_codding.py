import machine as mc
#from kullanmak yerine 

#pin=mc.Pin(4)

pin=machine.Pin(4)
#freq hertz olarak algılar 
#1000 ms 50hz gönder buda 20ms ye düşsün 
servo=mc.PWM(pin,freq=50)

while True:
  servo.duty(100)
  print("100 derece servo motor döndü")
