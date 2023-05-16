class Dog:

    def __init__(self, name: str, age : int, coat_color: str):
        self.name = name
        self.age = age
        self.coat_color = coat_color

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")

class Car:

    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage

    def drive(self, driven):
        self.mileage += driven

    def __str__(self):
        return (f"The {self.color} car has {self.mileage:,} miles.")

blue_car = Car("blue", 20000)
red_car = Car("red", 30000)
new_car = Car("black", 0)

new_car.drive(100)
print(blue_car)
print(red_car)
print(new_car)