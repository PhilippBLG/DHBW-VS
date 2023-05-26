"""Represents a bowl of ice cream.

Authors:
    John Doe <mail@johndoe.org>
"""


class Scoop:
    """ Represents a single scoop of ice cream."""

    price = 120

    def __init__(self, flavour):
        """ Initialize.

        Args:
            flavour (str): Flavour of ice cream (e. g. "Vanilla").

        """
        self._flavour = flavour

    def __str__(self):
        return f"Scoop with flavour '{self._flavour}'"

    @property
    def flavour(self):
        return str(self._flavour)


class Bowl:
    """ A bowl of ice cream scoops. """

    max_scoops = 8

    def __init__(self):
        self.bowl = []
        self._scoop_list = []

    def __str__(self):
        scoops_str = '\n'.join(str(scoop) for scoop in self._scoop_list)
        return f"Bowl for {self.get_price()//100} Euro and {self.get_price()%100} Cent contains:\n{scoops_str}"

    def add_scoops(self, scoops):
        """ Add scoops to bowl.

        Args:
            scoops (list of Scoop): scoops to be added.

        """
        for scoop in scoops:
            if len(self._scoop_list) == self.max_scoops:
                break
            self._scoop_list.append(str(scoop))

    def get_price(self):
        return len(self._scoop_list)*Scoop.price


class ChocBowl(Bowl):
    cream_price = 100

    def __init__(self):
        super().__init__()
        self._scoop_list = [Scoop("Chocolate"), Scoop("Chocolate"), Scoop("Chocolate")]
        self.cream = 1

    def __str__(self):
        scoops_str = '\n'.join(str(scoop) for scoop in self._scoop_list)
        return f"Bowl for {self.get_price() // 100} Euro and {self.get_price() % 100} Cent contains:\n" \
               f"{self.cream} serving(s) of cream\n" \
               f"{scoops_str}"

    def add_scoops(self, scoops):
        for scoop in scoops:
            if len(self._scoop_list) == self.max_scoops:
                break
            if str(scoop) == str(Scoop("Chocolate")):
                self._scoop_list.append(scoop)
            #else:
                #raise ValueError("ChocBowl can only contain Chocolate Scoops")

    def cream(self, count):
        if count < 0:
            count = -count
        self.cream = count

    def get_price(self):
        return len(self._scoop_list) * Scoop.price + self.cream * self.cream_price


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
