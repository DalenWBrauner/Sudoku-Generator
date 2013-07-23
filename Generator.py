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
    Puzz = [1,4,7,2,5,8,3,6,9,5,2,8,6,3,9,7,4,1,6,9,3,7,1,4,8,2,5,4,7,1,5,8,2,6,9,3,8,5,2,9,\
            6,3,1,7,4,9,3,6,1,4,7,2,5,8,7,1,4,8,2,5,9,3,6,2,8,5,3,9,6,4,1,7,3,6,9,4,7,1,5,8,2]
    Puzzle = Sudoku(Puzz)
    lst = [1,2,3,4,5,6,7,8,9]
    rep = []
    for Q in xrange(9):
        rep.append(lst.pop(randint(0,8-Q)))
    Puzzle.Mass_Replacement(rep)
    if Puzzle.isvalid():
        return Puzzle
    else:
        print "Nine_Factorial error! Puzzle not valid after replacement."

def Column_Shuffler(Puzzle):
    print "Column_Shuffler"
    return Puzzle

def Puzzle_Unsolver(Puzzle,num):
    print "Puzzle_Unsolver"
    return Puzzle

while True:
    aPuzzle = main()
    print aPuzzle
