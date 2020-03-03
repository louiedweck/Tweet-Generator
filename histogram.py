def get_all_words(location):
    '''opens text file and converts into array of strings '''
    f = open(location, "r")
    lines = f.readlines()
    f.close()
    # print(all_words)
    words = []
    for line in lines:
        for word in line.split():
            words.append(word)
    return words


def hist(text):
    ''' Iterate over words and adds them to dictionary that totals amount of occurences (for each word)'''
    histogram = dict()
    for word in text:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1
    return histogram


def get_num_tokens(self):
    '''gets the number of tokens in the listogram'''

    tokens = 0
    for item in self.list_histogram:
        tokens += item[1]
    return tokens


def repeated_words(histogram):
    '''Creates list of repeated words'''
    list_multiples = []
    for word, count in histogram.items():
        if count > 1:
            list_multiples.append(word)
    return list_multiples


def unique_words(histogram):
    ''' Returns amount of words occuring in text at least once '''
    return len(histogram)


def frequency(word, histogram):
    '''Returns count of single word usage throughout text '''
    return histogram[word]


def get_index(word, histogram):
    '''Checks indices to see where word is. Helper function for histograms using lists of lists and tuples.  '''
    current_index = 0
    for item in histogram:
        if item[0] == word:
            return current_index
        current_index += 1
    return -1


def listogram(text):
    '''Histogram using lists of lists. You should be able to grab a coffee in the time this program takes to run on a text with over 20,000 words. '''
    listogram = []
    lines = open(text, "r").readlines()
    for line in lines:
        for word in line.split():
            index = get_index(word, listogram)
            if index == -1:
                listogram.append([word, 1])
            else:
                listogram[index][1] += 1
    return listogram


def tuplegram(text):
    '''Takes in strings (single) words and provides a histogram using Tuples. '''
    tuplegram = []
    for word in text:
        index = get_index(word, tuplegram)
        if index == -1:
            tuplegram.append((word, 1))
        else:
            update_count = tuplegram[index][1] + 1
            tuplegram[index] = (word, update_count)
    return tuplegram


if __name__ == '__main__':
    words = get_all_words('book.txt')
    print(hist(words))
    # print(repeated_words(histogram))
    # print(unique_words(histogram))
    # print(frequency("liberty", histogram))
    # print(listogram('book.txt'))
    # print(tuplegram(words))
