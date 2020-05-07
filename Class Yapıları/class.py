   "classımız"
class Kullanici:

    "class a giriş yapılmışsa ilk olarak buraya gir. ve gererkli parametreleri al ve yap"
    def __init__(self,kullaniciAdi,kullanSoyadi):
        self.kullaniciAdi=str(kullaniciAdi)
        self.kullaniciSoyadi=str(kullanSoyadi)
        print(self.kullaniciAdi+" ben")

    def kullaniSoyadi(self):
        print(self.kullaniciAdi+" "+self.kullaniciSoyadi)
    
    def degistir(self):
        self.kullaniciSoyadi="değiştirildi."
    "-------------------Class içerisinde fonksiyonların kendi aralarında döndzerilmesi.--------------------"
    def fonkdonen(self):
        self.fonkdonendegisken="fonk degisken"

        return self.fonkyazdir()
    
    def fonkyazdir(self):
        print(self.fonkdonendegisken)

    def fonk(self):

        return self.fonkdonen()


"eğer ki bu safya main e eşit ise gerekli komutları yerine getir"
if __name__ == "__main__":
    print("İlk igirş")
    kullanici=Kullanici(kullaniciAdi="Harun",kullanSoyadi="KURT")
    kullanici.kullaniSoyadi()
    kullanici.degistir()
    kullanici.kullaniSoyadi()

    kullanici.fonk()