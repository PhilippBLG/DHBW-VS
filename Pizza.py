naturale = ["Naturale", "Oregano"]
margherita = ["Margherita", "Mozarella", "Tomaten", "Basilikum"]
napoli = ["Napoli", "Mozarella", "Tomate", "Sardellen", "Oliven"]
funghi = ["Mozarella", "Tomate", "Champignons"]

pizzas = [naturale, margherita, napoli, funghi]

print(pizzas)

for pizza in pizzas:
    print("Die Pizza " + "".join(pizza[:1]) + " wird belegt mit " + ", ".join(pizza[1:]))
