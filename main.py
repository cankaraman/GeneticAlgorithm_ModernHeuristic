import genetic_tsp as gt

def print_result(death, penalty, repair):
    print("death")
    print_method(death)
    print("penalty")
    print_method(penalty)
    print("repair")
    print_method(repair)

def print_method(results):
    total = 0
    best = 0
    worst = 99999999
    count = 0
    for res in results:
        if res is not None:
            value = res[1]
            total += value

            if value > best:
                best = value
            
            if value < worst:
                worst = value

            count += 1

    print("avarage: ",round(total/ count, 1), "best: ", best, "worst: ", worst)


def p06():
    res_penalty = []
    res_death = []
    res_repair = []
    problem = "p06"
    for _ in range(10):
        ga1 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "penalty",problem)
        res_penalty.append(ga1.run())

        ga2 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "death",problem)
        res_death.append(ga1.run())

        ga3 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "repair",problem)
        res_repair.append(ga1.run())

    print("\n",problem)
    print_result(res_death, res_penalty, res_repair)

def p07():
    res_penalty = []
    res_death = []
    res_repair = []
    problem = "p07"
    for _ in range(10):
        ga1 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "penalty",problem)
        res_penalty.append(ga1.run())

        ga2 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "death",problem)
        res_death.append(ga1.run())

        ga3 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "repair",problem)
        res_repair.append(ga1.run())

    print("\n",problem)
    print_result(res_death, res_penalty, res_repair)

def p08():
    res_penalty = []
    res_death = []
    res_repair = []
    problem = "p08"
    for _ in range(10):
        ga1 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "penalty",problem)
        res_penalty.append(ga1.run())

        ga2 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "death",problem)
        res_death.append(ga1.run())

        ga3 = gt.GeneticAlgorithm(20, 10, 0.8, 0.1, "repair",problem)
        res_repair.append(ga1.run())

    print("\n",problem)
    print_result(res_death, res_penalty, res_repair)

def main():
    p06()
    p07()
    p08()

main()
