class Servo:

    def __init__(self,pin=None,frekans=50,min_ms=600,max_ms=2400,derece=180):
        self.min_ms=min_ms
        self.max_ms=max_ms
        self.frekans=frekans
        self.derece = derece
        self.pin = pin
        self.analog_period = 0
        #analog_period=round((1/self.frekans)*1000)
        #self.pin.set_analog_period(analog_period)

    def write_ms(self,ms):
        w_ms=min(self.max_ms,max(self.min_ms,ms))
        pwm=round(w_ms*1024*self.frekans//1000000)
        print(pwm)
        #self.pin.write_analog(pwm)
        #self.pin.write_digital(0)

    def write_derece(self,derece):
        print(derece)
        derece=derece % 360
        deger=self.max_ms-self.min_ms
        ms=self.min_ms+deger*derece//self.derece
        self.write_ms(ms=ms)
        print(ms)

if __name__ == "__main__":
    Servo().write_derece(120)