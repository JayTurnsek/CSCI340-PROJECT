'''
Author: Jay Turnsek, Liam Johnston
Title: main.py

Main driver script for a-life simulation.
'''
# see updates plz

from individual import Individual
import random
import matplotlib.pyplot as plt

def init_population(size: int):
    return [Individual('base') for _ in range(size)]


def handle_predator(ind1, ind2):

    if ind1.behavior == 'base' and ind2.behavior == 'base':
        # 50/50 for baseline
        if random.random() < 0.5:
            ind1.setFoodState(True)
        else:
            ind2.setFoodState(True)
    
    elif ind1.behavior == 'selfish' and ind2.behavior == 'selfish':
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)
    
    elif ind1.behavior == 'selfless' and ind2.behavior == 'selfless':
        if random.random() < 0.5:
            ind1.setFoodState(True)
        else:
            ind2.setFoodState(True)
    
    elif ind1.behavior == 'selfish' and ind2.behavior == 'selfless':
        ind1.setFoodState(True)
        if random.random() < 0.5:
            ind2.setFoodState(True)

    elif ind1.behavior == 'selfless' and ind2.behavior == 'selfish':
        ind2.setFoodState(True)
        if random.random() < 0.5:
            ind1.setFoodState(True)


def do_generation(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):
        
        # Predator showed up!! ahhhh scary
        if random.random() <= predator_rate:

            handle_predator(i, j)
        else:
            i.setFoodState(True)
            j.setFoodState(True)


    food_count = 0
    for i in shuffled:
        if i.hasFood():
            food_count += 1
            if random.random() < reprod_rate:
                # reproduce, osmosis style. only if food was grabbed
                child1 = Individual('base')
                child2 = Individual('base')
                next_gen.append(child1)
                next_gen.append(child2)

    return next_gen, len(next_gen)


def do_generation_selfish_selfless(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):
        
        # Predator showed up!! ahhhh scary
        if random.random() <= predator_rate:

            handle_predator(i, j)
        else:
            i.setFoodState(True)
            j.setFoodState(True)

    food_count = 0
    for i in shuffled:
        if i.hasFood():
            food_count += 1
            if random.random() < reprod_rate:
                # reproduce, osmosis style. only if food was grabbed
                child1 = Individual(i.behavior)
                child2 = Individual(i.behavior)
                next_gen.append(child1)
                next_gen.append(child2)

    selfish_count, selfless_count = 0, 0
    for individual in population:
        if individual.behavior == 'selfish':
            selfish_count += 1
        if individual.behavior == 'selfless':
            selfless_count += 1
    
    return next_gen, selfish_count/len(population), selfless_count/len(population)


def do_simulation_baseline(gens: int, size: int, predator_rate: float, reprod_rate: float):

    population = init_population(size)
    sizes = []
    for gen in range(gens):
        
        population, cur_size = do_generation(population, predator_rate, reprod_rate)
        sizes.append(cur_size)
    
    return sizes


def do_simulation_selfish_selfless(gens: int, size: int, predator_rate: float, reprod_rate: float):

    population = []
    for i in range(size):
        if i % 2 == 0:
            population.append(Individual('selfish'))
        else:
            population.append(Individual('selfless'))

    selfish, selfless = [], []
    for _ in range(gens):
        
        population, selfish_cur, selfless_cur = do_generation_selfish_selfless(population, predator_rate, reprod_rate)
        selfish.append(selfish_cur)
        selfless.append(selfless_cur)

    
    return selfish, selfless

if __name__ == "__main__":


    # parameters
    N_GENS = 50
    POP_SIZE = 100
    PRED_RATE = 0.5
    REPROD_RATE = 0.7

    metrics = do_simulation_baseline(
        N_GENS,
        POP_SIZE,
        PRED_RATE, 
        REPROD_RATE
    )
    plt.style.use('seaborn-darkgrid')
    plt.plot(range(N_GENS), metrics, label="Population", color="green")
    plt.fill_between(range(N_GENS), 0, metrics, color="green")
    plt.legend()
    plt.title('Population Growth Baseline')
    plt.ylabel('Population')
    plt.xlabel('Generation')
    plt.savefig('baseline.png')
    plt.clf()

    N_GENS = 50

    pop1, pop2 = do_simulation_selfish_selfless(
        N_GENS,
        POP_SIZE,
        PRED_RATE,
        0.6
    )

    plt.plot(range(N_GENS), pop1, label="Selfish Proportion", color="red")
    plt.plot(range(N_GENS), pop2, label="Selfless Proportion", color="green")
    plt.fill_between(range(N_GENS), pop1, pop2, color="red")
    plt.fill_between(range(N_GENS), pop2, 0, color="green")
    plt.ylim(0, 1.2)
    plt.legend(facecolor='white', framealpha=1)
    plt.title('Population Growth')
    plt.ylabel('Population')
    plt.xlabel('Generation')
    plt.savefig('selfish_selfless.png')