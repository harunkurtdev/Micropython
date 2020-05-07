
import time
from machine import Pin

class MesafeSensor:

    
    def  __init__(self,trig_pin,echo_pin,echo_timeout=500*2*30):
        "consturctor"
        self.trig_pin=Pin(trig_pin,mode=Pin.OUT,pull=None)
        self.trig_pin.value(0)
        self.echo_pin=Pin(echo_pin,mode=Pin.IN,pull=None)
        self.echo_timeout=echo_timeout

    def darbe_bekleme(self):
        "ses gönderme 0 yaptık"
        self.trig_pin.value(0)
        "5 micro saniye beklendi"
        time.sleep_us(5)
        "ses gönderme aktif"
        self.trig_pin.value(1)
        "10 micro saniye beklendi"
        time.sleep_us(10)
        "ses gönderme kapatıldı"
        self.trig_pin.value(0)
        "zaman aşmı olmasın diye hata yakalama yapıldı"
        try:
            "machine arduinp da pulseIN fonksiuonı olarak kullanıldı"
            darbe_zamani=machine.time_pulse_us(self.echo_pin,1,self.echo_timeout)
            return darbe_zamani
        except OSError as ex:
            "zaman aşımı var ise hata yı bastır"
            if ex.args[0]==110:
                raise OSError("Hata oluştu")
            raise ex

    def mesafe_mm(self):

        mesafe=self.darbe_bekleme()
        
        mm= mesafe*100//582
        return mm

    def mesafe_cm(self):
        
        mesafe=self.darbe_bekleme()

        cm=mesafe/58.2

        return cm



    