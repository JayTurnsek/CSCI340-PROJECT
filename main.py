"""
Author: Jay Turnsek, Liam Johnston
Title: main.py

Main driver script for a-life simulation.
"""

import random
import matplotlib.pyplot as plt
from matplotlib import animation


class Individual:
    '''
    Representation/encoding of each of our subjects. Behavior determines how it handles predator interactions.
    Food state will determine if it is eligible to reproduce or not.
    '''
    def __init__(self, behavior):
        self.behavior = behavior
        self.foodState = False
    

    def __repr__(self):
        return f'Individual with {self.behavior} behavior'


    def hasFood(self) -> bool:
        return self.foodState


    def setFoodState(self, state: bool):
        self.foodState = state


# PREDATOR HANDING
def handle_predator(ind1, ind2):
    """
    Handles behavior of predator interactions between two individuals;
    Highly based on behavioral dynamics. 

    *** DEATH IS TREATED AS NOT GETTING FOOD; THUS NOT REPRODUCING. ***

    @ind1: first individual
    @ind2: Second individual
    """

    if ind1.behavior == "base" and ind2.behavior == "base":
        # 50/50 chance for baseline.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        else:
            ind2.setFoodState(True)

    elif ind1.behavior == "cowardice" and ind2.behavior == "cowardice":
        # Selfish/cowardice behaviors result in a 75% chance of running away unscathed.
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)

    elif ind1.behavior == "altruist" and ind2.behavior == "altruist":
        # One altruist individual will alert, the other gets away guarenteed.
        # The one who alerts has a 50% chance of getting killed.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        ind2.setFoodState(True)

    elif ind1.behavior == "cowardice" and ind2.behavior == "altruist":
        # The altruist individual alerts letting the cowardice get away free,
        # But altruist now has 50% chance of death.
        ind1.setFoodState(True)
        if random.random() < 0.5:
            ind2.setFoodState(True)

    elif ind1.behavior == "altruist" and ind2.behavior == "cowardice":
        # The altruist individual alerts letting the cowardice get away free,
        # But altruist now has 50% chance of death.
        ind2.setFoodState(True)
        if random.random() < 0.5:
            ind1.setFoodState(True)

    elif ind1.behavior == "gb_altruist" and ind2.behavior == "gb_altruist":
        # The green beard altruist individual alerts letting the other get away free,
        # But individual who alerted now has 50% chance of death.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        ind2.setFoodState(True)

    elif ind1.behavior == "gb_altruist" and ind2.behavior == "cowardice":
        # Since cowardice not same type as green beard altruist, no alert given;
        # Both have 25% chance of death
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)

    elif ind1.behavior == "cowardice" and ind2.behavior == "gb_altruist":
        # Since cowardice not same type as green beard altruist, no alert given;
        # Both have 25% chance of death
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)

    elif ind1.behavior == "spite" and ind2.behavior == "cowardice":
        # Spite alerts predator of cowardice's presence, raises cowardice's chance of death to 0.5.
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.5:
            ind2.setFoodState(True)

    elif ind1.behavior == "cowardice" and ind2.behavior == "spite":
        # Spite alerts predator of cowardice's presence, raises cowardice's chance of death to 0.5.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)

    elif ind1.behavior == "spite" and ind2.behavior == "spite":
        # Since both here are spiteful, both of their chances of death go up.
        if random.random() < 0.25:
            ind1.setFoodState(True)
        if random.random() < 0.25:
            ind2.setFoodState(True)

    elif ind1.behavior == "selective_spite" and ind2.behavior == "cowardice":
        # Selective spite alerts predator of cowardice's presence, raises cowardice's chance of death to 0.5.
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.5:
            ind2.setFoodState(True)

    elif ind1.behavior == "cowardice" and ind2.behavior == "selective_spite":
        # Selective spite alerts predator of cowardice's presence, raises cowardice's chance of death to 0.5.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)

    elif ind1.behavior == "selective_spite" and ind2.behavior == "selective_spite":
        # Since selective spite only alerts predator of other species' presence, both just run away.
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)

    elif ind1.behavior == "altruist" and ind2.behavior == "selective_spite":
        # Altruist alerts selective spite to predator, and selective spite alerts predator of 
        # altruist's presence. 0.75 death rate for altruist, selective spite gets away free.
        if random.random() > 0.75:
            ind1.setFoodState(True)
        ind2.setFoodState(True)

    elif ind1.behavior == "selective_spite" and ind2.behavior == "altruist":
        # Altruist alerts selective spite to predator, and selective spite alerts predator of 
        # altruist's presence. 0.75 death rate for altruist, selective spite gets away free.
        if random.random() > 0.75:
            ind2.setFoodState(True)
        ind1.setFoodState(True)

    elif ind1.behavior == "altruist" and ind2.behavior == "spite":
        # Altruist alerts spite to predator, and selective spite alerts predator of 
        # altruist's presence. 0.75 death rate for altruist, spite gets away free.
        if random.random() > 0.75:
            ind1.setFoodState(True)
        ind2.setFoodState(True)

    elif ind1.behavior == "spite" and ind2.behavior == "altruist":
        # Altruist alerts spite to predator, and selective spite alerts predator of 
        # altruist's presence. 0.75 death rate for altruist, spite gets away free.
        if random.random() > 0.75:
            ind2.setFoodState(True)
        ind1.setFoodState(True)
    
    elif ind1.behavior == "selective_spite" and ind2.behavior == "gb_altruist":
        # No alert given by green beard, and selective spite alerts predator of green
        # beard's presence. 0.5 death rate for green beard, selective spite 0.25.
        if random.random() < 0.5:
            ind2.setFoodState(True)
        if random.random() < 0.75:
            ind1.setFoodState(True)
    
    elif ind1.behavior == "gb_altruist" and ind2.behavior == "selective_spite":
        # No alert given by green beard, and selective spite alerts predator of green
        # beard's presence. 0.5 death rate for green beard, selective spite 0.25.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        if random.random() < 0.75:
            ind2.setFoodState(True)
    
    elif ind1.behavior == "selective_spite" and ind2.behavior == "spite":
        # Spite exchanged both ways. Predator is notified of both, one dies one doesn't.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        else:
            ind2.setFoodState(True)

    elif ind1.behavior == "spite" and ind2.behavior == "selective_spite":
        # Spite exchanged both ways. Predator is notified of both, one dies one doesn't.
        if random.random() < 0.5:
            ind1.setFoodState(True)
        else:
            ind2.setFoodState(True)

    elif ind1.behavior == "spite" and ind2.behavior == "gb_altruist":
        # No alert given by green beard, spite alerts predator of green beard's presence.
        # 0.25 death rate for spite, 0.5 for green beard.
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.5:
            ind2.setFoodState(True)

    elif ind1.behavior == "gb_altruist" and ind2.behavior == "spite":
        # No alert given by green beard, spite alerts predator of green beard's presence.
        # 0.25 death rate for spite, 0.5 for green beard.
        if random.random() < 0.75:
            ind2.setFoodState(True)
        if random.random() < 0.5:
            ind1.setFoodState(True)

    elif ind1.behavior == "gb_altruist" and ind2.behavior == "altruist":
        # Altruist gives alert, green beard does not. 0.25 death rate for green beard, 0.5 death
        # rate for altruist.
        if random.random() < 0.75:
            ind1.setFoodState(True)
        if random.random() < 0.5:
            ind2.setFoodState(True)

    elif ind1.behavior == "altruist" and ind2.behavior == "gb_altruist":
        # Altruist gives alert, green beard does not. 0.25 death rate for green beard, 0.5 death
        # rate for altruist.
        if random.random() < 0.75:
            ind2.setFoodState(True)
        if random.random() < 0.5:
            ind1.setFoodState(True)
        
    else:
        print(f"1: {ind1.behavior}, 2: {ind2.behavior}")
        exit()


