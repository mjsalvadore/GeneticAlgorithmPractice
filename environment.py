from random import randint

POPULATION_SIZE = 100
CHROMOSOME_SIZE = 100
current_generation = 0

PERFECT_CHROMOSOME = []
generation = [POPULATION_SIZE]


class Sprite:

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = run_sprite(self)

def generate_perfect_chromosome():
    for x in range(100):
        PERFECT_CHROMOSOME.add(0)

def generate_population():
    for x in range(POPULATION_SIZE):
        generation.add(Sprite(generate_chromosome()))

def generate_chromosome():
    chromosome = []
    for x in range(CHROMOSOME_SIZE):
        rand = randint(0,3)
        chromosome.add(rand)


def run_sprite(sprite):
    if sprite.chromosome == PERFECT_CHROMOSOME:
        return 1
    else:
        return set(sprite.chromosome).intersection(PERFECT_CHROMOSOME).count()/CHROMOSOME_SIZE











