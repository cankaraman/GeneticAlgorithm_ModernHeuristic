import numpy as np
import heuristic_tools as ht
import math

def hill_climber(iterationCount, numberOfBits):
	veryBestFitness = -1
	for outerIndex in range(iterationCount):

		bitArray = ht.initializeSolution(numberOfBits)
		bestFitness = ht.evaluate(bitArray)
		bestNeighbor = bitArray
		bitArraySize = len(bitArray)
		local = False
		#pdb.set_trace()

		while not local:
			currentBestNeighbor = ht.getBestNeighbor(bestNeighbor)
			currentBestFitness = ht.evaluate(currentBestNeighbor)
                        print currentBestNeighbor ,currentBestFitness 
			if currentBestFitness > bestFitness:
				bestNeighbor = np.copy(currentBestNeighbor)	
				bestFitness = currentBestFitness
			else: local = True

		if bestFitness == bitArraySize: 
			veryBestNeighbor = np.copy(bestNeighbor)
			break
		if bestFitness > veryBestFitness :
			veryBestFitness = bestFitness
			veryBestNeighbor = np.copy(bestNeighbor)

	return veryBestNeighbor 

def simulated_annealing(tempeture, iteration_count, number_of_bits):
	
    bitArray = ht.initializeSolution(number_of_bits)
    bestFitness = ht.evaluate(bitArray)
    bestNeighbor = bitArray
    current_neighbor = bitArray

    very_best_fitness = bestFitness
    very_best_neighbor = bestNeighbor 

    for outer_index in range(iteration_count):
        for inner_index in range(2*number_of_bits):
            current_neighbor = ht.get_random_neighbor(current_neighbor)
            current_fitness = ht.evaluate(current_neighbor)
            dif = float(current_fitness - bestFitness)
            posb = math.exp( dif / tempeture) 

            if bestFitness < current_fitness:
                bestFitness = current_fitness
                bestNeighbor = current_neighbor
               #print bestNeighbor, bestFitness
            elif bestFitness == number_of_bits:	#if it's best possible return solution
                return bestNeighbor
            elif np.random.uniform() < math.exp(
                    float(current_fitness - bestFitness) / tempeture): 
                #print "dif: ", dif,  "tempeture: ", tempeture,"posb: ", posb
                bestFitness = current_fitness
                bestNeighbor = current_neighbor
                print bestNeighbor, bestFitness
            
        print bestNeighbor, bestFitness
        if bestFitness == number_of_bits:
            return bestNeighbor

        if tempeture>1 :
            tempeture -= 1

    if bestFitness > very_best_fitness:
        very_best_fitness = bestFitness
        very_best_neighbor = bestNeighbor

    return very_best_neighbor

def tabu_search(iteration_count, number_of_bits):

    global_best_neighbor = ht.initializeSolution(number_of_bits)
    global_best_fitness = ht.evaluate(global_best_neighbor)

    for outer_index in range(iteration_count):
        bitArray = ht.initializeSolution(number_of_bits)
        bestFitness = ht.evaluate(bitArray)
        bestNeighbor = bitArray
        current_neighbor = bitArray
        tabu_list = ht.get_clean_tabu_list(number_of_bits)

        for inner_index in range(2*number_of_bits):
            current_neighbor_tuple = ht.get_best_neighbor_without_tabu(current_neighbor, 
                                                                        tabu_list)
            current_neighbor = current_neighbor_tuple[0]
            current_neighbor_index = current_neighbor_tuple[1]  #this value holds the changed in
            current_fitness = ht.evaluate(current_neighbor)

            print current_neighbor, current_fitness
            if current_fitness > bestFitness :
                bestFitness = current_fitness
                bestNeighbor = current_neighbor
                tabu_list[current_neighbor_index] = number_of_bits/2
            if bestFitness == number_of_bits:
                return bestNeighbor

        if global_best_fitness < bestFitness :
            global_best_fitness = bestFitness
            global_best_neighbor = bestNeighbor

    return global_best_neighbor
