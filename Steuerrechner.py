while True:
    try:
        preis = input("Preis: ")
        steuersatz = input("Steuersatz: ")
        if not preis or not steuersatz:
            break
        steuer = float(preis) * float(steuersatz) / 100
        gesamtpreis = float(preis) + float(steuer)
        print("Steuersatz: ", steuersatz, "%")
        print("Steuern: ", steuer, "EUR")
        print("Gesamtpreis: ", gesamtpreis, "EUR")
    except ValueError:
        print("Bitte geben Sie eine Zahl ein!")
        print("Beispiel: 100")
        print(f"Preis: {preis}")
        print(f"Steuersatz: {steuersatz}")
