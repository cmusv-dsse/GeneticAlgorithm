from individual import Individual


class Population:
    """
        A class that describes a population of virtual individuals
    """

    def __init__(self, size, mutation_rate, target):
        self.population = []
        self.size = size
        self.generations = 0
        self.target = target
        self.mutation_rate = mutation_rate
        self.best_ind = Individual(target)
        self.finished = False
        self.perfect_score = 1.0
        self.average_fitness = 0.0
        self.mating_pool = []

        self.create_initial_population(size, target)

    # Create a initial population randomly
    def create_initial_population(self, size, target):
        for i in range(size + 1):
            ind = Individual(self.target)
            ind.calc_fitness(target)

            if ind.fitness > self.best_ind.fitness:
                self.best_ind.fitness = ind.fitness

            self.average_fitness += ind.fitness
            self.population.append(ind)
        self.average_fitness /= size

    def print_population_status(self):
        print("\nGeneration " + str(self.generations))
        print("Population Average fitness: " + str(self.average_fitness))
        print("Best individual: " + str(self.best_ind))

    # Evolve population applying natural selection
    def evolve(self):
        # Generate a mating pool according to the probability of each individual
        """
            Implementation suggestion based on Lab:
            Based on fitness, each member will get added to the mating pool a certain number of times.
                a higher fitness = more entries to mating pool = more likely to be picked as a parent
                a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
            pass
        """

    # Generate the new population based on the natural selection function
    def generate_new_population(self):
        pass

    # Select two individuals for crossover
    def _selection(self):
        pass

    # Compute/Identify the current "most fit" individual within the population
    def _evaluate_offspring(self):
        pass
