import random

# The coin class simulates a coin tha can
# be flipped.

class Coin:
    # The __init__ method initializes the
    # sideup data attribute with "Heads".
    
    def __init__(self):
        self.__sideup = "Heads"
        
    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sidup is set to "Heads".
    # Otherwise, sideup is set to "Tails".
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    # The get_sideup method returns the value
    # referenced by sideup

    def get_sideup(self):
        return self.__sideup