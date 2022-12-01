user_input = input("Enter your age: ")
try:
     age = int(input("Enter your age: "))
     if age < 3 or age > 130:
         print(f"Are you really {age} years old?")
     else:
        print(f"You are {age} years old")
except ValueError:
    print(f"{user_input} is not a number")
except Exception as e:
    print(f"Something went wrong: {e}")
