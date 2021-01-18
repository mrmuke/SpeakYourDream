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
    sents = list(filter(lambda x : len(x) >0, sents))
    word_count = len(string.split(" "))
    
    if len(sents)>0:
        return float(word_count)/len(sents)
    else:
        return 0


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


def flesch(string):
    B = words_per_sentence(string)*1.015
    A = syllables_per_word(string)*84.6
    return 206.835-B-A

