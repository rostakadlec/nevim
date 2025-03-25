cis1 = int(input("zadej prvni cislo"))
cis2 = int(input("zadej druhy cislo"))

opakovat = "ano"
while opakovat == "ano":
    operace = input("co chces za operaci")
if operace == "scitani":
    print (cis1 + cis2)
elif operace == "odecitani":
    print (cis1 - cis2)
elif operace == "nasobeni":
    print (cis1 * cis2)
elif operace == "deleni":
    print (cis1 / cis2)
else:
    print ("zadej neco normalniho")

opakovat = input("chces program opakovat?")