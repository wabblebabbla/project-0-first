class Collectable:
    def __init__(self, type_of, description, value):
        self.type_of = type_of
        self.description = description
        self.value = value
    
    def examine(self):
        print(self.description)

    # I want to make it so that this collectable can be picked up and added to the inventory
    


    # I want to make it so that this collectable can be dropped and removed from the inventory