from environment import generate_perfect_chromosome, generate_population, generation
from natural_selection import generate_gen

def next_generation():
    return generate_gen(generation)

def play():
    generate_perfect_chromosome()
    generate_population()

    while current_generation < 10:
        next_generation()
        current_generation = + 1