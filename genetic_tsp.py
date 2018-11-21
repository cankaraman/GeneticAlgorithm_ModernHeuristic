import random
import pdb

TOURNEMET_SIZE = 2


class GeneticAlgorithm:

    def __init__(self, generation_count, population_size, crossover_rate,
                 mutation_rate, constraint_handle_type, problem):
        self.generation_count = generation_count
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.constraint_handle_type = constraint_handle_type
        self.problem = problem
        self.genom_size = 0
        self.capacity = 0
        self.weights = []
        self.values = []
        self.load_data()

    def load_data(self):
        problem = self.problem

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
        self.capacity = int(file.readline())
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
        #if index > len(genom):
        #    return new_genom

        try:
            new_genom[index] = ~genom[index]+2
        except:
            pass
        return new_genom

    def evaluate(self, genom):
        knapsack_value = 0
        knapsack_weight = 0
        if len(genom) < self.genom_size:
            return {'value': 0, 'weight': self.capacity * 2}
        for i in range(self.genom_size):
            try:
                if genom[i] == 1:
                    knapsack_value += self.values[i]
                    knapsack_weight += self.weights[i]
            except TypeError:
                # pdb.set_trace()
                pass
            except IndexError:
                #pdb.set_trace()
                pass

        return {'value': knapsack_value, 'weight': knapsack_weight}

    def initialize_population(self):
        return [self.initialize_genom() for _ in range(self.population_size)]

    def initialize_genom(self):
        return [random.randint(0, 1) for _ in range(self.genom_size)]

    def create_childs(self, parents):
        # crossover parents using random index
        index = random.randint(0, self.genom_size)
        if len(parents) < 2:
            return parents[0], parents[0]

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
            # if not genom:
            #    pdb.set_trace()
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
        self.population_size = len(genoms)
        for i in range(t_size):
            random_index = random.randint(0, self.population_size - 1)
            contenders.append(genoms[random_index])

        return self.get_best_genom(contenders)

    def penalty(self, genom, weight):
        return "penalty", genom

    def repair(self, genom, weight):
        index = random.randint(0, len(genom)-1)
        genom = self.flip_bit(genom, index)
        genom_weight = self.evaluate(genom)['weight']
        while genom_weight > self.capacity:
            index = random.randint(0, len(genom)-1)
            genom = self.flip_bit(genom, index)
            genom_weight = self.evaluate(genom)['weight']

        return "repair", genom

    def death(self, genom, weight):
        return "death", genom

    def handle(self, current_genom, current_genom_weight):
        handle_method = {
            'penalty': self.penalty,
            'repair': self.repair,
            'death': self.death
        }[self.constraint_handle_type]
        return handle_method(current_genom, current_genom_weight)

    def run(self):
        population = self.initialize_population()
        very_best_genom_fitness = 0
        very_best_genom = None
        very_best_genom_weight = 0

        for i in range(self.generation_count):
            childs = []
            for j in range(int(self.population_size / 2)):
                parents = [self.tournement_selection(population) for _ in
                           range(2)]
                childs.extend(self.create_childs(parents))

            # bootleg elitism. delete the worst add the best from previous
            # generaion
            best_previous = self.get_best_genom(population)
            population = childs.copy()
            worst_genom = self.get_worst_genom(population)
            if worst_genom in population:
                population.remove(self.get_worst_genom(population))
            population.append(best_previous)
            self.population_size = len(population)

            # childs comes back empty
            # if not childs:
            #    continue
            current_genom = self.get_best_genom(childs)
            #if not current_genom:
            #    pdb.set_trace()
            current_genom_info = self.evaluate(current_genom)
            current_genom_weight = current_genom_info['weight']

            handle_type = ""
            if current_genom_weight > self.capacity:
                handle_result = self.handle(
                    current_genom, current_genom_weight)
                current_genom = handle_result[1]
                handle_type = handle_result[0]

                if handle_type == "death" and current_genom in population:
                    handle_type = ""
                    population.remove(current_genom)
                    population.append(self.initialize_genom())
                    self.population_size = len(population)
                    current_genom_info['value'] = 0
                elif handle_type == "penalty" and current_genom in population:
                    handle_type = ""
                    current_genom_info['value'] -= (
                        current_genom_info['value']/3)*2

                else:
                    handle_type = ""
                    current_genom_info = self.evaluate(current_genom)

            current_genom_fitness = current_genom_info['value']
            if (very_best_genom_fitness < current_genom_fitness and
                    current_genom_weight <= self.capacity):
                very_best_genom_fitness = current_genom_fitness
                very_best_genom_weight = current_genom_weight
                very_best_genom = current_genom

        # if current_genom_weight > self.capacity:
        #    pdb.set_trace()
        if very_best_genom is not None:
            vbg_info = self.evaluate(very_best_genom)
            return very_best_genom, vbg_info['value'], vbg_info['weight'], self.capacity
