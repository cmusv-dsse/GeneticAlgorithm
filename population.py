from individual import Individual
import random


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
        self.mating_pool = []

    # Create a random initial population randomly
    def create_initial_population(self):
        for i in range(self.size):
            ind = Individual(self.target)

            if ind.fitness > self.best_ind.fitness:
                self.best_ind.fitness = ind.fitness

            self.population.append(ind)

    # Evolve population applying natural selection
    def evolve(self):
        # Generate a mating pool according to the probability of each individual being selected (fitness)
        self.mating_pool = []

        # creating a mating pool based on the individual fitness
        for index, individual in enumerate(self.population):
            prob = int(round(individual.fitness * 100))
            self.mating_pool.extend(index for _ in range(prob))

        self._generate_new_population()

    # Generate the new population based on the natural selection function
    def _generate_new_population(self):
        new_population = []

        for i in range(self.size):
            # selection
            partner_a, partner_b = self._selection()

            # crossover
            offspring = partner_a.crossover(partner_b)

            # mutation
            offspring.mutate(self.mutation_rate)

            offspring.calc_fitness(self.target)

            # evaluate the offspring
            self._evaluate_offspring(offspring)

            new_population.append(offspring)

        self.population = new_population
        self.generations += 1

    # Select two individuals for crossover
    def _selection(self):
        pool_len = len(self.mating_pool)

        i_partner_a = self.mating_pool[random.randint(0, pool_len - 1)]
        i_partner_b = self.mating_pool[random.randint(0, pool_len - 1)]

        partner_a = self.population[i_partner_a]
        partner_b = self.population[i_partner_b]

        return partner_a, partner_b

    # Compute/Identify the current "most fit" individual within the population
    def _evaluate_offspring(self, offspring):
        if offspring.fitness == self.perfect_score:
            self.finished = True

        if offspring.fitness > self.best_ind.fitness:
            self.best_ind = offspring

    def print_population_status(self):
        print("\nGeneration " + str(self.generations))
        print("Best individual: " + str(self.best_ind))