# GENERATION FUNCTIONS
def do_generation_baseline(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food
    for i, j in zip(shuffled[0::2], shuffled[1::2]):

        # Determine if predator present
        if random.random() <= predator_rate:

            handle_predator(i, j)

        # Otherwise, both get food and stay alive
        else:
            i.setFoodState(True)
            j.setFoodState(True)

    # Reproduction process.
    food_count = 0
    for i in shuffled:
        if i.hasFood():
            food_count += 1
            if random.random() < reprod_rate:
                # reproduce, osmosis style. only if food was grabbed.
                child1 = Individual("base")
                child2 = Individual("base")
                next_gen.append(child1)
                next_gen.append(child2)

    return next_gen, len(next_gen)


def do_generation_cowardice_altruist(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):

        # Determine if predator present
        if random.random() <= predator_rate:

            handle_predator(i, j)

        # Otherwise both get food and live
        else:
            i.setFoodState(True)
            j.setFoodState(True)

    # Do reproduction for population
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

    # Metrics for proportion plot
    cowardice_count, altruist_count = 0, 0
    for individual in population:
        if individual.behavior == "cowardice":
            cowardice_count += 1
        if individual.behavior == "altruist":
            altruist_count += 1

    return next_gen, cowardice_count / len(population), altruist_count / len(population)


def do_generation_gb_cowardice(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):

        # Determine if there is a predator
        if random.random() <= predator_rate:

            handle_predator(i, j)

        # Otherwise, both get food and to live
        else:
            i.setFoodState(True)
            j.setFoodState(True)

    # Do reproduction
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

    # Metrics for plot
    cowardice_count, altruist_count = 0, 0
    for individual in population:
        if individual.behavior == "cowardice":
            cowardice_count += 1
        if individual.behavior == "gb_altruist":
            altruist_count += 1

    return next_gen, cowardice_count / len(next_gen), altruist_count / len(next_gen)


def do_generation_spite_cowardice(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):

        # Determine if there is a predator
        if random.random() <= predator_rate:

            handle_predator(i, j)

        # Otherwise, both get food and to live
        else:
            i.setFoodState(True)
            j.setFoodState(True)

    # Do reproduction
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

    # Metrics for plot
    cowardice_count, spite_count = 0, 0
    for individual in population:
        if individual.behavior == "cowardice":
            cowardice_count += 1
        if individual.behavior == "spite":
            spite_count += 1

    return next_gen, cowardice_count / len(population), spite_count / len(population)


def do_generation_selectivespite_cowardice(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):

        # Determine if there is a predator
        if random.random() <= predator_rate:

            handle_predator(i, j)

        # Otherwise, both get food and to live
        else:
            i.setFoodState(True)
            j.setFoodState(True)

    # Do reproduction
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

    # Metrics for plot
    cowardice_count, selectivespite_count = 0, 0
    for individual in population:
        if individual.behavior == "cowardice":
            cowardice_count += 1
        if individual.behavior == "selective_spite":
            selectivespite_count += 1

    return (
        next_gen,
        cowardice_count / len(population),
        selectivespite_count / len(population),
    )


def do_generation_full(population: list[Individual], predator_rate: float, reprod_rate: float):
    # get randomized population
    shuffled = random.sample(population, len(population))

    # init next gen population
    next_gen = []

    # Process every 2 pair of individuals; since each tree has two food (situation handling)
    for i, j in zip(shuffled[0::2], shuffled[1::2]):

        # Determine if there is a predator
        if random.random() <= predator_rate:

            handle_predator(i, j)

        # Otherwise, both get food and to live
        else:
            i.setFoodState(True)
            j.setFoodState(True)

    # Do reproduction
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

    # Metrics for plot
    cowardice_count = 0
    altruist_count = 0
    gbaltruist_count = 0
    spite_count = 0
    selspite_count = 0

    for individual in population:
        if individual.behavior == "cowardice":
            cowardice_count += 1
        if individual.behavior == "altruist":
            altruist_count += 1
        if individual.behavior == "gb_altruist":
            gbaltruist_count += 1
        if individual.behavior == "spite":
            spite_count += 1
        if individual.behavior == "selective_spite":
            selspite_count += 1

    gen_metrics = {
        'cowardice': cowardice_count / len(population),
        'altruist': altruist_count / len(population),
        'gb_altruist': gbaltruist_count / len(population),
        'spite': spite_count / len(population),
        'selective_spite': selspite_count / len(population),
        

    }
    return (
        next_gen,
        gen_metrics
    )

# SIMULATION FUNCTIONS
def do_simulation_baseline(gens: int, size: int, predator_rate: float, reprod_rate: float):

    # Initialize population
    population = [Individual("base") for _ in range(size)]

    sizes = []
    for _ in range(gens):

        # Do generation, save population growth
        population, cur_size = do_generation_baseline(
            population, predator_rate, reprod_rate
        )
        sizes.append(cur_size)

    return sizes


def do_simulation_cowardice_altruist(gens: int, size: int, predator_rate: float, reprod_rate: float):

    # Init population, 50/50 split of cowardice and altruist
    population = []
    for i in range(size):
        if i % 2 == 0:
            population.append(Individual("cowardice"))
        else:
            population.append(Individual("altruist"))

    cowardice, altruist = [], []
    for _ in range(gens):

        # Do generation, save proportions for plotting later
        population, cowardice_cur, altruist_cur = do_generation_cowardice_altruist(
            population, predator_rate, reprod_rate
        )
        cowardice.append(cowardice_cur)
        altruist.append(altruist_cur)

    return cowardice, altruist


def do_simulation_gb_cowardice(gens: int, size: int, predator_rate: float, reprod_rate: float):

    # Init population, 50/50 split of cowardice and green beard altruist
    population = []
    for i in range(size):
        if i % 2 == 0:
            population.append(Individual("cowardice"))
        else:
            population.append(Individual("gb_altruist"))

    cowardice, altruist = [], []
    for _ in range(gens):

        # Do generation, save proportions for plotting later
        population, cowardice_cur, altruist_cur = do_generation_gb_cowardice(
            population, predator_rate, reprod_rate
        )
        cowardice.append(cowardice_cur)
        altruist.append(altruist_cur)

    return cowardice, altruist


def do_simulation_spite_cowardice(gens: int, size: int, predator_rate: float, reprod_rate: float):

    # Init population, 50/50 split of cowardice and green beard altruist
    population = []
    for i in range(size):
        if i % 2 == 0:
            population.append(Individual("cowardice"))
        else:
            population.append(Individual("spite"))

    cowardice, spite = [], []
    for _ in range(gens):
        # Do generation, save proportions for plotting later
        population, cowardice_cur, spite_cur = do_generation_spite_cowardice(
            population, predator_rate, reprod_rate
        )
        cowardice.append(cowardice_cur)
        spite.append(spite_cur)

    return cowardice, spite


def do_simulation_selectivespite_cowardice(gens: int, size: int, predator_rate: float, reprod_rate: float):

    # Init population, 50/50 split of cowardice and green beard altruist
    population = []
    for i in range(size):
        if i % 2 == 0:
            population.append(Individual("cowardice"))
        else:
            population.append(Individual("selective_spite"))

    cowardice, selectivespite = [], []
    for _ in range(gens):
        # Do generation, save proportions for plotting later
        (
            population,
            cowardice_cur,
            selectivespite_cur,
        ) = do_generation_selectivespite_cowardice(
            population, predator_rate, reprod_rate
        )
        cowardice.append(cowardice_cur)
        selectivespite.append(selectivespite_cur)

    return cowardice, selectivespite


def do_simulation_full(gens: int, size: int, predator_rate: float, reprod_rate: float):

    # Init population, with even split of all behavior types.
    behaviors  = ['cowardice', 'altruist', 'gb_altruist', 'spite', 'selective_spite']
    metrics = {b: [] for b in behaviors}
    population = []

    for i in range(size):
        population.append(Individual(behaviors[i % len(behaviors)]))


    for _ in range(gens):
        # Do generation, save proportions for plotting later
        population, cur_metrics = do_generation_full(
            population, predator_rate, reprod_rate
        )

        # Add to metrics dict
        for b in behaviors:
            metrics[b].append(cur_metrics[b])

    return metrics


# RUNNABLE FUNCTIONS
def baseline():
    # Baseline
    metrics = do_simulation_baseline(N_GENS, POP_SIZE, PRED_RATE, REPROD_RATE)

    # Plot results
    plt.style.use("seaborn-darkgrid")
    plt.plot(range(N_GENS), metrics, label="Population", color="blue")
    plt.fill_between(range(N_GENS), 0, metrics, color="blue")
    plt.legend()
    plt.title("Population Growth Baseline")
    plt.ylabel("Population")
    plt.xlabel("Generation")
    plt.savefig("baseline.png")
    plt.clf()


def altruist_cowardice():
    # Cowardice vs. Altruist
    pop1, pop2 = do_simulation_cowardice_altruist(N_GENS, POP_SIZE, PRED_RATE, 0.6)

    # Plot results
    plt.plot(range(N_GENS), TOP_PROP, label="Cowardice Proportion", color="red")
    plt.plot(range(N_GENS), pop2, label="Altruist Proportion", color="yellow")
    plt.fill_between(range(N_GENS), TOP_PROP, pop2, color="red")
    plt.fill_between(range(N_GENS), pop2, 0, color="yellow")
    plt.ylim(0, 1.2)
    plt.legend(facecolor="white", framealpha=1)
    plt.title("Population Distribution")
    plt.ylabel("Proportion")
    plt.xlabel("Generation")
    plt.savefig("cowardice_altruist.png")
    plt.clf()


def greenbeard_cowardice():
    # Green Beard Altruist vs Cowardice
    pop1, pop2 = do_simulation_gb_cowardice(N_GENS, POP_SIZE, PRED_RATE, 0.6)

    # Plot results
    plt.plot(range(N_GENS), TOP_PROP, label="Cowardice", color="red")
    plt.plot(range(N_GENS), pop2, label="Green Beard Altruist", color="green")
    plt.fill_between(range(N_GENS), TOP_PROP, pop2, color="red")
    plt.fill_between(range(N_GENS), pop2, 0, color="green")
    plt.ylim(0, 1.2)
    plt.legend(facecolor="white", framealpha=1)
    plt.title("Population Distribution")
    plt.ylabel("Proportion")
    plt.xlabel("Generation")
    plt.savefig("cowardice_gbaltruist.png")
    plt.clf()


def spite_cowardice():
    # Spite vs Cowardice
    pop1, pop2 = do_simulation_spite_cowardice(N_GENS, POP_SIZE, PRED_RATE, REPROD_RATE)
    # Plot results
    plt.plot(range(N_GENS), TOP_PROP, label="Cowardice", color="red")
    plt.plot(range(N_GENS), pop2, label="Spite", color="purple")
    plt.fill_between(range(N_GENS), TOP_PROP, pop2, color="red")
    plt.fill_between(range(N_GENS), pop2, 0, color="purple")
    plt.ylim(0, 1.2)
    plt.legend(facecolor="white", framealpha=1)
    plt.title("Population Distribution")
    plt.ylabel("Proportion")
    plt.xlabel("Generation")
    plt.savefig("spite_cowardice.png")
    plt.clf()


def selectivespite_cowardice():
    # Selective Spite vs Cowardice
    pop1, pop2 = do_simulation_selectivespite_cowardice(
        N_GENS, POP_SIZE, PRED_RATE, 0.6
    )
    # Plot results
    # plt.plot(range(N_GENS), TOP_PROP, label="Cowardice", color="red")
    plt.plot(range(N_GENS), pop1, color="magenta")
    plt.fill_between(range(N_GENS), TOP_PROP, pop2, color="red", label="Cowardice")
    plt.fill_between(range(N_GENS), pop2, 0, color="magenta", label="Selective Spite")
    plt.ylim(0, 1.2)
    plt.legend(facecolor="white", framealpha=1)
    plt.title("Population Distribution")
    plt.ylabel("Proportion")
    plt.xlabel("Generation")
    plt.savefig("selectivespite_cowardice.png")


def full_sim():
    # Run full simulation with all species involved.
    metrics = do_simulation_full(
        N_GENS, POP_SIZE, PRED_RATE, REPROD_RATE
    )
    
    # Plot results
    behaviors  = ['cowardice', 'altruist', 'gb_altruist', 'spite', 'selective_spite']
    behavior_titles = ['Cowardice', 'Altruist', 'Green Beard Altruist', 'Spite', 'Selective Spite']
    colors = ['red', 'yellow', 'green', 'purple', 'magenta']
    plt.style.use('seaborn-darkgrid')
    for behavior, color, behavior_title in zip(behaviors, colors, behavior_titles):
        plt.plot(range(N_GENS), metrics[behavior], color=color, label=behavior_title)
    plt.legend(facecolor="white", framealpha=1)
    plt.title(f"Population Distribution, Predator rate: {PRED_RATE}")
    plt.ylabel("Proportion")
    plt.xlabel("Generation")
    plt.savefig('full_simulation.png')
    plt.clf()

    
    
    # Do animation
    fig = plt.figure()
    plt.ylim(0, 1)
    plt.title('Population Distribution')

    # Init data for the bar graphs
    y = [
        metrics['cowardice'], 
        metrics['altruist'], 
        metrics['gb_altruist'],
        metrics['spite'], 
        metrics['selective_spite']
    ]
    bars = plt.bar(behavior_titles, [vals[0] for vals in y], color=colors)

    # Generation counter display
    gens = range(N_GENS)
    gen = plt.text(0, 0.8, 'Generation: 0', size=20, bbox=dict(facecolor='grey', edgecolor='black', alpha=0.2))

    # Frame update procedure
    def animate(i):
        new_vals = [vals[i] for vals in y]

        for bar, new_val in zip(bars, new_vals):
            bar.set_height(new_val)
        
        gen.set_text(f'Generation: {gens[i]}, Predator Rate: {PRED_RATE}')

    # Do and save animation
    ani = animation.FuncAnimation(fig, animate, interval=400) 
    ani.save('fullsim.gif', writer='imagemagick')


if __name__ == "__main__":

    # PARAMETERS
    N_GENS = 50
    POP_SIZE = 50
    PRED_RATE = 0.7
    REPROD_RATE = 0.7
    TOP_PROP = [1] * len(range(N_GENS))

    # baseline()                      # Baseline run of concept.
    # altruist_cowardice()            # Test altruism vs cowardism
    # greenbeard_cowardice()          # Test green beard altruism vs. cowardism
    # spite_cowardice()               # Test spitefulness vs cowardism
    # selectivespite_cowardice()      # Test selective spitefulness vs cowardism
    full_sim()                      # Simulate environment with all types
