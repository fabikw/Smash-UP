'''
Created on Jun 22, 2015

@author: fabian
'''

from enum import Enum

class Expansion(Enum):
    base = 1
    AL9000 = 2
    OCS = 3
    SFDF = 4
    BGB = 5
    MS = 6
    PPSU = 7
    M = 8
    PT = 9


# This module contains data to populate forms and lists.

destroying_actions = ["Burn it Down", "Not in Kansas"]

# FACTIONS is a dictionary where the keys are the factions' names, and the value is a tuple with the first and second word for the names as well as the expansion set.
FACTIONS = {'Aliens': ('Alien', 'Aliens', Expansion.base),
            'Dinosaurs': ('Dinosaur', 'Dinosaurs', Expansion.base),
            'Ninjas': ('Ninja', 'Ninjas', Expansion.base),
            'Pirates': ('Pirate', 'Pirates', Expansion.base),
            'Robots': ('Robotic', 'Robots', Expansion.base),
            'Tricksters': ('Trickster', 'Tricksters', Expansion.base),
            'Wizards': ('Wizarding', 'Wizards', Expansion.base),
            'Zombies': ('Zombie', 'Zombies', Expansion.base),

            'Bear Cavalry': ('Bear', 'Bears', Expansion.AL9000),
            'Ghosts': ('Ghost', 'Ghosts', Expansion.AL9000),
            'Killer Plants': ('Plant', 'Plants', Expansion.AL9000),
            'Steampunk': ('Steampunk', 'Steampunks', Expansion.AL9000),

            'Cthulhu Cultists': ('Cultist', 'Cultists', Expansion.OCS),
            'Elder Things': ('Elder Thing', 'Elder Things', Expansion.OCS),
            'Innsmouth': ('Innsmouth', 'of Insmouth', Expansion.OCS),
            'Miskatonic University': ('Miskatonic', 'Miskatonic', Expansion.OCS),

            'Time Travelers': ('Time Traveling', 'Time Travelers', Expansion.SFDF),
            'Cyborg Apes': ('Cyborg Ape', 'Cyborg Apes', Expansion.SFDF),
            'Super Spies': ('Super Spying', 'Super Spies', Expansion.SFDF),
            'Shapeshifters': ('Shapeshifting', 'Shapeshifters', Expansion.SFDF),

            'The Geeks': ('Geek', 'Geeks', Expansion.BGB),

            'Vampires': ('Vampire', 'Vampires', Expansion.MS),
            'Mad Scientists': ('Mad Scientist', 'Mad Scientists', Expansion.MS),
            'Werewolves': ('Werewolf', 'Werewolves', Expansion.MS),
            'Giant Ants': ('Giant Ant', 'Giant Ants', Expansion.MS),

            'Fairies': ('Fairy', 'Fairies', Expansion.PPSU),
            'Mythic Horses': ('Mythic Horse', 'Mythic Horses', Expansion.PPSU),
            'Kitty Cats': ('Kitty Cat', 'Kitty Cats', Expansion.PPSU),
            'Princesses': ('Princess', 'Princesses', Expansion.PPSU),

            'Clerics': ('Cleric', 'Clerics', Expansion.M),
            'Dwarves': ('Dwarf', 'Dwarves', Expansion.M),
            'Elves': ('Elf', 'Elves', Expansion.M),
            'Halflings': ('Halfling', 'Halflings', Expansion.M),
            'Mages': ('Mage', 'Mages', Expansion.M),
            'Orcs': ('Orc', 'Orcs', Expansion.M),
            'Thieves': ('Thief', 'Thieves', Expansion.M),
            'Warriors': ('Warrior', 'Warriors', Expansion.M),

            'Sharks': ('Shark', 'Sharks', Expansion.PT),
            'Superheroes': ('Superhero', 'Superheroes', Expansion.PT),
            'Tornadoes': ('Tornado', 'Tornadoes', Expansion.PT),
            'Mythic Greeks': ('Mythic Greek', 'Mythic Greeks', Expansion.PT),
            'Dragons': ('Dragon', 'Dragons', Expansion.PT)}

