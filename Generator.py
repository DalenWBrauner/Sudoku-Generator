"""
[Name]          Generator.py
[Author]        Dalen W. Brauner
[DLM]           723/2013    2:11 PM
[Purpose]       To create friendly Sudoku objects s.t. Sudoku Puzzles can easily be generated
                and manipulated.
"""
from Puzzle import Sudoku
from random import randint

def main():
    num = "This is a unique sentence the user is unlikely to input."
    while (type(num) != int) or (not (-1 < num < 82)):
        if num != "This is a unique sentence the user is unlikely to input.":
            print "Please only enter integers 0-81."
        num = input("How many boxes would you like omitted?\n40 = Easy, 55 = Normal, 70 = Hard\n")
    return Generate(num)

def Generate(num):
    return Puzzle_Unsolver(Column_Shuffler(Nine_Factorial()),num)

def Nine_Factorial():
    """Creates a random Sudoku Puzzle with up to Nine Factorial (9!) possible combinations."""

    # Sample puzzle from which all puzzles are generated
#    Puzz = [1,4,7,2,5,8,3,6,9,5,2,8,6,3,9,7,4,1,6,9,3,7,1,4,8,2,5,4,7,1,5,8,2,6,9,3,8,5,2,9,\
#            6,3,1,7,4,9,3,6,1,4,7,2,5,8,7,1,4,8,2,5,9,3,6,2,8,5,3,9,6,4,1,7,3,6,9,4,7,1,5,8,2]
    Puzz = [2,4,8,3,9,5,7,1,6,5,7,1,6,2,8,3,4,9,9,3,6,7,4,1,5,8,2,6,8,2,5,3,9,1,7,4,3,5,9,1,\
            7,4,6,2,8,7,1,4,8,6,2,9,5,3,8,6,3,4,1,7,2,9,5,1,9,5,2,8,6,4,3,7,4,2,7,9,5,3,8,6,1]
    Puzzle = Sudoku(Puzz)

    # Randomly generates a list for Mass_Replacement
    lst = [1,2,3,4,5,6,7,8,9]
    rep = []
    for Q in xrange(9):
        rep.append(lst.pop(randint(0,8-Q)))
    
    # MASS REPLACEMENNNNNNNT
    Puzzle.Mass_Replacement(rep)

    # Makes sure the Puzzle generated is valid before shipping it off.
    if Puzzle.isvalid():
        return Puzzle
    else:
        print "Nine_Factorial error! Puzzle not valid after replacement."

def Column_Shuffler(Puzzle):
    """Shuffles the Columns of the Puzzle in such a way that perserves validity yet multiplies
    the number of possible puzzles by a factor of 6**4."""

    # This is called thrice to save lines.
    def Shuffle_Columns(Puzzle,trip):
        """Randomly shuffles any 3 columns."""
        s = randint(0,5)
        if s == 1 or 4:   Puzzle.swapcol(trip[0],trip[1])
        if s == 2 or 5:   Puzzle.swapcol(trip[0],trip[2])
        if s >= 3:        Puzzle.swapcol(trip[1],trip[2])
            
    # See? Called thrice. Saving lines.
    Shuffle_Columns(Puzzle,[0,1,2])
    Shuffle_Columns(Puzzle,[3,4,5])
    Shuffle_Columns(Puzzle,[6,7,8])

    # Shuffles all of the columns in groups of three to perserve validity.
    s = randint(0,5)
    if s == 1 or 4:     #Swaps triplets 1 & 2.
        Puzzle.swapcol(0,3)
        Puzzle.swapcol(1,4)
        Puzzle.swapcol(2,5)
    if s == 2 or 5:     #Swaps triplets 1 & 3.
        Puzzle.swapcol(0,6)
        Puzzle.swapcol(1,7)
        Puzzle.swapcol(2,8)
    if s >= 3:          #Swaps triplets 2 & 3.
        Puzzle.swapcol(3,6)
        Puzzle.swapcol(4,7)
        Puzzle.swapcol(5,8)
    
    # Makes sure the Puzzle generated is valid before shipping it off.
    if Puzzle.isvalid():
        return Puzzle
    else:
        print "Column_Shuffler error! Puzzle not valid after replacement."

def Puzzle_Unsolver(Puzzle,num):
    print "Puzzle_Unsolver"
    return Puzzle

while True:
    aPuzzle = main()
    print aPuzzle
