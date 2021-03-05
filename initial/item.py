class Item:
    def __init__(self, name,  description = None, weight = 10 ): # Initilizer
        self.name = name
        self.description = description if description is not None else "No description given"
        self.weight = weight

    def __repr__(self):
        return f'Item({self.name},{self.description},{self.weight},)'

    def __str__(self):
        return f'Item-- (\n Name: {self.name},\n Weight: {self.weight},\n Description: {self.description} \n)'

class Weapon(Item):
    def __init__(self, name, damage, description = None, weight = 10):
        super(Weapon, self).__init__(name, description, weight)
        self.damage = damage

    def __str__(self):
        return f'Weapon-- (\n Name: {self.name},\n Damage: {self.damage}, \n Weight: {self.weight},\n Description: {self.description} \n)'
