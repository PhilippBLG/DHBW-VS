class CrewMember:

    def __init__(self, name: str, function: str):
        self.name = name
        self.function = function

    def introduce(self):
        print(self.name + ": " + self.function)


kirk = CrewMember("James T. Kirk", "Captain")
spock = CrewMember("S'chn T'gai Spock", "Commander")
bones = CrewMember("Leonard McCoy", "Lieutenant Commander")

kirk.introduce()
