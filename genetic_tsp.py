import random

class GeneticAlgorithm:
    TOURNEMET_SIZE = 2

    def __init__(self, generation_count, population_size, crossover_rate,
                 mutation_rate, genom_size):
        self.generation_count = generation_count
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.genom_size = genom_size
        self.capacity = 0
        self.weights = []
        self.values = []
        self.load_data()

    def load_data(self)
        file_header = ""
        problem = ""

        #read values
        file_type = ""
        file_name = file_header + problem + file_type
        file = open(file_name, "r")
        for line in file:
            self.values.append(int(line))
        file.close()

        #read capacity
        file_type = ""
        file_name = file_header + problem + file_type
        file = open(file_name, "r")
        capacity = int(file.readline())
        file.close()

        #read weights
        file_type = ""
        file_name = file_header + problem + file_type
        file = open(file_name, "r")
        for line in file:
            self.weights.append(int(line))
        file.close()


    def flip_bit(self, genom, index):
        newBitArray = genom.copy()
        newBitArray[index] = ~bit_array[index]+2
        return newBitArray

    def evaluate(self, genom):
        knapsack_value = 0
        knapsack_weight = 0
        for i in range(self.genom_size):
            if genom[i] == 1:
                knapsack_value = self.values[i]
                knapsack_weight = self.weights[i]

        return {'value': knapsack_value, 'weight': knapsack_weight}


    def initialize_population(self):
        return [self.initialize_genom() for _ in range(self.population_size)]

    def initialize_genom(self):
        return [random.randint(0, 1) for _ in range(self.genom_size)]

    def create_childs(self, parents):
        # crossover parents using random index
        index = random.randint(0, genom_size)

        i = 0
        if random.random() < crossover_rate:
            child1 = parents[i][:index]
            child1.extend(parents[i+1][index:])

            child2 = parents[i+1][:index]
            child2.extend(parents[i][index:])
        else:
            child1 = parents[0]
            child2 = parents[1]

        # mutation
        if random.random() < mutation_rate:
            mutation_index = random.randint(bit_count*2)
            if mutation_index >= bit_count:
                mutation_index -= bit_count
                child1 = self.flip_bit(child1, mutation_index)
            else:
                child2 = self.flip_bit(child2, mutation_index)

        return child1, child2

    def get_best_genom(self, genoms):
        best_fitness = 0
        best_genom = genoms[0]

        for genom in genoms:
            current_fitness = self.evaluate(genom)['value']
            if current_fitness > best_fitness:
                best_genom = genom

        return best_genom

    def tournement_selection(genoms):
        contenders = []
        t_size = TOURNEMET_SIZE
        for i in range(t_size):
            random_index = random.randint(0, population_size)
            contenders.append(genoms[random_index])

        return get_best_genom(contenders)

    def run(self):
        # not yet rearranged
        population = self.initialize_population()
        very_best_genom_fitness = 0
        very_best_genom = population[0]

        for i in range(self.generation_count):
            childs = []
            for j in range(self.population_size / 2):
                parents = select_parents(population, TOURNEMET_SIZE)
                childs.extend(create_childs(
                    parents, crossover_rate, mutation_rate, bit_count))

            current_genom = get_best_genom(childs, bit_count)
            current_genom_fitness = ht.evaluate(current_genom)
            if very_best_genom_fitness < current_genom_fitness:
                very_best_genom_fitness = current_genom_fitness
                very_best_genom = current_genom

        return very_best_genom, very_best_genom_fitness
