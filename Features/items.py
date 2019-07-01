class Items:
    """ Creates, uses and stores item objects"""

    def __init__(self, name):
        self.name = name

    def use(self):
        print("You used the " + self.name)

    def store(self):
        print("You stored the " + self.name + " into your inventory")
