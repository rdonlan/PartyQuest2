'''
THe recipe class reperesents a recipe which contains a name and a list of ingredient. It has string 
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
Ingredient class represents ingredients in a recipe. An Ingredient has a name and quanity, and two setter
methods
'''
class Ingredient(object):
    def __init__(self, name, quantity):
        self.name = name            # string
        self.quantity = quantity    # float
        
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

    '''
    Returns quantity of the name of the ingredient 
    '''
    def __str__(self):
        # allows you to use print(Ingredient)
        return str(self.quantity) + " oz of " + self.name