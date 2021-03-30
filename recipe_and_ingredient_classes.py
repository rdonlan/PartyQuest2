
# This array shows the index positions, and category types/names, of our different kinds of ingredients in a recipe
KINDS = ["sugar", "flour", "salt", "butter", "baking powder", "milk", "egg", "vanilla", "chips", "baking soda", "other"]

'''
The recipe class reperesents a recipe which contains a name and a list of ingredient. It has string 
representation method, and check_for_ingredients method. Check_for_ingrediens checks if an ingredient 
type is in the recipe 
'''

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
Ingredient class represents ingredients in a recipe. An Ingredient has a name, quanity and kind, as well as
two setter methods
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


'''Helper Function to assign ingredient kinds from names. There are edge cases that
we have added in the form of extra if statements.
    Params:
        @string name: name of ingredient
    Return:
        String --> more general type of ingredient
'''
def get_kind(name):
    if "sugar" in name:
        if "refrigerated" not in name:
            return "sugar"
    if "flour" in name:
        return "flour"
    if "salt" in name and "salted" not in name:
        return "salt"
    if "butter" in name:
        if "butterscotch" not in name and "buttermilk" not in name and "peanut" not in name: #exclude edge case
            return "butter"
    if "baking powder" in name:
        return "baking powder"
    if "milk" in name:
        if "chocolate" not in name: #exclude edge case
            return "milk"
    if "egg" in name:
        return "egg"
    if "vanilla" in name:
        if "french" not in name or "French" not in name: #exclude edge case
            return "vanilla"
    if "chips" in name:
        return "chips"
    if "baking soda" in name:
        return "baking soda"
    else:
        return "other"
