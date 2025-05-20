zvirata = []
pocet_zvirat = int(input("Kolik chcete zvířat: "))
for i in range (pocet_zvirat):
    zadej_zvire = input("Zadejte zvíře: ")
    zvirata.append(zadej_zvire)
if "tapír" in zvirata or "mýval" in zvirata or "kočka" in zvirata:
    print("Super")
else:
    print("Nic moc")