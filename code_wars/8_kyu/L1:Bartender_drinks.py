##DONE##
def get_drink_by_profession(param):
    drinks = {
        'jabroni': 'Patron Tequila',
        'school counselor': 'Anything with Alcohol',
        'programmer': 'Hipster Craft Beer',
        'bike gang member': 'Moonshine',
        'politician': 'Your tax dollars',
        'rapper': 'Cristal',
        }
    param = param.lower()
    if param in drinks.keys():
        return drinks[param]
    else:
        return('Beer')
