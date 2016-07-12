def melon_inventory(melon_name, price, seedless,
                    flesh_color, weight, rind_color):

    """Prints a dictionary with melon information.

    Initializes with empty dictionary 'melons_in_stock'. Sets the melon_name
    input as a key in melons_in_stock, and the other info is stored in a
    dictionary as the value to melon_name.

    Each successive melon_name is added as a new key with new dictionary to
    the melons_in_stock dictionary

    For example::

    >>> melon_inventory('Cantaloupe', 3, True, 'orange', 3.5, 'tan')
    {'Cantaloupe': {'seedless': True, 'price': 3.0, 'flesh_color': 'orange',
     'weight': 3.5, 'rind_color': 'tan'}




    """

    melons_in_stock = {}

    melons_in_stock[melon_name] = {

        'price': float(price),
        'seedless': seedless,
        'flesh_color': flesh_color,
        'weight': float(weight),
        'rind_color': rind_color

    }

    print melons_in_stock

# melon_inventory('Cantaloupe', 3, True, 'orange', 3.5, 'tan')

# melon_inventory('Watermelon', 5, False, 'red', 7, 'green')
