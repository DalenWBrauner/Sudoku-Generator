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

def Unsolve(Puzzle,boxes):
    """Given an answer key and a number of boxes, returns a puzzle missing
    precisely that many."""
    # Picks the first victim at random.
    r = randint(0,8)
    c = randint(0,8)
    Puzzle.setvalue(r,c,' ')    # Oh yeah, blanks are just ' 's.

    # Now to remove all n-1 others:
    for b in xrange(boxes-1):
        
        # We first pick whether to omit a box from the same row, col or sec.
        rcs = randint(0,2)

        # We keep trying to omit a box until we succeed.
        NoSuccess = True
        while NoSuccess:
        
            # Try to omit a box. If you succeed, break out of the loop.
            try:
                if    rcs == 0:     (r,c) = omit_f_row(Puzzle,r)
                elif  rcs == 1:     (r,c) = omit_f_col(Puzzle,c)
                else:               (r,c) = omit_f_sec(Puzzle,r,c)
                NoSuccess = False
            
            # If omitting fails, incriment rcs by 1 to try something new.
            except ValueError:
                rcs = (rcs + 1)%3

                #...and try again.
                try:
                    if    rcs == 0:     (r,c) = omit_f_row(Puzzle,r)
                    elif  rcs == 1:     (r,c) = omit_f_col(Puzzle,c)
                    else:               (r,c) = omit_f_sec(Puzzle,r,c)
                    NoSuccess = False

                # If it fails again, incriment rcs one last time...
                except ValueError:
                    rcs = (rcs +1)%3
                    try:
                        if    rcs == 0:     (r,c) = omit_f_row(Puzzle,r)
                        elif  rcs == 1:     (r,c) = omit_f_col(Puzzle,c)
                        else:               (r,c) = omit_f_sec(Puzzle,r,c)
                        NoSuccess = False

                    # If THAT doesn't work,
                    # let's try a different box and start over.
                    except ValueError:
                        r = (r+1)%9
                        c = (c+1)%9
    return Puzzle

def omit_f_row(Puzzle,r):
    """Omits a random nonempty value from the row provided and returns the
    omitted value's location."""    
    # Creates a list with the positions of all nonempty values in the row
    nonempty = []
    for v in xrange(9):
        if Puzzle.row[r][v] != ' ':
            nonempty.append(v)
            
    # Selects a random nonempty value in the row
    try:                c = nonempty[randint(0,len(nonempty)-1)]
    except ValueError:  raise ValueError("Nothing left to omit from row.")
    
    # Omits that value from the row, and returns value's the row and column
    Puzzle.setvalue(r,c,' ')
    return (r,c)


def omit_f_col(Puzzle,c):
    """Omits a random nonempty value from the col provided and returns the
    omitted value's location."""
    # Creates a list with the positions of all nonempty values in the column
    nonempty = []
    for v in xrange(9):
        if Puzzle.col[c][v] != ' ':
            nonempty.append(v)
            
    # Selects a random nonempty value in the column
    try:                r = nonempty[randint(0,len(nonempty)-1)]
    except ValueError:  raise ValueError("Nothing left to omit from row.")
    
    # Omits that value from the column, and returns value's the row and column
    Puzzle.setvalue(r,c,' ')
    return (r,c)
    

def omit_f_sec(Puzzle,r,c):
    """Omits a random nonempty value from the sec provided and returns the
    omitted value's location."""
    # The code is largely the same, comments observe differences
    nonempty = []
    index = 0                           # index being the position within the sector
    s = (r/3)*3 + c/3                   # s being the sector the values are in
    for value in Puzzle.sec[s]:
        if value != ' ':
            nonempty.append(index)      # i.e. we append the positions if they are nonempty
        index += 1
    try:
        p = nonempty[randint(0,len(nonempty)-1)]    # p being the position within the sector
    except ValueError:
        raise ValueError("Nothing left to omit from row.")

    # Calculates the row and column of the new value
    r = (s/3)*3 + p/3
    c = p - (p/3)*3 + (s%3)*3
    Puzzle.setvalue(r,c,' ')
    return (r,c)

main()
