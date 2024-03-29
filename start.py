from population import Population


def main():
    pop_size = 200
    target = "To be or not to be."
    mutation_rate = 0.01

    pop = Population(pop_size, mutation_rate, target)

    # you don't need to call this function when the ones right bellow are fully implemented
    pop.print_population_status()

    """
    Uncomment these lines bellow when you implement all the functions
    
    while not pop.finished:
        pop.evolve()
        pop.print_population_status()
    """


if __name__ == "__main__":
    main()
