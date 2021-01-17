import math

def getFinalScore(raw_emotions, pronounciation, raw_category, raw_pauses, raw_fillers, raw_wpm, conciseness, readability):
    weights = {
        "emotions": 0.1,
        "pronounciation": 0.15,
        "category": 0.2,
        "pauses": 0.05,
        "fillers":0.05,
        "wpm":0.15,
        "conciseness":0.15,
        "readability":0.15
    }
    raw_category_total = 0
    for key in raw_category:
        if key in ["Funny","Beautiful","Ingenious","Courageous", "Informative", "Inspiring", "Fascinating","Persuasive", "Jaw-dropping"]:
            raw_category_total += raw_category[key]
        else:
            raw_category_total -= raw_category[key]
    category = raw_category_total * 0.5
    emotions = len(raw_emotions) * 0.25
    pauses = (pow(math.e, (-4 * raw_pauses)) * -1) + 1
    fillers = pow(math.e, (-0.33 * raw_fillers))
    wpm = (-0.002 * pow((raw_wpm-140),2))+1
    score = 0
    score = (emotions * weights["emotions"])+(weights["pronounciation"] * pronounciation)+(weights["category"]*category)+(weights["pauses"]*pauses)+(weights["fillers"]*fillers)+(weights["wpm"]*wpm)+(weights["conciseness"]* conciseness)+(weights["readability"]*readability)
    return score