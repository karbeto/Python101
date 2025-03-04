import random


def toss_biased_coin():

    sides = ['heads', 'tails']
    probabilities = [0.7, 0.3]

    print(random.choices(sides, probabilities))


toss_biased_coin()
