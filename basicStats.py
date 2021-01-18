import scipy.io.wavfile as wav
from itertools import islice

def getRepitition(string):
    return get_top_3(get_frequency_hash(string))

def get_frequency_hash(text):
    array = text.split(" ")
    frequency = {} 
    for word in array: 
        try: 
           frequency[word] += 1 
        except: 
           frequency[word]= 1
    return frequency

def get_top_3(frequency_hash):
    sorted_array_of_tuples = dict(sorted(frequency_hash.items(), key=lambda item: item[1],reverse=True))
    return take(3, sorted_array_of_tuples.items())

def getWPM(text,path):
    (source_rate, source_total) = wav.read(path)
    totalTime = len(source_total)/float(source_rate)
    wordArr = text.lower().split(' ')
    totalWords = len(wordArr)
    wpm = (totalWords/totalTime) * 60
    return wpm
def take(n, iterable):
    return list(islice(iterable, n))