# BASES is a dictionary where the keys are the bases' names, and the value is a tuple with the point awards and the expansion
BASES = {'The Homeworld': (4, 2, 1, Expansion.base),
         'The Mothership': (4, 2, 1, Expansion.base),
         'Jungle Oasis': (2, 0, 0, Expansion.base),
         'Tar Pits': (4, 3, 2, Expansion.base),
         'Ninja Dojo': (2, 3, 2, Expansion.base),
         'Temple of Goju': (2, 3, 2, Expansion.base),
         'The Grey Opal': (3, 1, 1, Expansion.base),
         'Tortuga': (4, 3, 1, Expansion.base),
         'Factory 436-1337': (2, 2, 1, Expansion.base),
         'The Central Brain': (4, 2, 1, Expansion.base),
         'Cave of Shinies': (4, 2, 1, Expansion.base),
         'Mushroom Kingdom': (5, 3, 2, Expansion.base),
         'School of Wizardry': (3, 2, 1, Expansion.base),
         'The Great Library': (4, 2, 1, Expansion.base),
         'Evans City Cemetery': (5, 3, 2, Expansion.base),
         'Rhodes Plaza Mall': (0, 0, 0, Expansion.base),

         'Field of Honor': (3, 2, 1, Expansion.AL9000),
         "Tsar's Palace": (5, 3, 2, Expansion.AL9000),
         'Haunted House': (4, 3, 2, Expansion.AL9000),
         'The Dread Gazebo': (4, 2, 1, Expansion.AL9000),
         'Secret Grove': (3, 2, 1, Expansion.AL9000),
         'The Greenhouse': (4, 2, 1, Expansion.AL9000),
         "Inventor's Salon": (4, 2, 1, Expansion.AL9000),
         'Workshop': (4, 2, 1, Expansion.AL9000),

         'Antarctic Base': (5, 3, 2, Expansion.OCS),
         'Asylum': (3, 1, 1, Expansion.OCS),
         'Innsmouth': (5, 3, 2, Expansion.OCS),
         'Mountains of Madness': (6, 4, 3, Expansion.OCS),
         'Miskatonic University': (3, 3, 2, Expansion.OCS),
         'Plateau of Leng': (3, 2, 1, Expansion.OCS),
         "R'lyeh": (4, 2, 1, Expansion.OCS),
         'Ritual Site': (4, 2, 2, Expansion.OCS),

         'Monkey Lab': (4, 2, 1, Expansion.SFDF),
         'Primate Park': (3, 2, 1, Expansion.SFDF),
         'Faceless City': (4, 2, 1, Expansion.SFDF),
         'The Vats': (3, 1, 1, Expansion.SFDF),
         "ISI's Swingin' Pad": (4, 2, 1, Expansion.SFDF),
         'Secret Volcano Headquarters': (4, 3, 2, Expansion.SFDF),
         'Portal Room': (2, 3, 1, Expansion.SFDF),
         'The Nexus': (3, 3, 2, Expansion.SFDF),

         'TableTop': (4, 2, 1, Expansion.BGB),
         'The Con': (5, 3, 2, Expansion.BGB),

         'Egg Chamber': (3, 1, 1, Expansion.MS),
         'The Hill': (4, 2, 1, Expansion.MS),
         'Golem Schloß': (3, 3, 2, Expansion.MS),
         'Laboratorium': (5, 3, 3, Expansion.MS),
         'Castle Blood': (3, 1, 1, Expansion.MS),
         'Crypt': (4, 2, 2, Expansion.MS),
         'Moot Site': (2, 1, 0, Expansion.MS),
         'Standing Stones': (4, 2, 1, Expansion.MS),

         'Enchanted Glen': (4, 2, 1, Expansion.PPSU),
         'Fairy Circle': (4, 3, 2, Expansion.PPSU),
         'The House of Nine Lives': (4, 2, 1, Expansion.PPSU),
         "Cool Cats' Alley": (3, 2, 1, Expansion.PPSU),
         'Equaria': (5, 3, 2, Expansion.PPSU),
         'Pony Land': (3, 2, 1, Expansion.PPSU),
         'Beautiful Castle': (4, 2, 1, Expansion.PPSU),
         'Ice Castle': (3, 2, 2, Expansion.PPSU),

         'The Coffers': (4, 2, 1, Expansion.M),
         "Thieves' Guild": (4, 3, 2, Expansion.M),
         'Bastion': (3, 2, 2, Expansion.M),
         'The Gauntlet': (5, 3, 2, Expansion.M),
         'Hotel of Holiness': (4, 3, 2, Expansion.M),
         'Whack-A-Ghoul': (3, 2, 1, Expansion.M),
         'Dimension Doors': (4, 2, 1, Expansion.M),
         "Mage's Tower": (4, 3, 2, Expansion.M),
         'Treehouse': (4, 2, 1, Expansion.M),
         "Helper's Hollow": (3, 2, 1, Expansion.M),
         "The Mines": (4, 2, 1, Expansion.M),
         'Treasure Bath': (2, 0, 0, Expansion.M),
         'The Pits': (4, 2, 1, Expansion.M),
         'Garrison': (3, 2, 1, Expansion.M),
         'Birthday Party': (4, 2, 1, Expansion.M),
         'Subterranean Lair': (5, 3, 2, Expansion.M),

         'Shark Reef': (4, 2, 1, Expansion.PT),
         'The Deep': (3, 3, 2, Expansion.PT),
         'Converted Cave': (4, 3, 2, Expansion.PT),
         'Crystal Fortress': (3, 2, 1, Expansion.PT),
         'Oracle at Delphi': (3, 2, 2, Expansion.PT),
         'Wooden Horse': (4, 2, 1, Expansion.PT),
         "Worm's Desolation": (5, 3, 2, Expansion.PT),
         "Dragon's Lair": (4, 2, 1, Expansion.PT),
         "Storm Cellar": (4, 2, 1, Expansion.PT),
         "Tornado Alley": (4, 3, 2, Expansion.PT)}
