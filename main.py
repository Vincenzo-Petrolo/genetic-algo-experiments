import population

def main():

    p = population.population(5,10,0.8,0)

    print(f"Created population {str(p)}")
    
    terminate = 0
    i = 1
    while (terminate == 0):
        # select top 3 parents for crossover
        p.selection(3)
        print(f"New population after selection is {p}")
        # perform crossover
        terminate = p.crossover()
        print(f"New population at generation {i} is {p}")
        i += 1

if __name__ == "__main__":
    main()