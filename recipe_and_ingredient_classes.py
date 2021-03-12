'''
THe recipe class reperesents a recipe which contains a name and a list of ingredient. It has string 
representation method, and check_for_ingredients method. Check_for_ingrediens checks if an ingredient 
type is in the recipe 
'''


KINDS = ["sugar", "flour", "salt", "butter", "baking powder", "milk", "egg", "vanilla", "chips", "baking soda", "other"]

class Recipe(object):
    def __init__(self, name, ingredient_arr):
        self.name = name #name of recipe string
        self.ingredient_arr = ingredient_arr #array of ingredients

    '''
    check_for_ingredients iterates through all the ingredients and returns true if the input string matches
    any of the names of the ingredients and false otherwise.
    '''
    def check_for_ingredient(self, name):
        for ingredient in self.ingredient_arr: 
            if name == ingredient.name:
                return True
        return False


    '''
    This string funtion returns the name of the recipe and the ingredients that are in that racipe. Iterates
    through all ingredients to print their name and quantity. 
    '''
    def __str__(self):
        # allows you to use print(Recipe)
        final_string = self.name + " contains the ingredients below:" + "\n"
        for ingredient in self.ingredient_arr:
            str_to_add = str(ingredient.quantity) + " oz of " + ingredient.name + "\n"
            final_string += str_to_add
        return final_string
        
'''
Ingredient class represents ingredients in a recipe. An Ingredient has a name and quanity, and two setter
methods
'''
class Ingredient(object):
    def __init__(self, name, quantity):
        self.name = name            # string
        self.quantity = quantity    # float
        self.kind = get_kind(name)  # string
        
    '''
    Sets the quantity of the Ingredient
    '''
    def set_quantity(self, amount):
        self.quantity = amount
    '''
    Sets the name of the Ingredient
    '''
    def set_name(self, name):
        self.name = name
        self.kind = get_kind(name)

    '''
    Returns quantity of the name of the ingredient 
    '''
    def __str__(self):
        # allows you to use print(Ingredient)
        return str(self.quantity) + " oz of " + self.name

# def get_kind(name):
#     for kind in KINDS[:-1]: #exclude "other"
#         # we need to fix edge text cases like milk chocolate chips
#         if kind in name:
#             return kind

#     return "other"



def get_kind(name):
    if "sugar" in name:
        return "sugar"
    if "flour" in name:
        return "flour"
    if "salt" in name:
        return "salt"
    if "butter" in name:
        if "butterscotch" not in name and "buttermilk" not in name: #exclude edge case
            return "butter"
    if "baking powder" in name:
        return "baking powder"
    if "milk" in name:
        if "chocolate" not in name: #exclude edge case
            return "milk"
    if "egg" in name:
        return "egg"
    if "vanilla" in name:
        return "vanilla"
    if "chips" in name:
        return "chips"
    if "baking soda" in name:
        return "baking soda"
    else:
        return "other"
