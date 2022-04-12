from chromosome import chromosome
import population

# in this example i want to satisfy the
# expression a + b = 5
# I define a chromosome with 10 genes, the first 5 genes
# are for a, and the other 5 are for b.
# If a gene is 1, it will count as a contribute of 1 in the expansion
# of the given letter. Therefore if a = [0,1,1,1,1] = 4
# the fitness function returns how close we are to the wanted value

# define your own fitness function
def own_fitness_function(chromosome : chromosome):
    a = 0
    b = 0
    target_val = 5
    chromosome_list = chromosome.get_chromosome()
    
    for i in range(0,4):
        a += chromosome_list[i]
    for i in range(5,9):
        b += chromosome_list[i]
    
    actual_val = a + b
    
    # return a score which depends on the distance to the target value
    return 10 - abs(target_val - actual_val)

def main():

    # I create a population with chromosomes of length 10
    # Starting population is 10
    # The threshold for termination is 80%
    # The chance of mutation during crossover is 10%
    p = population.population(10,10,0.8,0.1)
    # assign the fitness function
    p.fitness_function = own_fitness_function

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