import re


def count_syllables(word):
    return len(
        re.findall('(?!e$)[aeiouy]+', word, re.I) +
        re.findall('^[^aeiouy]*e$', word, re.I)
    )


def syllables_per_word(string):
    arr = string.lower().split(" ")
    count = 0
    for item in arr:
        count += count_syllables(item)
    return float(count)/len(arr)


def words_per_sentence(string):
    sents = re.split(r'[.?!]\s*', string)
    sents = sents[:len(sents)-1]
    word_count = 0
    for i in string:
        word_count += len(i.split(" "))
    return float(word_count)/len(sents)


def fog(string):
    syllablecount = 0
    beg_each_Sentence = re.findall(r"\.\s*(\w+)", string)
    capital_words = re.findall(r"\b[A-Z][a-z]+\b", string)
    words = string.split()
    for word in words:
        # all lower case words
        if word not in capital_words and len(word) >= 3:
            if count_syllables(word) >= 3:
                syllablecount += 1

        if word in capital_words and word in beg_each_Sentence:  # beginning of each sentence is uppercase

            if count_syllables(word) >= 3:
                syllablecount += 1
    sents = re.split(r'[.?!]\s*', string)
    avg_len = sum(len(x.split()) for x in sents) / len(sents)
    return (syllablecount + avg_len) * 0.4


string = open('speech.txt', 'r').read()


def fleshers(string):
    B = words_per_sentence(string)*1.015
    A = syllables_per_word(string)*84.6
    C = B-A
    return 206.835-C


print(fleshers(string))
print(fog(string))
