"""Represents a bowl of ice cream.

Authors:
    John Doe <mail@johndoe.org>
"""


class Scoop:
    """ Represents a single scoop of ice cream."""
    def __init__(self, flavour):
        """ Initialize.

        Args:
            flavour (str): Flavour of ice cream (e. g. "Vanilla").

        """
        self.flavour = flavour

    def __str__(self):
        return f"Scoop with flavour '{self.flavour}'"


class Bowl:
    """ A bowl of ice cream scoops. """
    def __init__(self):
        self.bowl = []
        self.scoop_list = []

    def __str__(self):
        scoops_str = '\n'.join(str(scoop) for scoop in self.bowl)
        return f"Bowl contains:\n{scoops_str}"

    def add_scoops(self, scoops):
        """ Add scoops to bowl.

        Args:
            scoops (list of Scoop): scoops to be added.

        """
        for scoop in scoops:
            self.scoop_list.append(str(scoop))
        self.bowl.extend(scoops)


# Test code
if __name__ == "__main__":
    s1 = Scoop("Vanilla")
    s2 = Scoop("Chocolate")
    s3 = Scoop("Strawberry")
    scoops = [s1, s2, s3]
    for s in scoops:
        print(s)

    b = Bowl()
    b.add_scoops([s1, s2])
    b.add_scoops([s3])
    b.add_scoops([Scoop("Raspberry")])
    print(b)
