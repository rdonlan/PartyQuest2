                  Authors: Caleb Eurich, Ryan Donlan, Noah Gans
CSCI 3725
PQ2
3/12/2021

This program scrapes cookie recipies from the internet, stores these recipies as recipe objects with ingredient objects. These objects are used to generalize and average ratio of ingredients in popular cookies. This data is then used with some intentional variation to generate new cookie recipies with ingredients found in scraped recipies and ingredients similar to those in most normal cookies. In order to run this project, run executor.py with no arguments.

This folder contains three main python files and a text file generated from web scraping. scraper2.py scrapes popular cookie recipies from the internet and populates a text file to be used as the inspiring set for our program. recipe_and_ingredient_classes.py contains the basic structure of our recipe and ingredient classes along with helper methods for assigning properties to these objects. Executor.py does the heavy lifting of this program. It can be run with no arguments and will generate cookie recipies based on ratios and ingredients from the inspiring set in the text file. When run, executor will print NEW_RECIPES_TO_BE_GENERATED new recipies which is currently set to 5. 

Our cookie recipe generation program has two creativity metrics aimed to account for value and novelty. The code for these functions can be found in the fitness_funtions.py file. Out metric for novelty scores recipes based on the number of other/added ingredients in the recipe. The more ingredients the higher score the recipe received. Other ingredients are those that are added onto the base ingredients of a cookie, and therefore the addition of them makes the cookie progressively more different from a regular cookie. For value, we needed a way to judge taste. A valuable cookie would be one that tasted good. Good taste is difficult to quantify, but we theorized that ingredients that appeared in the same recipe more frequently tasted better together. This idea was formulated into the flavor index. The flavor index is a 2D array that is the length and width of all the ingredients from all the recipes. For each ingredient, if another ingredient occurred in the same recipe, the corresponding index would be increased by 1. After going through every recipe and every ingredient in every recipe any ingredients that did not appear with other ingredients would be receive a -1. This allowed for a recipes’ ingredients to be scored on their flavor compatibility, which was done by comparing each ingredient to every other ingredient in a recipe and summing the score from the flavor index. Scoring cookies on these too metrics would produce novel and valuable cookies. In our final program, the value score is weighted more heavily than the novelty score. Our reasoning and examples are included in metrics.txt. 

So far these recipies appear to resemble cookies that would actually be edible which is cool!



