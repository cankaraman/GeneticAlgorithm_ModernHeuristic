import heuristic_tools as ht
import numpy as np

TOURNEMET_SIZE = 2

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
    #crossover parents using random index
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

