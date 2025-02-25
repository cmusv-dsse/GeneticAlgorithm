from population import Population


def genetic_algorithm(pop_size, mutation_rate, target):
    pop = Population(pop_size, mutation_rate, target)

    pop.create_initial_population()

    while not pop.finished:
        pop.evolve()
        pop.print_population_status()


def main():
    pop_size = 200
    target = "To be or not to be."
    mutation_rate = 0.01

    genetic_algorithm(pop_size, mutation_rate, target)


if __name__ == "__main__":
    main()
