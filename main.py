from chromosome import chromosome
import population

# define your own fitness function
def fitness_function(chromosome : chromosome):
    return 0

def main():

    # I create a population with chromosomes of length 5
    # Starting population is 10
    # The threshold for termination is 80%
    # The chance of mutation during crossover is 50%
    p = population.population(5,10,0.8,0.5)

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
    
    print(f"Final population is {p}")
    print(f"I'm performing the last selection for best solutions")
    p.selection(3)
    print(f"Best solutions {p}")

if __name__ == "__main__":
    main()