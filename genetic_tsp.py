import random
import pdb

TOURNEMET_SIZE = 2


class GeneticAlgorithm:

    def __init__(self, generation_count, population_size, crossover_rate,
                 mutation_rate):
        self.generation_count = generation_count
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.genom_size = 0
        self.capacity = 0
        self.weights = []
        self.values = []
        self.load_data()

    def load_data(self):
        problem = "p06"

        # read values
        file_type = "_p.txt"
        file_name = problem + file_type
        file = open(file_name, "r")
        for line in file:
            self.values.append(int(line))
        file.close()

        # pdb.set_trace()
        self.genom_size = len(self.values)

        # read capacity
        file_type = "_c.txt"
        file_name = problem + file_type
        file = open(file_name, "r")
        capacity = int(file.readline())
        file.close()

        # read weights
        file_type = "_w.txt"
        file_name = problem + file_type
        file = open(file_name, "r")
        for line in file:
            self.weights.append(int(line))
        file.close()

    def flip_bit(self, genom, index):
        new_genom = genom.copy()
        new_genom[index] = ~genom[index]+2
        return new_genom

    def evaluate(self, genom):
        knapsack_value = 0
        knapsack_weight = 0
        for i in range(self.genom_size):
            if genom[i] == 1:
                knapsack_value += self.values[i]
                knapsack_weight += self.weights[i]

        return {'value': knapsack_value, 'weight': knapsack_weight}

    def initialize_population(self):
        return [self.initialize_genom() for _ in range(self.population_size)]

    def initialize_genom(self):
        return [random.randint(0, 1) for _ in range(self.genom_size)]

    def create_childs(self, parents):
        # crossover parents using random index
        index = random.randint(0, self.genom_size)

        i = 0
        if random.random() < self.crossover_rate:
            # pdb.set_trace()
            child1 = parents[i][:index]
            child1.extend(parents[i+1][index:])

            child2 = parents[i+1][:index]
            child2.extend(parents[i][index:])
        else:
            child1 = parents[0]
            child2 = parents[1]

        # mutation
        if random.random() < self.mutation_rate:
            mutation_index = random.randint(0, self.genom_size*2 - 1)
            if mutation_index >= self.genom_size:
                mutation_index -= self.genom_size
                child1 = self.flip_bit(child1, mutation_index)
            else:
                child2 = self.flip_bit(child2, mutation_index)

        return child1, child2
    def get_worst_genom(self, genoms):
        worst_fitness = 0
        worst_genom = []

        for genom in genoms:
            current_fitness = self.evaluate(genom)['value']
            if current_fitness > worst_fitness:
                worst_genom = genom

        return worst_genom

    def get_best_genom(self, genoms):
        best_fitness = 0
        best_genom = []

        for genom in genoms:
            current_fitness = self.evaluate(genom)['value']
            if current_fitness > best_fitness:
                best_genom = genom

        return best_genom

    def tournement_selection(self, genoms):
        contenders = []
        t_size = TOURNEMET_SIZE
        for i in range(t_size):
            random_index = random.randint(0, self.population_size - 1)
            contenders.append(genoms[random_index])

        return self.get_best_genom(contenders)

    def run(self):
        population = self.initialize_population()
        very_best_genom_fitness = 0
        very_best_genom = population[0]

        for i in range(self.generation_count):
            childs = []
            for j in range(int(self.population_size / 2)):
                parents = [self.tournement_selection(population) for _ in
                           range(2)]
                childs.extend(self.create_childs(parents))

            #bootleg elitism. delete the worst add the best from previous
            #generaion
            best_previous = self.get_best_genom(population)
            population = childs.copy()
            population.remove(self.get_worst_genom(population))
            population.append(best_previous)

            current_genom = self.get_best_genom(childs)
            current_genom_fitness = self.evaluate(current_genom)['value']
            if very_best_genom_fitness < current_genom_fitness:
                very_best_genom_fitness = current_genom_fitness
                very_best_genom = current_genom

        return very_best_genom, very_best_genom_fitness
