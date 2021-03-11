from urllib.request import urlopen
from recipe_and_ingredient_classes import Ingredient
from recipe_and_ingredient_classes import Recipe
import re
import pprint

list_of_cookie_types = ["https://www.allrecipes.com/recipes/836/desserts/cookies/bar-cookies/",
            "https://www.allrecipes.com/recipes/837/desserts/cookies/biscotti/",
            "https://www.allrecipes.com/recipes/838/desserts/cookies/brownies/",
            "https://www.allrecipes.com/recipes/15057/desserts/cookies/butter-cookies/",
            "https://www.allrecipes.com/recipes/11977/desserts/cookies/cake-mix-cookies/",
            "https://www.allrecipes.com/recipes/839/desserts/cookies/chocolate-chip-cookies/",
            "https://www.allrecipes.com/recipes/840/desserts/cookies/chocolate-cookies/",
            "https://www.allrecipes.com/recipes/841/holidays-and-events/christmas/desserts/christmas-cookies/",
            "https://www.allrecipes.com/recipes/844/desserts/cookies/cut-out-cookies/",
            "https://www.allrecipes.com/recipes/16394/desserts/cookies/drop-cookies/",
            "https://www.allrecipes.com/recipes/846/desserts/cookies/filled-cookies/",
            "https://www.allrecipes.com/recipes/847/desserts/cookies/fruit-cookies/",
            "https://www.allrecipes.com/recipes/14712/desserts/cookies/gingerbread-cookies/",
            "https://www.allrecipes.com/recipes/16416/desserts/cookies/sandwich-cookies/",
            "https://www.allrecipes.com/recipes/14691/desserts/cookies/thumbprint-cookies/",
            "https://www.allrecipes.com/recipes/17794/desserts/cookies/gingersnaps/",
            "https://www.allrecipes.com/recipes/845/desserts/cookies/international-cookies/",
            "https://www.allrecipes.com/recipes/17019/desserts/cookies/macaroons/",
            "https://www.allrecipes.com/recipes/848/desserts/cookies/meringue-cookies/",
            "https://www.allrecipes.com/recipes/849/desserts/cookies/no-bake-cookies/",
            "https://www.allrecipes.com/recipes/850/desserts/cookies/nut-cookies/",
            "https://www.allrecipes.com/recipes/851/desserts/cookies/oatmeal-cookies/",
            "https://www.allrecipes.com/recipes/852/desserts/cookies/peanut-butter-cookies/",
            "https://www.allrecipes.com/recipes/968/desserts/cookies/pumpkin-cookies/",
            "https://www.allrecipes.com/recipes/854/desserts/cookies/refrigerator-cookies/",
            "https://www.allrecipes.com/recipes/855/desserts/cookies/butter-cookies/shortbread-cookies/",
            "https://www.allrecipes.com/recipes/16420/desserts/cookies/snickerdoodles/",
            "https://www.allrecipes.com/recipes/857/desserts/cookies/spice-cookies/",
            "https://www.allrecipes.com/recipes/859/desserts/cookies/sugar-cookies/",
            "https://www.allrecipes.com/recipes/16417/desserts/cookies/whoopie-pies/",
            "https://www.allrecipes.com/recipes/16162/desserts/cookies/zucchini-cookies/",
            "https://www.allrecipes.com/recipes/842/desserts/frostings-and-icings/cookie-frosting/"]




url = "https://www.allrecipes.com/recipe/18185/yum/"
url1 = "https://www.allrecipes.com/recipes/362/desserts/cookies/"




t = open("test2.txt", "w")
print("done")

RECIPECOUNTER = 0

unitsList = []

