import time

start_time = time.time()
pizzas = {"margherita": "Tomate, Mozzarella, Basilikum",
          "naturale": "Oregano",
          "fungi": "Tomate, Mozzarella, Champignons"}

for pizza, zutaten in pizzas.items():
    print(f"Pizza {pizza.title()} mit {zutaten}")

print("--- %s seconds ---" % (time.time() - start_time))
print("")

start_time = time.time()
pizzas = {"margherita": "Tomate, Mozzarella, Basilikum",
          "naturale": "Oregano",
          "fungi": "Tomate, Mozzarella, Champignons"}

for pizza in pizzas:
    print(f"Pizza {pizza.title()} mit {pizzas[pizza]}")

print("--- %s seconds ---" % (time.time() - start_time))
print("")

start_time = time.time()
pizzas = {"margherita": {"Zutaten": "Tomate, Mozzarella, Basilikum"},
          "naturale": {"Zutaten": "Oregano"},
          "fungi": {"Zutaten": "Tomate, Mozzarella, Champignons"}}

for pizza in pizzas:
    print(f"Pizza {pizza.title()} mit {pizzas[pizza]['Zutaten']}")

print("--- %s seconds ---" % (time.time() - start_time))
print("")

start_time = time.time()
pizzas = {"margherita": ["Tomate", "Mozzarella", "Basilikum"],
          "naturale": ["Oregano"],
          "fungi": ["Tomate", "Mozzarella", "Champignons"]}

for pizza in pizzas:
    print(f"Pizza {pizza.title()} mit " + " ".join(pizzas[pizza]))

print("--- %s seconds ---" % (time.time() - start_time))
