try :
  import usocket as socket
except :
  import socket
#sockjet bağalntısı için
from machine import Pin
import network # network 

import esp #esp32 veyahut esp8266 için
esp.osdebug(None)# her ikisini kullanmak istoyorsak none giriceğiz 

import gc #gc den hafıza birimini silmek istiyorsak
gc.collect() 

ssid="TTNET_HUAWEI_9207" #wifiadi
password="80D75FD3A8"#wifi şifersi


station=network.WLAN(network.STA_IF)#istasyon kurmak için 

station.active(True)#istasyonu aktif etmek 
station.connect(ssid,password)#wifi ye bağlantı yap

#wifi ye bağlanmamıs gerekli işleri yap
while station.isconnected() == False:
  print("Bağlantı Tamamlanmadı")
  pass

print("Bağlantı Tamamlandı")
print(station.ifconfig())#lçocal de ki ip yi çek

#çıkış tanımlıyoruz
led=Pin(2,Pin.OUT)

#fonskiyon için web 
def web_page():
    #ledin durumuna göre text yazısını değiştir
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  #html sayfası
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

#socket ile dinleme yapmak için
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while True:
  conn, addr = s.accept() #response ve request yapılan bildirim aynı zamanda yapılan ip  bildirimi
  print('Got a connection from %s' % str(addr)) #yapılan request göster
  request = conn.recv(1024) # request
  request = str(request) 
  print('Content = %s' % request) #request i göster
  led_on = request.find('/?led=on') # yapılan request i dinle
  led_off = request.find('/?led=off')
  if led_on == 6: 
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page() #wb sayfasını return et
  conn.send('HTTP/1.1 200 OK\n') 
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response) #burada da bir return verimizi 
  conn.close() #burada socket bağlantısını kapatıyoruz 