def get_url_string(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html




def get_child_hyperlinks(html_string):
    list_of_ingredient = re.findall(".url\": \[[\s\S]*?\]", html_string)
    sub_link_list = re.findall("h.*\/", list_of_ingredient[0])
    return sub_link_list
    

def parent_of_recipies(html_string):
    if len(re.findall(".url\": \[[\s\S]*?\]", html_string)) == 0:
        return True
    return False



def get_recipies_from_recipie_group(html_string):
    list_of_recipie_links = re.findall("class=\"card__titleLink manual-link-behavior\"[\s\S]*?href=[\s\S]*?title=[\s\S]*?aria-hidden=", html_string)
    returnlist = []
    for element in list_of_recipie_links:
        if re.findall("h.*\/", element)[0] not in returnlist:
            returnlist.append(re.findall("h.*\/", element)[0][6:])    
    return(returnlist)

def check_if_recipe(html_string):
    title = re.findall("<title>.* Allrecipes", html_string)[0]
    recipie_or_naw = title[-19:-13]
    if recipie_or_naw != "ookies" and recipie_or_naw != "ecipes":
        return True
    return False

def read_and_make_recipie(html_string, name):
    print("making recipie")
    print("why are you not coming here")
    t.write(name)
    t.write("\n")
    list_of_ingredient = re.findall("data-ingredient = \".+?\" data-unit", html_string)
    list_of_ingredient_amounts = re.findall("data-init-quantity = \".+?\" data-unit", html_string)
    list_of_units = re.findall("data-unit = \".*?\"", html_string)
    ing_to_add = []
    for i in range(len(list_of_ingredient)):
        ingredient_amount_unit_list = str(re.findall("\".+?\"", list_of_units[i]))
        ingredient_amount = str(re.findall("\".+?\"", list_of_ingredient_amounts[i]))
        ingredient_amount = float(ingredient_amount[3:-3])
        ingredient_name = str(re.findall("\".+?\"", list_of_ingredient[i]))
        ingredient_amount_unit = ingredient_amount_unit_list[3:-3]
        print("cow")
        if "cup" in ingredient_amount_unit:
            print("CUP")
            ingredient_amount = (ingredient_amount * 8)
        elif ingredient_amount_unit == "" or "egg" in ingredient_amount_unit:
            print(ingredient_amount)
            ingredient_amount = (ingredient_amount * 1.7)
        elif "table" in ingredient_amount_unit:
            print("Table Spoon")
            ingredient_amount = (ingredient_amount * .5)
        elif "teaspoon" in ingredient_amount_unit:
            print("tea Spoon")
            ingredient_amount = (ingredient_amount * .1666)
        elif "pound" in ingredient_amount_unit:
            print("pound")
            ingredient_amount = (ingredient_amount * 16)
        elif "stick" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount * 16)
        elif "pinch" or "drop" or "dash" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount / 32)
        elif "ounce)" in ingredient_amount_unit:
            ingredient_amount = float(ingredient_amount_unit[1:-7])
        elif "pint" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount_unit * 16)
        elif "quart" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount_unit * 32)
        elif "gallon" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount_unit * 128)
        else:
            ingredient_amount = ingredient_amount
        t.write(str(ingredient_amount) + " oz " + str(ingredient_name[3:-3]) )
        t.write("\n")

        ing_to_add.append(Ingredient(ingredient_name[3:-3], ingredient_amount))
    
    
    t.write("\n\n")
    new = Recipe("recipie num " + str(recipie_num), ing_to_add)

def get_units_of_mesurment(html_string):
    list_of_units = re.findall("data-unit = \".*?\"", html_string)
    print(list_of_units)
    for i in range(len(list_of_units)):
        ingredient_amount_unit = str(re.findall("\".+?\"", list_of_units[i]))
        if ingredient_amount_unit[3:-3] not in unitsList:
            unitsList.append(ingredient_amount_unit[3:-3])
            print(ingredient_amount_unit[3:-3])
            t.write(ingredient_amount_unit[3:-3] + "\n")
    print(unitsList)


def travese_tree_of_cookies_and_get_units(url_link):
    print(url_link)
    link = get_url_string(url_link)
    print(check_if_recipe(link))
    if check_if_recipe(link):
        print("came here")
        read_and_make_recipie(link, url_link)
        return
    if parent_of_recipies(link):
        try:
            recipies = get_recipies_from_recipie_group(link)
            for element in recipies:
                travese_tree_of_cookies_and_get_units(element)
                
        finally:
            return
    for url in get_child_hyperlinks(link):
        travese_tree_of_cookies_and_get_units(url)
    return

#link = get_url_string(url1)
#read_and_make_recipie(link, 1)
#t.write(link)
#get_units_of_mesurment(link)
#print(check_if_recipe(link))

travese_tree_of_cookies_and_get_units(url1)
#link = get_url_string(url1)
#print(check_if_recipe(link))
#get_units_of_mesurment(link)
#list_of_children = get_child_hyperlinks(link)
#for element in list_of_children:
    #print(element)


t.close()

#recipies = get_recipies_from_recipie_group(link)


#list_of_links = get_child_hyperlinks(link)
#print(list_of_links)