import sys
import random


def get_random_words(n):
    words = open('/usr/share/dict/words', 'r').read().split('\n')
    random_words = []
    for _ in range(n):
        random_words.append(random.choice(words))
    return random_words


if __name__ == '__main__':
    num_rand_words = int(sys.argv[1])
    words = get_random_words(num_rand_words)
    print(words)
