from random import randint, random
import chromosome

class population():
    def __init__(self,number_of_genes,number_of_initial_pop,threshold,mutation_prob) -> None:
        # define empty population set
        self._population = []
        self._threshold = threshold
        self._mutation = mutation_prob

        for i in range(0,number_of_initial_pop):
            self._population.append(chromosome.chromosome(number_of_genes))

    def __str__(self) -> str:
        initial_string = "\nPopulation\n"

        for c in self._population:
            initial_string +=str(c.get_chromosome()) + "\t Fitness: "+ str(self.fitness_function(c)) + '\n'
        
        return initial_string
    
    def fitness_function(self,chromosome):
        # default fitness function, can be overriden
        # gets a chromosome and returns how much it is fit on a scale of 0 to 255
        fitness = 0
        MAX = 255
        for i in range(0,len(chromosome.get_chromosome())):
            if (i % 2 == 0):
                # if gene is even returns a contribute of
                if (chromosome.get_chromosome()[i] == 1):
                    fitness += MAX/(len(chromosome.get_chromosome())/2)
                #else:
                   # fitness -= MAX/len(chromosome.get_chromosome())
        
        return fitness
    
    def selection(self,top_n_chromosomes):
        fitness_list = []
        new_population = []
        
        for i in range(0,top_n_chromosomes):
            max_fit = 0
            max_chromo = 0
            for chromosome in self._population:
                if (self.fitness_function(chromosome) >= max_fit):
                    max_fit = self.fitness_function(chromosome)
                    max_chromo = chromosome
            # at the end add to the new population
            new_population.append(max_chromo)
            # remove it from the old population
            self._population.remove(max_chromo)
        
        # at the end, overwrite the old population with the new
        self._population = new_population
    
    def crossover(self):
        new_offspring = []
        ret_val = 0

        for i in range(0,len(self._population)):
            for j in range(i,len(self._population)):
                if (i != j):
                    # i can't reproduce with myself
                    print(self._population[i].get_chromosome())
                    print(self._population[j].get_chromosome())
                    tmp_offspring = self._population[i].crossover(self._population[j])
                    for offspring in tmp_offspring:
                        new_offspring.append(offspring)
        # after crossover perform mutation
        for offspring in new_offspring:
            # mutate with 50% probability
            offspring.mutate(self._mutation)
        
        ret_val = self.terminate(new_offspring)
        # add the new offspring to the existing population
        self._population.extend(new_offspring)

        return ret_val
    
    #threshold is a number ranging from 0 to 1
    def terminate(self, new_pop):
        equal = 0

        for offspring in new_pop:
            for parent in self._population:
                print(parent.get_chromosome())
                if (offspring.get_chromosome() == parent.get_chromosome()):
                    print(f"Found {offspring.get_chromosome()} == {parent.get_chromosome()}")
                    equal += 1
                    break
        
        # at the end compute the percentile
        equal /= len(new_pop)
        if (equal >= self._threshold):
            return 1
        
        return 0

        
        
        
        
    
    