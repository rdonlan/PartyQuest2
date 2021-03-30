from fitness_functions import novel_fitness_function, value_fitness_function
from recipe_and_ingredient_classes import Recipe, Ingredient
import random

MAX_NUM_OTHER_INGREDIENTS = 5

'''
This method returns the sum of all the ranks for a given population. It iterates through the size of the
population and sums all the index's. The denominator will be used to calculate probabilities for each
individual index. 
    Params:
        @pop_num {int}: number of individuals within the population
    Return:
        int --> the denominator to be used in rank sum
'''
def ranked_sum(pop_num):
    denominator = 0
    for i in range(1, pop_num + 1):
        denominator += i
    return denominator


'''
This method returns a list with each index filled with probabilities. These probabilities are the sumation of 
all ranks up to the respective index divided by the total sumation of all indexes. For every index, the 
probability is added to the return list creating a list of cumulative proababilites. This list will
be iterated through and checked against a random generated number.
    Params:
        @pop_num {int}: number of individuals within the population
    Return:
        @prob_list {arr[float]}: each index, i, contains the probability of selecting an individual at that index, i, from a ranked population 
'''
def rank_selection_cum_prob_list(pop_num):
    denominator = ranked_sum(pop_num)
    cum_sum = 0
    prob_list = []
    for i in range(1, pop_num+1):
        cum_sum += i
        prob = cum_sum / denominator
        prob_list.append(prob)
    return prob_list


'''
This method takes in the population to be sorted by rank. With this population, another list, pop_rank, is
filled with the corresponding ranks of each individual in the population. These two lists are merged into
onelist of tuples that contains individuals and their rank. Rank is based of length of the array holding their 
ingredients. This tuple list is sorted by rank, and a list is returned with the population now ordered by rank.  
    Params:
        @pop {arr[Recipe obj]}: population of recipes to be sorted by rank
        @flavor_matrix {arr[arr[float]]}: this 2D array contains N arrays that are a length of N where N is the number of unique ingredients in the
            inspiring set. Each arr will contain the correlation values for that ingredient with every other unique ingredient. The index of each ingredient in 
            @single_ingredients_arr corresponds to the index of the ingredient's correlation array within the 2D array, as well as its position in every
            other ingredient's correlation array. 
        @single_ingredients_arr corresponds to the index of the ingredient's correlation array within the 2D array, as well as its position in every
            other ingredient's correlation array. 
    Return:
        @r {arr[Recipe objs]}: a sorted list of recipes that are ranked by fitness


'''
def sort_by_rank(pop, flavor_matrix, single_ingredients_arr):
    # pop is an array containing our recipes
    pop_rank = []
    for i in range(len(pop)):
        # get the fitness for each recipe of the population
        value_fitness = value_fitness_function(flavor_matrix, single_ingredients_arr, pop[i])
        novel_fitness = novel_fitness_function(pop[i], MAX_NUM_OTHER_INGREDIENTS)
        recipe_fitness = novel_fitness + value_fitness
        pop_rank.append(recipe_fitness)
    # creates list of tuple based on two corresponding lists (index matches index) List of items (RECIPE OBJECT, fitness)
    fitness = list(zip(pop, pop_rank)) 
    # sorts by fitness
    rank_sorted = sorted(fitness, key=lambda x: x[1]) 
    # returns only string
    r = [individual[0] for individual in rank_sorted] 
    return r


'''
This method takes in the ranked_pop array, which contains the population of recipes sorted by rank. It then
chooses the number of recipes equivalent to the population size (the size of our population) by calling the choose_individual
method. This method returns an array of the population that will now be used for recombination.
    Params:
        @ranked_pop {arr[Recipe objs]}: list of recipes ranked by fitness
        @prob_list {arr[float]}: each index, i, contains the probability of selecting an individual at that index, i, from a ranked population 
    Return:
        @rank_selection_pop {arr[Recipe objs]}: an array of the recipes that will be used for recombination
'''
def rank_selection(ranked_pop, prob_list):
    rank_selection_pop = []
    for i in range(len(ranked_pop)):
        chosen_indiv = choose_individual(ranked_pop, prob_list)
        rank_selection_pop.append(chosen_indiv)

    return rank_selection_pop


'''
This method selects an individual index based of a randomly generated probability. It does so by iterating
throuhg the cumulative probabilites list and cheking if the randomly generated value(between 1-0) is greater
than the current index probability. If it is larger it means that this the individual(recipe) at this index
will be selected for breeding. The cumulative list allows for this itrative process.  
    Params:
        @pop {arr[Recipe obj]}: population of recipes to be sorted by rank
        @prob_list {arr[float]}: each index, i, contains the probability of selecting an individual at that index, i, from a ranked population 
    Return:
        @chosen_indiv {Recipe obj}: the chosen recipe object

'''
def choose_individual(pop, prob_list):
    p = random.uniform(0, 1)
    indiv_index = -99999 #so it doesn't break
    for i in range(len(prob_list)):
        cum_p = prob_list[i]
        #if probability is greater.
        if cum_p >= p: 
            indiv_index = i
            break
    chosen_indiv = pop[indiv_index] #select approprite individual
    return chosen_indiv