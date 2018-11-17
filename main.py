import heuristic_algorithms as ha
import heuristic_tools as ht
import genetic_algorithm as ga

def heuristic_trilogy():
    iteration_count = 20
    number_of_bits = 10
    tempeture = 10
    print "\n\nhill climber"
    solution_hill =  ha.hill_climber(iteration_count,number_of_bits)
    print "solution array:",solution_hill , "fitness:", ht.evaluate(solution_hill)

    print "\n\ntabu search"
    tabu_solution = ha.tabu_search(iteration_count, number_of_bits)
    print "solution array:",tabu_solution, "fitness:", ht.evaluate(tabu_solution) 

    print "\n\nsimulated annealing"
    solution =ha.simulated_annealing(tempeture, iteration_count, number_of_bits)
    print "solution array:",solution, "fitness:", ht.evaluate(solution)

def main():
    #heuristic_trilogy()

    print "\n\npop size experiment"
    iterate_ga(generation_count = 10, population_size = 10, 
            crossover_rate = 0.7, mutation_rate = 0.1, bit_count = 20)
    iterate_ga(generation_count = 10, population_size = 80, 
            crossover_rate = 0.7, mutation_rate = 0.1, bit_count = 20)
    print "------------------------------------------------------------------"
    
    print "\n\ncrossover rate experiment"
    iterate_ga(generation_count = 10, population_size = 10, 
            crossover_rate = 0.8, mutation_rate = 0.1, bit_count = 20)
    iterate_ga(generation_count = 10, population_size = 10, 
            crossover_rate = 0.2, mutation_rate = 0.1, bit_count = 20)
    print "------------------------------------------------------------------"

    print "\n\nmutation rate experiment"
    iterate_ga(generation_count = 10, population_size = 10, 
            crossover_rate = 0.7, mutation_rate = 0.1, bit_count = 20)
    iterate_ga(generation_count = 10, population_size = 10, 
            crossover_rate = 0.7, mutation_rate = 0.8, bit_count = 20)
    print "------------------------------------------------------------------"

def iterate_ga(generation_count, population_size,
        crossover_rate, mutation_rate, bit_count) :

    print "Genetic Algorithm\n"
    best = 0
    worst = 10000
    all_fitness_sum = 0
    for i in range(10) :
        solution_ga =ga.genetic_algorithm(generation_count, population_size, 
                crossover_rate, mutation_rate, bit_count)

        current_fitness = solution_ga[1]

        all_fitness_sum += current_fitness

        if best < current_fitness :
            best = current_fitness

        if worst > current_fitness:
            worst = current_fitness
        
        
    print "generation_count:", generation_count, "population_size:",  population_size, "crossover_rate:",  crossover_rate, "mutation_rate:", mutation_rate, "bit_count:",  bit_count
    print "best: ", best, "worst: ", worst, "avarage: ", all_fitness_sum/10

main()
