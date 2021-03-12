Authors: Caleb Eurich, Ryan Donlan, Noah Gans
CSCI 3725
PQ2
3/12/2021

This program scrapes cookie recipies from the internet, stores these recipies as recipe objects with ingredient objects. These objects are used to generalize and average ratio of ingredients in popular cookies. This data is then used with some intentional variation to generate new cookie recipies with ingredients found in scraped recipies and ingredients similar to those in most normal cookies. In order to run this project, run executor.py with no arguments.

This folder contains three main python files and a text file generated from web scraping. scraper2.py scrapes popular cookie recipies from the internet and populates a text file to be used as the inspiring set for our program. recipe_and_ingredient_classes.py contains the basic structure of our recipe and ingredient classes along with helper methods for assigning properties to these objects. Executor.py does the heavy lifting of this program. It can be run with no arguments and will generate cookie recipies based on ratios and ingredients from the inspiring set in the text file. When run, executor will print NEW_RECIPES_TO_BE_GENERATED new recipies which is currently set to 5. 

So far these recipies appear to resemble cookies that would actually be edible which is cool!



