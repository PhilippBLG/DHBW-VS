favourite_cities = {"Guido": "Austin",
                    "Sarah": "Dallas",
                    "Barry": "Tuscon",
                    "Rachel": "Reno",
                    "Tim": "Portland"}

h = hash("Guido")
i = h % len(favourite_cities)
perturb = h
n = len(favourite_cities)
while favourite_cities[i] != -1:
    i = (5*i + perturb + 1) % n
    perturb = perturb // 32