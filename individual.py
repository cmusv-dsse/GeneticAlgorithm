import random
import string


class Individual:
    """
        Individual in the population
    """

    def __init__(self, target):
        self.fitness = 0
        self.genes = self.generate_random_genes(len(target))
        self.calc_fitness(target)

    @staticmethod
    def generate_random_genes(size):
        genes = []

        for i in range(size):
            genes.append(random.choice(string.printable))

        return genes

    def __repr__(self):
        return ''.join(self.genes) + " -> fitness: " + str(self.fitness)

    # Fitness function: returns a floating points of "correct/matching" characters
    def calc_fitness(self, target):
        score = 0  # number of matching genes
        index = 0

        # insert your logic to calculate the individual fitness here
        for gene in self.genes:
            if gene == target[index]:
                score += 1
            index += 1

        self.fitness = score / len(target)

    # The crossover function selects pairs of individuals to be mated, generating a third individual (offspring)
    def crossover(self, partner):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        child = Individual(self.genes)

        midpoint = random.randint(0, len(self.genes))
        child.genes = self.genes[:midpoint] + partner.genes[midpoint:]

        return child

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate):
        # code to mutate the individual here
        for elem in enumerate(self.genes):
            if random.uniform(0, 1) < mutation_rate:
                self.genes[elem[0]] = random.choice(string.printable)

    def __str__(self):
        return ''.join(self.genes) + " -> fitness: " + str(self.fitness)
