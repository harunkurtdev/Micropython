
def map(x,in_min,in_max,out_min,out_max):
    return (x-in_min)*(out_max-out_min)/(in_max - in_min)+out_min

while True:
    
    x=int(input("X e bir değer gönderin sonuç alın"))

    maps_giden=map(x,0,1023,0,255)

    print(maps_giden)
