class Monster:
    def __init__(self, name, health, damage, description = None):
        self.name = name
        self.health = health
        self.damage = damage
        self.description = description if description is not None else "This is a monester and it is myYYYSssttterRRRiOOusss..."

    def take_hit(self, damage):
        if damage < self.health:
            self.health -= damage
        else:
            print(f'The monster {self.name} has died!')

    def attack(self, player):
        pass