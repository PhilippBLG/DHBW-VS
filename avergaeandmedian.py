import simplestats
user_number = input("Add to list: ")
lst = []
while True:
    try:
        while user_number != "":
            lst.append(float(user_number))
            user_number = input("Add to list: ")
        print(f"Deine Liste ist {lst}"
              f"\nDer Total ist {simplestats.total(lst)}"
              f"\nDer Mittelwert ist {simplestats.mean(lst):.2f}"
              f"\nDer Median ist {simplestats.median(lst):.2f}")
        lst.clear()
        user_number = input("Add to list: ")
    except ValueError:
        print("Invalid input!")
        print("Do you want to quit? (y/n)")
        user_input = input()
        if user_input == "y":
            break
        else:
            print("Clear the list or add to the current? (y/n)")
            user_input = input()
            if user_input == "y":
                lst.clear()
                user_number = input("Add to list: ")
            else:
                user_number = input("Add to list: ")

print("Danke fürs benutzen unseres Taschenrechners")
