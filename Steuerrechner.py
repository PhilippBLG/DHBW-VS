print("***** Berechnung der Mehrwertsteuer *****")

while True:
    try:
        preis = input("Preis: ")
        if not preis:
            print("Auf wiedersehen!")
            break
        steuersatz = input("Steuersatz: ")
        if not steuersatz:
            print("Auf wiedersehen!")
            break
        steuer = float(preis) * float(steuersatz) / 100
        gesamtpreis = float(preis) + float(steuer)
        print("Steuersatz: ", steuersatz, "%")
        print("Steuern: ", steuer, "EUR")
        print("Gesamtpreis: ", gesamtpreis, "EUR")
        print(20*"*")
    except ValueError:
        print("Bitte geben Sie eine Zahl ein! Beispiel: 100")
        print(f"Preis: {preis}")
        print(f"Steuersatz: {steuersatz}")
