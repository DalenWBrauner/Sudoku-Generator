"""
[Name]          Answer_Generator.py
[Author]        Dalen W. Brauner
[DLM]           8/1/2013    4:00 PM
[Purpose]       To randomly generate answer sheets for Sudoku Puzzles when
                prompted with Generate().
"""
from Puzzle import Sudoku
from random import randint

def Generate():
    """Call this, an a randomly generated Answer Sheet shall be returned."""
    return Column_Shuffler(Nine_Factorial())

def Nine_Factorial():
    """Creates a random Sudoku Puzzle with up to Nine Factorial (9!) possible combinations."""

    # Seed puzzle from which all puzzles are generated
    Seed = [9,8,6,7,3,1,4,5,2,2,7,3,5,4,8,9,1,6,5,1,4,9,2,6,3,7,8,4,6,5,2,8,7,1,3,9,1,2,8,3,\
            5,9,6,4,7,7,3,9,6,1,4,2,8,5,6,4,2,8,7,3,5,9,1,8,9,1,4,6,5,7,2,3,3,5,7,1,9,2,8,6,4]
    Puzzle = Sudoku(Seed)

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
