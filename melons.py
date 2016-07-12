""" Edit files to track flesh color, rind color, and average weight of melons. Output should look something like:

CASABA
  seedless: False
  price: 2.5
  flesh_color: None
  weight: None
  rind_color: None
Refactor melons.py and melon_info.py to make it easier to add more things to track in the future.

Hint 1: You can change the format of the melons.py file

Hint 2: Try combining data into one big dictionary

Hint 3: With melon name as the key and a dictionary containing melon info as the value

"""


def melon_inventory(melon_name, price, seedless,
                    flesh_color, weight, rind_color):
    """

    """

    melons = {}

    melons[melon_name] = {

        'price': float(price),
        'seedless': seedless,
        'flesh_color': flesh_color,
        'weight': float(weight),
        'rind_color': rind_color

    }

    print melons

melon_inventory('Watermelon', 5, False, 'red', 10, 'green')

melon_inventory('Cantaloupe', 3, True, 'orange', 3.5, 'tan')
