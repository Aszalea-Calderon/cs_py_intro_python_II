from room import Room
from player import Player
from item import Item

# Monsters #

# ITEMS #
# Bow / arrows
item_bow_arrow = Item('Bow of wonder', 'Its a super cool, amazing, bow and arrow! Whoa! Nice!', 80)
# health pot
item_health_pot = Item('Health Pot', 'Its a health pot, it heals... and stuff', 0.5)
# sword
item_sword = Item('Magic sword', 'This is the sword you have looked for all your life. Why is it here??', 10)
# gold
item_gold = Item('Gold', 'Whoa! Its shiny gold. There are 20 pieces Maybe you can use this somewhere', 2)
# Boots
item_boots = Item('Boots', 'This is an old boot. Boooo.....', 3)
# helmet
item_helmet = Item('Helmet', 'Its a helmet. It is kinda beat up but better than nothing!', 3)
# potato
item_potato = Item('Potato', 'It looks like a potato, smells like a potato, feels like a potato.... but is it??', 1)
# Randomly assign items to rooms
# list_of_all_items = [item_bow_arrow, item_health_pot, item_sword, item_gold, item_boots, item_helmet, item_potato]

# DECLARE ROOMS
room_outside = Room(
    "Outside Cave Entrance",
    "North of you, the cave mount beckons",
    {item_health_pot: 3, item_sword:1}
)
room_foyer = Room(
    "Foyer",
    """Dim light filters in from the south. Dusty passages run north and east.""",
    {item_potato: 4, item_helmet: 1}
)
room_overlook = Room(
    "Grand Overlook",
    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",

)
room_narrow = Room(
    "Narrow Passage",
    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    {item_helmet: 1, item_bow_arrow:1}
)
room_treasure = Room(
    "Treasure Chamber",
    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    {item_gold: 10000, }
)

# Link rooms together
room_outside.branches.update({
    "north": room_foyer,
})
room_foyer.branches.update({
    "north": room_overlook,
    "east": room_narrow,
    "south": room_outside
})
room_overlook.branches.update({
    "south": room_foyer
})
room_narrow.branches.update({
    "south": room_foyer
})
room_treasure.branches.update({
    "south": room_narrow,
})
command_table ={
    'q':"q",
    'quit':"q",
    'f' : "find",
    'find' : "find",
    'i' : "inventory",
    'inventory' : "inventory",
}
direction_table = {
    'n':"north",
    'north':"north",
    'e':"east",
    'east':"east",
    'w':"west",
    'west': "west",
    's':"south",
    'south':"south",
}
## fight monster / inventory / search / a(action) / pickup item / drop item / use item / timeout (/flip table/) then reset
def die():
    print(f"You died! Restart to try again.")
    quit()

def handle_command_input(command):
    global player
    if command == "q":
        print('Thank you for playing!')
        quit() # This kills the flow of the program, how rude
    elif command == "find":
        player.search_room()
    elif command == "inventory":
        player.check_inventory()
    else:
        print('The cake is a lie. Command not found.')

# main method-- This is what gets run by default, the first time through
if __name__ == '__main__':
    # Make a new player object that is currently in the 'outside' room.
    name = input('Please input your name: ') # this will give the value for the name
    player = Player(name, room_outside)
    # Write a loop that:
    input("Press any key to get started on your adventure!")


    command_key = None # this is the key press to get it started
    while command_key != "q":
        print(player.current_location)
        command_key = input("What would you like to do? \n Options: [n,s,e,w, (q)- Quit, (i)- Inventory, (f)- Search room ]").lower() ## We want it to always be a key we recognize-

        # This is your reference table for what the user is typing in.
        if command_key in direction_table:
            player.move_rooms(direction_table[command_key])
        # This checks if it is a valid command or not
        elif command_key in command_table:
            handle_command_input(command_table[command_key]) # Good command, this is bracet
        else:
            print(f'Nah, "{command_key}" is not valid my boi! Try again:') # bad command, so warn away
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Prints branches<YAY
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.


