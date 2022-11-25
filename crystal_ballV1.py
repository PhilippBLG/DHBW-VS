import random

question = input("Frag die Magische Miesmuschel: \n")
while question != "":
    answers = ["Das Beste wäre es, wenn Du die Beine hochlegst",
               "Vorteilhaft wäre es, wenn Du Dein Leben chillst",
               "Es ist ratsam, dass Du Dein Glück suchst",
               "Deinem Karma würde es gut tun, wenn Du öfter Urlaub machst",
               "Tue alles dafür, um Erfolg zu haben",
               "Glaube daran, dass Du Dein Leben meisterst",
               "Es gelingt sicher, wenn Du härter arbeitest",
               "Es ist sehr wahrscheinlich, wenn Du Deinen Arbeitsstil änderst",
               "Es kann nicht gelingen, wenn Du nichts änderst",
               "Es gelingt nicht, wenn Du nicht flexibler wirst",
               "Finde Deine Mitte, damit Du ruhiger wirst",
               "Glaube an Dich, damit Du Deinen Weg machst"]
    print(answers[random.randint(0, 11)] + "\n")
    question = input("Frag die Magische Miesmuschel: \n")
print("Ich hoffe ich konnte dir weiterhelfen.")
