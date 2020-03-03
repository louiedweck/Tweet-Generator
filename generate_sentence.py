from histogram import hist
from histogram import get_all_words
from random import randint


def sample(histogram):
    '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''

    # TODO: use your sample function as a starting point to complete this method
    pointer = randint(1, sum(histogram.values()))
    count = 0
    for key, value in histogram.items():
        count += value
        if count >= pointer:
            return key


def generate_sentence():
    my_file = get_all_words("book.txt")
    my_histogram = hist(my_file)

    sentence = ""
    num_words = 10
    for _ in range(num_words):
        word = sample(my_histogram)
        sentence += " " + word
    return sentence


if __name__ == '__main__':
    print(generate_sentence())
