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

# I'll be honest, I'm about to do this the cheap and easy way.
# I WILL have to redo all of this if I continue writing this program;
# however, I just want to get this done for now.

def main():
    """Asks the user for the number of numbers they'd like to be
    omitted from their Sudoku Puzzle, then calls functions to generate a
    puzzle at random, omit that many, and then return it to the user."""
    while True:
        print "How many boxes would you like missing from your puzzle?"
        print "To quit, enter 81."
        Omissions = input("")
            while type(Omissions) != int or (not -1 < Omissions < 82):
                print "Sorry, you need to enter a number from 0 to 81."
                print "How many boxes would you like missing from your puzzle?"
                print "To quit, enter 81."
                Omissions = input("")
            if Omissions == 0:
                print "Oh, you'd like an answer sheet? Here you go!"
            elif Omissions == 81:
                print "Oh, you must be done! We hope you enjoyed the puzzles!"
                return
    Puzzle = Unsolve(Generate(),Omissions)
    print Puzzle

def Unsolve(Puzzle,boxes):
    """Given an answer key and a number of boxes, returns a puzzle missing
    precisely that many."""
    # Picks the first victim at random.
    r = randint(0,8)
    c = randint(0,8)
    Puzzle.setvalue(r,c,' ')    # Oh yeah, blanks are just ' 's.

    # Now to remove all n-1 others:
    for b in xrange(boxes-1):
        # We first randomly choose whether to omit a box in the same Row,
        # Column or Section (rcs).
        # Then we choose which entry from the row/col/sec to omit (n).
        rcs = randint(0,2)
        n   = randint(0,8)
        if   rcs == 0:
            c = n
        elif rcs == 1:
            r = n
        else:
            # I'll figure this out later
        # Actually fuck, this won't work at all.
        
        Puzzle.setvalue(r,c,' ')
