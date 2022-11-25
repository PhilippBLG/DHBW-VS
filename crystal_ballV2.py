import random

question = input("Frag die Magische Miesmuschel: \n")
while question != "":
    if "glück" in question.lower():
        answers1 = ["Das beste wäre es ",
                    "Vorteilhaft wäre es ",
                    "Es wäre ratsam "]
        answers2 = ["wenn Du die Beine hochlegst und auf dein Glück wartest",
                    "wenn Du Dein Leben chillst und auf dein Glück wartest",
                    "wenn Du Dein Glück suchst"]
        print(answers1[random.randint(0, 2)] + answers2[random.randint(0, 2)] + "\n")
    elif "erfolg" in question.lower():
        answers1 = ["Das beste wäre es ",
                    "Vorteilhaft wäre es ",
                    "Es wäre ratsam "]
        answers2 = ["wenn Du die Beine hochlegst und auf dein Erfolg wartest",
                    "wenn Du Dein Leben chillst und auf dein Erfolg wartest",
                    "wenn Du Dein Erfolg suchst"]
        print(answers1[random.randint(0, 2)] + answers2[random.randint(0, 2)] + "\n")
    else:
        answers1 = ["Das beste wäre es ",
                    "Vorteilhaft wäre es ",
                    "Es wäre ratsam "]
        answers2 = ["wenn Du die Beine hochlegst",
                    "wenn Du Dein Leben chillst",
                    "wenn Du Dein Glück suchst"]
        print(answers1[random.randint(0, 2)] + answers2[random.randint(0, 2)] + "\n")
    question = input("Frag die Magische Miesmuschel: \n")
print("Ich hoffe ich konnte dir weiterhelfen.")
