import genetic_tsp as gt

def main():
    ga = gt.GeneticAlgorithm(20,10,0.8,0.1)
    res = ga.run()

    print(res)

main()
