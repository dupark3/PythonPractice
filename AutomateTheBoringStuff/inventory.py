#! /usr/bin/python3.5

def addToInventory(inventory, loot):
    for item in loot:
        inventory.setdefault(item, 0)
        inventory[item] += 1

def displayInventory(inventory):
    print('Inventory: ')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))

inventory = {'rope':42, 'coin':200, 'sword':1}
displayInventory(inventory)

dragonLoot = ['coin', 'rope', 'dagger', 'sword', 'coin', 'coin', 'armor']
addToInventory(inventory, dragonLoot)
displayInventory(inventory)