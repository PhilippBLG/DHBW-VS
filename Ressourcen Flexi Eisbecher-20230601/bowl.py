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
        self.flavour = flavour

    def __str__(self):
        return f"Scoop with flavour '{self.flavour}'"

    def get_price():
        return 120

class Cream:

    price = 100

    def __init__(self, sugar=False):
        self.sugared = sugar

    def get_price():
        return 100

    def __str__(self):
        if self.sugared:
            return f"Sugared cream serving"
        else:
            return f"Pure cream serving"
class Bowl():
    """ A bowl of ice cream scoops. """

    def __init__(self, max_scoops, max_cream):
        self.bowl = []
        self._scoop_list = []
        self._cream_list = []
        self._max_scoops = max_scoops
        self._max_cream = max_cream

    def __str__(self):
        scoops_str = '\n'.join(str(scoop) for scoop in self._scoop_list)
        cream_str = "\n".join(str(cream) for cream in self._cream_list)
        if cream_str is not "":
            cream_str += "\n"
        return f"Bowl for {self.get_price() // 100} Euro and {self.get_price() % 100} Cent contains:\n" \
               f"{cream_str}" \
               f"{scoops_str}"

    def add_scoops(self, scoops):
        """ Add scoops to bowl.

        Args:
            scoops (list of Scoop): scoops to be added.

        """
        for scoop in scoops:
            if len(self._scoop_list) == self._max_scoops:
                break
            self._scoop_list.append(str(scoop))

    def get_price(self):
        return len(self._scoop_list)*Scoop.price

    def add_cream(self, cream):
        self._cream_list.append(cream)


class ChocBowl(Bowl):

    def __init__(self):
        super().__init__(max_scoops=8, max_cream=3)
        self._scoop_list = [Scoop("Chocolate"), Scoop("Chocolate"), Scoop("Chocolate")]
        self._cream_list = [Cream(sugar=False)]

    def add_scoops(self, scoops):
        for scoop in scoops:
            if len(self._scoop_list) == self._max_scoops:
                break
            if str(scoop) == str(Scoop("Chocolate")):
                self._scoop_list.append(scoop)
    def get_price(self):
        return len(self._scoop_list)*Scoop.get_price()+len(self._cream_list)*Cream.get_price()

    # def __str__(self):
    #     scoops_str = '\n'.join(str(scoop) for scoop in self._scoop_list)
    #     cream_str = "\n".join(str(cream) for cream in self._cream_list)
    #     return f"Bowl for {self.get_price() // 100} Euro and {self.get_price() % 100} Cent contains:\n" \
    #            f"{cream_str}\n" \
    #            f"{scoops_str}"
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
