"""
[Name]              Answer_Unsolver.py
[Author]            Dalen W. Brauner
[DLM]               8/1/2013   4:00 PM
[Purpose]           To remove a selected number of boxes from a Sudoku
                    puzzle.
"""
from Puzzle import Sudoku
import Answer_Generator
from random import randint

def main():
    """Asks the user for the number of numbers they'd like omitted from
    their Sudoku Puzzle, then calls functions to generate a puzzle at
    random, omit that many, and then return it to the user."""
    
    print "How many boxes would you like missing from your puzzle?"
    while True:
        print "To quit, enter 81."
        Omissions = input("")
        while type(Omissions) != int or (not -1 < Omissions < 82):
            print "Sorry, you need to enter a number from 0 to 81."
            print "How many boxes would you like missing from your puzzle?"
            print "To quit, enter 81."
            Omissions = input("")
        if Omissions == 0:
            print "Oh, you'd like an answer sheet? Here you go!"
            Puzzle = Answer_Generator.Generate()
        elif Omissions == 81:
            print "Oh, you must be done! We hope you enjoyed the puzzles!"
            return
        else:
            Puzzle = Unsolve(Answer_Generator.Generate(),Omissions)
        print Puzzle
        print "How many boxes would you like missing from your next puzzle?"

def Unsolve(Puzzle, boxes):
    """Given an answer key and a number of boxes, returns a puzzle missing
    precisely that many."""
    # Creates a list of every position still filled in
    filled = [(r,c) for r in xrange(9) for c in xrange(9) ]

    # While there are still boxes to remove
    while len(filled) != (81-boxes):

        # If there wasn't a previous odd-numbered removal,
        if len(filled)%2 == 1:
            # set a random filled value to be removed
            removed = filled.pop(randint(0,len(filled)-1))

        # Otherwise, grab the 'rotationally-symmetrical' value
        else:
            symmy = (8-removed[0],8-removed[1])
            # If it hasn't yet been removed, set it to be
            if symmy in filled:
                filled.remove(symmy)
                removed = symmy
            # Otherwise set a random filled value to be removed
            else:
                removed = filled.pop(randint(0,len(filled)-1))

        # Remove the set value
        Puzzle.setvalue(removed[0],removed[1],' ')
    return Puzzle

if __name__ == '__main__':  main()
