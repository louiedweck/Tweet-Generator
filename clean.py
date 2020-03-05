import re


def clean(string: str):
    lowercased = string.lower()
    without_punctuation = re.sub(r'[.,!?]', '', lowercased)
    return without_punctuation

# def tokenize(text):
#     tokens = split_on_whitespace(text)
#     return tokens

# def split_on_whitespace(text):
#     return re.split('\s+', text)


if __name__ == '__main__':
    text = open('book.txt').read()
    cleaned = clean(text)
    print(cleaned[:1000])
