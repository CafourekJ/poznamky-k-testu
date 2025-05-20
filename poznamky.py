# Definice seznamu jídel
jidla = ["řízek,hranolky,svíčková"]
# Výpis prvního jídla
print(jidla[0])
# Výpis třetího jídla (dvakrát)
print(jidla[2])
print(jidla[2])

# Definice seznamu známek z matematiky
matika = [4, 1, 3, 1, 2, 3, 5]
# Výpočet součtu známek
soucet = sum(matika)
print(soucet)
# Výpočet počtu známek
pocetZnamek = len(matika)
print(pocetZnamek)
print("")
# Výpis všech známek pomocí cyklu
for znamky in matika:
    print(znamky)

# Definice seznamu zvířat
zvire = ["pes,kočka,slon,žirafa"]
# Výpis druhého a čtvrtého zvířete
print(zvire[1])
print(zvire[3])

# Definice seznamu čísel
cisla = [20, 24, 11]
# Přidání čísla 20 na konec seznamu
cisla.append(20)
print(cisla)

# Definice seznamu filmů
filmy = ["Vyšehrad,Kokosy na sněhu,Shrek"]
# Výpis všech filmů pomocí cyklu
for i in filmy:
    print(i)

# Definice dalšího seznamu čísel
cislo = [21, 3, 16]
# Změna druhého čísla v seznamu na 999
cisla[1] = 999
print(cislo)

# Definice seznamu náhodných čísel
randomCisla = [2, 1, 10, 56, 43]
# Výpočet součtu čísel v seznamu
soucetCisel = sum(randomCisla)
print(soucetCisel)

# Definice seznamu pole
pole = [20, 52, 54, 24, 44]
# Výpočet počtu prvků v seznamu
pocetPoli = len(pole)
print(pocetPoli)

# Definice seznamu známek
Znamky = [5, 2, 1, 2, 3, 4, 2]
# Výpočet součtu známek
soucet = sum(Znamky)
# Výpočet počtu známek
pocet = len(Znamky)
# Výpočet průměru známek
prumer = soucet / pocet
print(prumer)

# Definice seznamu ovoce
ovoce = ["jablko,banán,mandarinka,meloun,hruška"]
# Kontrola, zda je v seznamu "banán"
if "banán" in ovoce:
    print("Banán tam je!")
else:
    print("Banán tam není😪.")

# Definice seznamu čísel
mojeCisla = [6, 16, 2, 0, 10, 98]
# Počítadlo čísel větších než 10
pocet_vetsi_nez_10 = 0
# Cyklus pro kontrolu každého čísla
for cislo in cisla:
    if cislo > 10:
        pocet_vetsi_nez_10 += 1
# Výpis počtu čísel větších než 10
print("Počet čísel větších než 10: ", pocet_vetsi_nez_10)