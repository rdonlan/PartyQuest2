Authors: Caleb Eurich, Ryan Donlan, Noah Gans
CSCI 3725
PQ2
3/131/2021

This program scrapes cookie recipies from the internet, stores these recipies as recipe objects with ingredient object arrays. Once scraped, these objects are used to generalize the average ratio of ingredients in popular cookies. This data is then used with some intentional variation to generate new cookie recipies with ingredients found in scraped recipies and ingredients similar to those in most normal cookies. After generating random cookies, this program uses a genetic algorithm to optimize cookie recipies over multiple generations. In order to do this, the program uses rank selection based on fitness metrics of novelys and value. Following this, there is some mutation and recombination of ingredients as you would find in any GA. In order to run this project, run executor.py with no arguments. Global variables can be changed in executor.py to impact the GA. 

This folder contains six main python files and a text file generated from web scraping. 

scraper2.py scrapes popular cookie recipies from the internet and populates a text file to be used as the inspiring set for our program. 

recipe_and_ingredient_classes.py contains the basic structure of our recipe and ingredient classes along with helper methods for assigning properties to these objects. 

fitness_functions.py contains the fitness functions. The novelty fitness function calculted fitness based on amount of other ingredients to favor more interesting recipes. The value fitness function calculated fitness based on the recipe's score from the flavor index which is a 2D matrix which holds values correlated to how often ingredients showed up in the same recipe in the inspiring set. Ideally this should mimic some metric of how well the ingredients go together and taste good. 

rank_selection.py contains the selection portion of the GA. This file ranks recipies based on fitness and chooses individuals to breed from there. 

Recombination_and_mutation.py contains the GA functinality for recombination and mutation. Ingredients are recombined and mutated in a way that preserves the "kinds" structure and does not vary cookies too far from the original ratio.

Executor.py does the heavy lifting of this program. It can be run with no arguments and will generate cookie recipies based on ratios and ingredients from the inspiring set in the text file. When run, executor will print the best recipe found after running the genetic algorithm. 

This program produces reasonable recipes overall that seem edible!



