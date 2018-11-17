import numpy as np
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
		#print i, "current fitness", currentFitness, "Current neighbor", currentNeighbor
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
		#print i, "current fitness", currentFitness, "Current neighbor", currentNeighbor
		if currentFitness > bestFitness:
			bestNeighbor = np.copy(currentNeighbor)
			bestFitness = currentFitness
                        best_index = i

        #tabu_list[best_index] = array_size/2
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
	
