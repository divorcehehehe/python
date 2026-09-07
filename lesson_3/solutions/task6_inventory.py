inventory = {}

while True:
    parts = input().split()
    if not parts:
        continue

    command = parts[0]
    if command == 'stop':
        break

    if command == 'show':
        if not inventory:
            print('пусто')
        for name in sorted(inventory):
            print(name, inventory[name])
    elif command == 'add':
        name, count = parts[1], int(parts[2])
        inventory[name] = inventory.get(name, 0) + count
    elif command == 'remove':
        name, count = parts[1], int(parts[2])
        left = inventory.get(name, 0) - count
        if left > 0:
            inventory[name] = left
        elif name in inventory:
            del inventory[name]
