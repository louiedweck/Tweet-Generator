from random import randint
from histogram import get_all_words
from histogram import hist
from histogram import get_index


class Dictogram:

    def __init__(self, word_list):
        '''Initializes the dictogram properties'''

        # self.word_list = get_all_words('book.txt')

        self.dictionary_histogram = self.build_dictogram(word_list)
        print(word_list, self.dictionary_histogram, sum(
            self.dictionary_histogram.values()))
        self.tokens = self.get_num_tokens()
        self.types = self.unique_words()

    def build_dictogram(self, word_list):
        '''Creates a histogram dictionary using the word_list property and returns it'''
        return hist(word_list)

    def frequency(self, word):
        '''returns the frequency or count of the given word in the dictionary histogram'''
        return self.dictionary_histogram[word]

    def unique_words(self):
        '''returns the number of unique words in the dictionary histogram'''
        return len(self.dictionary_histogram.keys())

    def get_num_tokens(self):
        return sum(self.dictionary_histogram.values())

    def sample(self):
        '''Randomly samples from the dictionary histogram based on the frequency, returns a word'''
        pointer = randint(1, self.get_num_tokens())
        count = 0
        for word, value in self.dictionary_histogram.items():
            count += value
            if count >= pointer:
                return word


def print_dictogram(word_list):
    '''Creates a dictionary based histogram (dictogram) and then prints out its properties and samples from it'''

    print()
    print('Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    dictogram = Dictogram(word_list)
    print('dictogram: {}'.format(dictogram.dictionary_histogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(dictogram)


def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Dictionary Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist.dictionary_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in dictogram.dictionary_histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / dictogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(
            error) < 0.1 else red
        print('| {!r:<9} '.format(word)
              + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
              + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
              + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
