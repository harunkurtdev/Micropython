import machine

class mpu6050():

    def __init__(self,i2c,addr=0x68):
        self.iic=i2c
        self.addr=addr
        self.iic.start()
        self.iic.writeto(self.addr,bytearray([107,0]))
        self.iic.stop()

    def okuma_bit_sutun(self):
        self.iic.start()
        deger=self.iic.readfrom_mem(self.addr,0x3B,14)
        self.iic.stop()
        return a

    def byte_kayirma(self,birincibyte,ikincibyte):
        return birincibyte<<8|ikincibyte

    def get_degerler(self):
        sutunlar= self.okuma_bit_sutun()
        deger={}
        deger["ivmeX"]= self.byte_kayirma(sutunlar[0],sutunlar[1])
        deger["ivmeY"]=self.byte_kayirma(sutunlar[2],sutunlar[3])
        deger["ivmeZ"]=self.byte_kayirma(sutunlar[4],sutunlar[5])
        deger["Sicaklik"]=(self.byte_kayirma(sutunlar[6],sutunlar[7]))/340.00+36.53
        deger["gyroX"]=self.byte_kayirma(sutunlar[8],sutunlar[9])
        deger["gyroY"]=self.byte_kayirma(sutunlar[10],sutunlar[11])
        deger["gyroZ"]=self.byte_kayirma(sutunlar[12],sutunlar[13])

        return deger
    # -32768 ile 32767 #int16

    def test_fonksiyonu(self):
        from time import sleep
        while True:
            print(self.get_degerler())
            sleep(0.5)
