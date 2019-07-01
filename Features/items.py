class Items:
    """ Creates item objects"""

    def __init__(self, item, use):
        self.item = item
        self.use = use

    def add_item(self, item):
        self.item.append(item)
    
    def use(self, item):
        self.print("You used the " + item)

    def store(self, item,):
        self.print("You stored the " + item + " into your inventory")
        