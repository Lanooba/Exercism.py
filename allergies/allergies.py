class Allergies(object):
    def __init__(self, score):
        pass

    def is_allergic_to(self, item):
        pass

    @property
    def lst(self):
        pass

#Creating a function containing the entire calculation to call later      
def allergic(score):
    inputScore = score

    is_allergic_to = {1:'eggs', 2:'peanuts', 4:'shellfish', 
        8:'strawberries', 16:'tomatoes', 32:'chocolate',
        64:'pollen', 128:'cats'}
    
    # first, decompose the score into binary and store it in an array
    # the [2:] is how to remove the first 2 elements, which are the bin indicators, in the array
    scoreDecomp = bin(inputScore)
    scoreArray = list(scoreDecomp)[2:]
    # print(scoreArray)

    # next, we need to generate an array of indeces for ScoreArray
    # then, we reverse ScoreArray and apply the indeces to the power of 2
    for idx, val in enumerate(reversed (scoreArray)):
        if val == '1':
            newIndex = 2 ** idx
            print(is_allergic_to[newIndex])   
    

# let's call this function and see how it goes
allergic(17)
