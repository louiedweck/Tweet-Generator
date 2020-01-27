import sys
import random

arguements = sys.argv[1:]


def rearrange():
    for random_arguement in arguements:
        random_arguement = random.randint(0, len(arguements) - 1)
        print(arguements[random_arguement])


rearrange()
