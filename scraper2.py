from urllib.request import urlopen
from recipe_and_ingredient_classes import Ingredient
from recipe_and_ingredient_classes import Recipe
import re
import pprint












""" This method gets the html string of a given website string. It opens the page, reads the page and decodes it with
utf-8. It takes the string url and returns the html string.
"""
def get_url_string(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

'''
This method gets all the children links from a page. Allrecipies.com strutures there recipies in a giant tree. In this
file I only look at the cookie sub tree. The cookie page has 32 children and these children have varying amounts of 
children as well. This method will get the children of a given page and return those children links in a list. 
It has to use two stages of regex to fist find the list of all the children list, and then it splits that list
by links. This list is returned

'''
def get_child_hyperlinks(html_string):
    list_of_ingredient = re.findall(".url\": \[[\s\S]*?\]", html_string)
    sub_link_list = re.findall("h.*\/", list_of_ingredient[0])
    return sub_link_list
    
'''
This method checks if the given link is the parent of recipies. At the lowest level of the tree discribed in the 
method above are recipies. A conglomeration of recipies will have a single parent. This method checks if the given
url is the parent to a conglomeration to recpies. It funtions by checking weather a url has children url that are 
parents. If the link's chidren are not parents thenselvs, then the given link is the parent of recipies.
Children links that are recipies are stored differently in the html than children links that are parents. If the 
string that typically stores the children that are parents is not found in the html of the given link, the current
link is a parent of recipies. 
'''
def parent_of_recipies(html_string):
    if len(re.findall(".url\": \[[\s\S]*?\]", html_string)) == 0:
        return True
    return False


'''
This method gets a list of all the children recipies. It must be fed a link that is a parent of recipies. 
It finds all the instances of recpies in the html. This list is made roughly and then further refined down to 
just the links of the children recipies. The list of all the recipies on a given page is returned. 

'''
def get_recipies_from_recipie_group(html_string):
    list_of_recipie_links = re.findall("class=\"card__titleLink manual-link-behavior\"[\s\S]*?href=[\s\S]*?title=[\s\S]*?aria-hidden=", html_string)
    returnlist = []
    for element in list_of_recipie_links:
        if re.findall("h.*\/", element)[0] not in returnlist:
            returnlist.append(re.findall("h.*\/", element)[0][6:])    
    return(returnlist)

'''
This funtion checks if a given page is a recpie or not. It looks at a part of the html string, and if it is
"ookines," than it is the top cookie page, and if it is "ecipes" it is a parent to either another parent, or 
a parent to recpies and therfor not a recipe page. 

'''
def check_if_recipe(html_string):
    title = re.findall("<title>.* Allrecipes", html_string)[0]
    recipie_or_naw = title[-19:-13]
    if recipie_or_naw != "ookies" and recipie_or_naw != "ecipes":
        return True
    return False

'''
this method returned and wrote to a file all the diffrent types of units of mesurements for every single
recipie reviewd. This was needed to do conversion to ounces. It takes a recpie html string, makes a list of
where all the units of mesurment are kept, goes through that list, trims each string, and adds that string to
a list if it is not already in it. If that unit of mesurement is not in the list than it is written to a file too. 

'''
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


'''
This method takes the html string and a name to make a recipie. It writes the recipie to a file. It begins by
finding all hte ingredient amounts, ingredient names, and ingredient units. It then iterates through all of these
lists simultaneously. It first trimms down and converts these parts as necessary, then finds the units of mesument
for a given ingredient, converts to ounces, then writes it to a file.  

'''
def read_and_make_recipie(html_string, name):
    t.write(name)
    t.write("\n")
    rating = re.findall("\"og:rating\" content=\".*\"", html_string)[0]
    trimmed_rating = rating[21:-1]
    t.write(trimmed_rating)
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
        if "cup" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount * 8)
        elif ingredient_amount_unit == "" or "egg" in ingredient_amount_unit:
            print(ingredient_amount)
            ingredient_amount = (ingredient_amount * 1.7)
        elif "table" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount * .5)
        elif "teaspoon" in ingredient_amount_unit:
            ingredient_amount = (ingredient_amount * .1666)
        elif "pound" in ingredient_amount_unit:
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
    



'''
This is funtion drives the scraping. It uses recusion to traverse the tree. It first gets the html string of
the input url. If the input is a recipie, then the funtion calls read_and_make_recipie for that url, and 
returns out of the funtion. If the url link is not a recipie url, it checks if it is the parent of recipies
with the parent_of_recipies funtion. If it is, it iterated through all the recipies, calling
itself(travese_tree_of_cookies_and_get_units) on each recipie. After recipies have been iterated through it returns
too. Finally, if it is not a parent of recipies, it iterates through all the child parents, and calls the funtion
on them. There are try and finally statements, becase there are some inconsistency on allrecpies.com. 
'''
def travese_tree_of_cookies_and_get_units(url_link):
    html_string = get_url_string(url_link)
    print(url_link)
    if check_if_recipe(html_string) and url_link in RECIPIES:
        RECIPIES.append(url_link)
        try:
            read_and_make_recipie(html_string, url_link)
        finally:
            return
    if parent_of_recipies(html_string):
        
        recipies = get_recipies_from_recipie_group(html_string)
        for element in recipies:

            try:
                travese_tree_of_cookies_and_get_units(element)
            finally:
                print("recipie added")
        
        return
    for url in get_child_hyperlinks(html_string):
        if url_link == "https://www.allrecipes.com/recipes/842/desserts/frostings-and-icings/cookie-frosting/":
            return
        travese_tree_of_cookies_and_get_units(url)
    return



if __name__ == "__main__":
    global RECIPIES
    RECIPIES = []
    url1 = "https://www.allrecipes.com/recipes/362/desserts/cookies/"#cookies url
    t = open("big_recipes.txt", "w")#file to write too

    travese_tree_of_cookies_and_get_units(url1)#traverse tree

    t.close()#close file

