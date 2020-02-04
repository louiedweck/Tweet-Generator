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


def repeated_words(histogram):
    list_multiples = []
    for word, count in histogram.items():
        if count > 1:
            list_multiples.append(word)
    return list_multiples


def unique_words(histogram):
    # unique_words = []
    # for word in histogram.items():
    #     if word not in unique_words:
    #         unique_words.append(word)
    # print(len(unique_words))
    return len(histogram)


def frequency(word, histogram):
    return histogram[word]


if __name__ == '__main__':
    words = get_all_words('book.txt')
    histogram = hist(words)
    print(repeated_words(histogram))
    print(unique_words(histogram))
    print(frequency("liberty", histogram))
