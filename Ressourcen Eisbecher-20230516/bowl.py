"""Represents a bowl of ice cream.

Authors:
    John Doe <mail@johndoe.org>
"""


class Scoop:
    """ Represents a single scoop of ice."""
    def __init__(self, flavour):
        """ Initialize.

        Args:
            flavour (str): Flavour of ice cream (e. g. "Vanilla").

        """
        # Your code here
        pass

    def __str__(self):
        # Your code here. Note: returns a string
        pass


class Bowl:
    """ A bowl of ice cream scoops. """
    def __init__(self):
        # Your code here.
        pass

    def __str__(self):
        # Your code here.
        pass

    def add_scoops(self, scoops):
        """ Add scoops to bowl.

        Args:
            scoops (list of Scoop): scoops to be added.

        """
        # Your code here.
        pass


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
