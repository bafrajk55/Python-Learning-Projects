x = float (input ("Birinci Sayiyi Giriniz: "))
isaret = input("Bir Isaret Seciniz (+ , - , * , / )")
y = float (input("Ikinci Sayiyi Giriniz: "))

if isaret == "+" :
    z = x + y 

elif isaret == "-" :
    z = x - y

elif isaret == "/" :
    if y == 0:
        z = "Sifira bolunemez"
    else:
        z = x / y 

elif isaret == "*" :
    z= x * y 

else :
    print ("Isareti Dogru Seciniz") 

print ("Sonuc:", z)