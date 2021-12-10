'''
Author: Jay Turnsek, Liam Johnston
Title: main.py

Main driver script for a-life simulation.
'''
# see updates plz

from individual import Individual
import random


def init_population(size: int):
    return [Individual('base') for i in range(size)]


def do_generation(population: list[Individual], predator_rate: float):

    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):

        # Predator showed up!! ahhhh scary
        if random.random() <= predator_rate:

            # 50/50 for baseline
            if random.random() < 0.5:
                i.setFoodState(True)
            else:
                j.setFoodState(False)
        else:
            i.setFoodState(True)
            j.setFoodState(False)

    if len(shuffled) % 2 == 1:
        # ADD ODD LEN HANDLING PROCEDURE
        print('odd')

    for i in shuffled:
        if i.hasFood():
            # reproduce, osmosis style. only if food was grabbed
            next_gen.append(i)
            next_gen.append(i)
    
    print(len(next_gen))
    return next_gen


def do_simulation(gens: int, size: int, predator_rate: float):

    population = init_population(size)
    for gen in range(gens):
<<<<<<< HEAD
        
        next_gen = do_generation(population, predator_rate)
        population = next_gen
        print(len(population))
        
=======
        do_generation(population, predator_rate)

>>>>>>> cfdc2d00e4785cd23012f1bccfc9174ea030974e

if __name__ == "__main__":
    # parameters
    N_GENS = 10
    POP_SIZE = 20
    PRED_RATE = 0.25

    do_simulation(
        N_GENS,
        POP_SIZE,
        PRED_RATE
    )
