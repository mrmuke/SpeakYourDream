import re

def count_syllables(word):
    return len(
        re.findall('(?!e$)[aeiouy]+', word, re.I) +
        re.findall('^[^aeiouy]*e$', word, re.I)
    )

def syllables_per_word(string):
    arr=string.lower().split(" ")
    count=0
    for item in arr:
        count+=count_syllables(item)
    return float(count)/len(arr)

def words_per_sentence(string):
    string = re.split(r'[.?!]\s*', string)
    string=string[:len(string)-1]
    word_count=0
    for i in string:
        word_count += len(i.split(" "))
    return float(word_count)/len(string)

string=open('speech.txt', 'r').read()
A=words_per_sentence(string)*0.39
B=syllables_per_word(string)*11.8
C=A+B
print(15.5-C)

