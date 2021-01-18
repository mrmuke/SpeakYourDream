import math
import numpy as np
def getFinalScore(raw_emotions, pronounciation, raw_category, raw_pauses, raw_fillers, raw_wpm, readability):
    weights = {
        "emotions": 0.1,
        "pronounciation": 0.15,
        "category": 0.2,
        "pauses": 0.1,
        "fillers":0.05,
        "wpm":0.15,
        "readability":0.25
    }
    raw_category_total = 0
    for key in raw_category:
        if key in ["Funny","Beautiful","Ingenious","Courageous", "Informative", "Inspiring", "Fascinating","Persuasive", "Jaw-dropping"]:
            raw_category_total += raw_category[key]
        else:
            raw_category_total -= raw_category[key]

    category = raw_category_total
    print(category)
    emotions = len(np.unique(raw_emotions)) 
    if(emotions>1):
        emotions=1.0
    else:
        emotions=0.75
    print(emotions)

    pauses = (pow(math.e, (-4 * raw_pauses)) * -1) + 1
    print(pauses)
    fillers = pow(math.e, (-0.05 * raw_fillers))
    print(fillers)
    
    wpm = (-0.0005 * pow((raw_wpm-150),2))+1
    print(wpm)
    score = (emotions * weights["emotions"])+(weights["pronounciation"] * pronounciation)+(weights["category"]*category)+(weights["pauses"]*pauses)+(weights["fillers"]*fillers)+(weights["wpm"]*wpm)+(weights["readability"]*readability)
    return score