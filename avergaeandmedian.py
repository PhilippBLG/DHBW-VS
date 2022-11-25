import simplestats
user_number = input("Add to list: ")
lst = []
while user_number != "":
    lst.append(float(user_number))
    user_number = input("Add to list: ")
total = simplestats.total(lst)
mean = simplestats.mean(lst)
median = simplestats.median(lst)
print(f"Der Total ist {total}"
      f"\nDer Mittelwert ist {mean:.2f}"
      f"\nDer Median ist {median:.2f}")
print("Danke fürs benutzen unseres Taschenrechners")
