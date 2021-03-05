from item import Weapon

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_location, inventory = None,):
        fists = Weapon("fists", 2, "Its your hands", 0)
        self.name= name
        self.current_location = current_location
        self.inventory = inventory if inventory is not None else {}
        self.inventory.update({fists: 1})
        self.capacity = 50
        self.health = 100
        self.weapon = fists
    def __str__(self):
        return f"""
--------
Player
--------
* Name: {self.name}
* Current Health : {self.health}
* Current Capacity: {self.capacity}
* Current Weapon : {self.weapon} 
* Your Current Location: {self.current_location.name}
    * Description: {self.current_location.description}
--------
"""
    def move_rooms(self, direction):
        self.current_location = self.current_location.get_room_in_direction(direction)
        if self.current_location.monster:
            take_action = input(f'You have been spotted by a {self.current_location.monster}. What would you like to do? [Y or N] ').lower()
            if take_action == 'y' or take_action =="yes":
                self.attack(self.current_location.monster)
            else:
                self.get_hit(self.current_location.monster.damage)

    def check_inventory(self):
        print(f"""
-------
Inventory 
-------
{self.inventory if len(self.inventory) > 0 else "No items in inventory! Go adventure."}
""")
        will_manage= input('To manage inventory (m)- Manage inventory').lower()
        if will_manage == "m" or will_manage == "manage":
            self.manage_inventory()


    def drop_item(self, item):
        if item not in self.inventory:
            print('How did you do that? That is not allowed and you know it!')
            return
        self.inventory[item] -= 1
        if self.inventory[item] == 0:
            del self.inventory[item]
        self.capacity += item.weight
        self.current_location.handle_dropped_item(item)

    def pick_up_item(self, item):
        if item.weight > self.capacity:
            print("You are carrying too much! That can hurt your back, please drop something before you can pick this up!")
            return
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] +=1
        self.capacity -= item.weight
        self.current_location.handle_taken_item(item)
        if isinstance(item, Weapon): ## this is our weapon check
            will_replace = input(f"You have picked up a weapon! Would you like to use {item} instead of {self.weapon}? [Y or N]").lower()
            if will_replace == "y" or will_replace== "yes":
                self.weapon = item

    def manage_inventory(self):  ## Inventory list with item numbers, and have the ability to click on it
        items_to_remove = []
        for item in self.inventory:
            will_drop = input(f'Is {item} the item you want to drop? [Y or N]').lower()
            if will_drop == 'y' or will_drop == "yes":
                items_to_remove.append(item)
        for item in items_to_remove:
            self.drop_item(item)

    def search_room(self):
        items_to_take =[]
        for item, count in self.current_location.items.items():
            will_take = input(f'Do you wish to pick up \n {item}, there are {count}? [Y or N]').lower()
            if will_take == "y" or will_take == 'yes':
                num_to_take = int(input(f'How many would you like? As a reminder there is {count}. Please type the number of items you would like to take!'))
                items_to_take.extend([item for _ in range(num_to_take)])
        for item in items_to_take:
            self.pick_up_item(item)

    def attack(self, enemy):
        enemy.get_hit(self.weapon.damage)

    def get_hit(self, damage):
        if damage < self.health:
            self.health -= damage
        else:
            print(f"You dieddddd!")

