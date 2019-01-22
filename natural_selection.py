from environment import Sprite
from random import randrange

MUTATION_SIZE = 4
MUTATION_RATE = .01

def selection(population):
    for sprite in population:
        rand = randrange(0,1,.1)
        if rand >= sprite.fitness:
            population.remove(sprite)

    return population

def crossover(population):
    new_population = []

    for sprite in population:
        sprite_mate = choose_mate(sprite, population)

        population.remove(sprite)

        if sprite_mate != sprite:
            population.remove(sprite_mate)
            rand = randrange(0, 100, 1)
            for i in range(50):
                index = rand % 100
                temp = sprite[index]
                sprite[index] = sprite_mate[index]
                sprite_mate[index] = temp

            new_population.add(sprite)
            new_population.add(sprite)



    return population


'''
3 ways to go about mate pairing
    1) Like attracts like, in respect to fitness score

    2) Sprite will always attempt to match with highest ranking sprite.
       Probability of that sprite's success is dependent on how similar their
       fitnesses are

    3) Sprite has sense of "league" and will only attempt to mate with sprite
       within their league. Represent by regression number proportional to
       fitness. The lower the fitness, the smalled the league threshold. The
       larger the fitness, the larger the league threshold. 


Notes
    - Mating not dependent on probability of mating, dependent on 
      where the sprite starts the search for a mate. This is because sprites
      lower in the list of pairing have lower chance of being picked because
      more chances for sprite to pick someone before they reach them.

    - Probability of mating, for all scenarios, is the same. Dependent on how
      similar the sprite's fitnesses are. Probability of Mating = 
      (.98 - absolute value of the difference of the two sprite's fitnesses).

    - With current algorithms, it is possible that the sprite will not find a
      mate. This should remain true throughout any iteration of this. Represents
      a sprite's failure to breed, not because of death (which is handled in
      selection), but because of inability to find a partner.

'''

def choose_mate(sprite, population):
    def sort_by_fit():
        for fillslot in range(len(population) - 1, 0, -1):
            positionOfMax = 0
            for location in range(1, fillslot + 1):
                if population[location] > population[positionOfMax]:
                    positionOfMax = location

            temp = population[fillslot]
            population[fillslot] = population[positionOfMax]
            population[positionOfMax] = temp
        return population

    sort_by_fit()

    for s in population:
        if randrange(0,1,.01) <= (.98 - abs(sprite.fitness - s.fitness)):
            return s


    return sprite

def mutation(population):
    for sprite in population:
        rand = randrange(0,1,.01)
        if rand <= MUTATION_RATE:
            mutate(sprite)


def mutate(sprite):
    rand_location = randrange(0,sprite.chromosome.count, 1)
    rand_num = randrange(0,3,1)

    sprite.chromosome[rand_location] = rand_num
    sprite.chromosome[(rand_location + 1) % sprite.chromosome.count] = rand_num + 1 % 3
    sprite.chromosome[(rand_location + 2) % sprite.chromosome.count] = rand_num + 2 % 3

    return sprite

def generate_gen(population):
    return mutation(crossover(selection(population)))

