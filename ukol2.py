cislo1 = float(input("Zadejte první desetinné číslo: "))
cislo2 = float(input("Zadejte druhé desetinné číslo: "))
 
soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2
if cislo2 != 0:
    podil = cislo1 / cislo2
else:
    podil = None
 
print(f"Součet: {soucet:.2f}")
print(f"Rozdíl: {rozdil:.2f}")
print(f"Součin: {soucin:.2f}")
if podil is not None:
    print(f"Podíl: {podil:.2f}")
else:
    print("Podíl: Nelze dělit nulou")