stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):

    print('Inventory')
    item_total = 0
    for k, v in inventory.items():
        print('{} {}'.format(v, k))
        item_total += v
    print('Total number of items: {}'.format(item_total))


display_inventory(stuff)