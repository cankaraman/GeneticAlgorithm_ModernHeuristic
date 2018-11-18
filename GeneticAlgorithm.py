from random import randint


class GeneticAlgorithm:
    TOURNEMET_SIZE = 2

    def __init__(self, generation_count, population_size, crossover_rate,
                 mutation_rate, genom_size):
        self.generation_count = generation_count
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.genom_size = genom_size

    def evaluate(genom):
        raise NotImplementedError("implement this please")

    def tournement_selection(population):
        contenders = []
        t_size = TOURNEMET_SIZE
        for i in range(t_size):
            random_index = random.randint(0, population_size)
            contenders.append(population[random_index])

        best_fitness = 0
        for genom in contenders:
            curren_fitness = evaluate(genom)
            if(current_fitness > best_fitness):
                best_fitness = current_fitness
                best_solution = contenders[j]

        return best_solution


#############################################################################
import heuristic_tools as ht
import numpy as np

def tournement_selection(population_list, tournement_size):
    genom_size = len(population_list)
    contenders = []
    for i in range(tournement_size) :
        index = np.random.randint(genom_size)
        contenders.append(population_list[index])

    best_fitness = 0
    for j in range(tournement_size) :
        current_fitness = ht.evaluate(contenders[j])
        if(current_fitness > best_fitness) :
            best_fitness = current_fitness
            best_solution = contenders[j]
    
    return best_solution

def initialize_population(population_size, bit_count):
   population = [] 
   for i in range(population_size) :
        population.append(ht.initializeSolution(bit_count))

   return population

def select_parents(population_list, tournement_size):
    parents= []
    for i in range(2) :
        parents.append(tournement_selection(population_list, tournement_size))

    return parents

def create_childs(parents, crossover_rate, mutation_rate, bit_count) :
    # crossover parents using random index
    index = np.random.randint(bit_count)
    
    i = 0
    if np.random.uniform() < crossover_rate :
        child1 = parents[i][:index].tolist() 
        child1.extend(parents[i+1][index:])

        child2 = parents[i+1][:index].tolist() 
        child2.extend(parents[i][index:])
    else :
        child1 = parents[0]
        child2 = parents[1]
        
    if np.random.uniform() < mutation_rate :
        mutation_index = np.random.randint(bit_count*2)
        if mutation_index >= bit_count :
            mutation_index -= bit_count
            child1 = ht.flip_bit(child1, mutation_index)
        else :
            child2 = ht.flip_bit(child2, mutation_index)

    return child1, child2

def get_best_genom(population_list, bit_count) :
    best_fitness = 0
    best_genom = population_list[0]

    for genom in population_list :
        current_fitness = ht.evaluate(genom)
        if current_fitness > best_fitness :
            best_genom = genom

    return best_genom


def genetic_algorithm(generation_count, population_size, crossover_rate, 
        mutation_rate, bit_count):

    population_list = initialize_population(population_size, bit_count)
    very_best_genom_fitness = 0
    very_best_genom = population_list[0]

    for i in range(generation_count) :
        childs = []
        for j in range(population_size / 2) :
            parents = select_parents(population_list,TOURNEMET_SIZE)
            childs.extend(create_childs(parents,crossover_rate, mutation_rate, bit_count))
        
        current_genom = get_best_genom(childs,bit_count)
        current_genom_fitness =ht.evaluate(current_genom)
        if very_best_genom_fitness < current_genom_fitness :
            very_best_genom_fitness = current_genom_fitness 
            very_best_genom = current_genom

    return very_best_genom, very_best_genom_fitness

import pdb

def evaluate(bit_array):
	array_size = len(bit_array)
	fitness = 0	

	for index in range(array_size):
		if index % 2 == 0 and bit_array[index] == 1:
			fitness +=1
		elif index % 2 == 1 and bit_array[index] == 0:
			fitness +=1

	return fitness

def flip_bit(bit_array, index):
	newBitArray =np.copy(bit_array)
	newBitArray[index]=~bit_array[index]+2
	return newBitArray

def get_random_neighbor(bit_array):
	bit_array_size = len(bit_array)
	random_index = np.random.randint(bit_array_size)
	return flip_bit(bit_array,random_index)

def getBestNeighbor(bit_array):
	array_size = len(bit_array)
	bestFitness = -1
	currentFitness =-1
	
	for i in range(array_size):
		currentNeighbor = flip_bit(bit_array, i)		
		currentFitness = evaluate(currentNeighbor)
		# print i, "current fitness", currentFitness, "Current neighbor", currentNeighbor
		if currentFitness > bestFitness:
			bestNeighbor = np.copy(currentNeighbor)
			bestFitness = currentFitness
	return bestNeighbor		

def get_best_neighbor_without_tabu(bit_array, tabu_list):
	array_size = len(bit_array)
	bestFitness = -1
	currentFitness =-1
	
	for i in range(array_size):
                if tabu_list[i]>0:
                    continue
		currentNeighbor = flip_bit(bit_array, i)		
		currentFitness = evaluate(currentNeighbor)
		# print i, "current fitness", currentFitness, "Current neighbor", currentNeighbor
		if currentFitness > bestFitness:
			bestNeighbor = np.copy(currentNeighbor)
			bestFitness = currentFitness
                        best_index = i

        # tabu_list[best_index] = array_size/2
	return bestNeighbor, best_index

def get_clean_tabu_list(array_size):
    tabu_list = [0] * array_size
    return tabu_list 

def decrement_tabu_list(tabu_list):
    for bit in tabu_list:
        if bit > 0:
            bit -= 1
		
def initializeSolution(numberOfBits):
	return np.random.randint(2,size=numberOfBits)
	
