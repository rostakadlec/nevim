#Kadlec, Jiřinec

print("zadej 3 jidla")
jidlo1 = input("zadejte jidlo 1 ")
jidlo2 = input("zadejte jidlo 2 ")
jidlo3 = input("zadejte jidlo 3 ")
 
print("zadej ke každému jidlu pocet kalorií ")
kalorie1 = int(input("zadej pocet kalorií k jidlu 1 "))
kalorie2 = int(input("zadej pocet kalorií k jidlu 2 "))
kalorie3 = int(input("zadej pocet kalorií k jidlu 3 "))
součet = (kalorie1 + kalorie2 + kalorie3)
 

akt1 = input("cos delal")
cas1 = int(input("jak dlouho jsi to delal"))
akt2 = input("cos delal")
cas2 = int(input("jak dlouho jsi to delal"))
celkovy_vydej = (cas1 * 5) + (cas2 * 5)

print ("snedl jsi"(součet))
print(f"celkovy vydej je {celkovy_vydej}")
if součet < celkovy_vydej:
    print("nedostatek kalorií")
elif součet > celkovy_vydej:
    print("přebytek kalorií")
else:
    print("50/50")
