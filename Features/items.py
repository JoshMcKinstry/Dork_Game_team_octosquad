class Items:
    """ Creates, uses and stores item objects"""

    def __init__(self, item):
        self.item = item

    def add_item(self, item):
        self.item.append(item)
    
    def use(self, item):
        print("You used the " + item)

    def store(self, item,):
        print("You stored the " + item + " into your inventory")
