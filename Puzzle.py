"""
[Name]              Puzzle.py
[Author]            Dalen W. Brauner
[DLM]               12/31/2013   01:54 PM
[Purpose]           To allow for the creation and manipulation of Sudoku
                    Puzzles.
"""

#
##
### These functions exist primarily to assist Sudoku object functions
### yet are not exclusive to them.

def any_duplicates(theList):
    """Checks if there are any duplicates in a list."""
    s = set(theList)
    return len(s) != len(theList)

def Gsec(r,c):
    """Returns which of the 9 sectors your value is in."""
    return (r/3)*3 + c/3

def Gslt(r,c):
    """Returns which of the 9 slots in a sector your value is in."""
    return c - (c/3)*3 + (r%3)*3

#
##
### Sudoku object ahoy!
            
class Sudoku(object):
    def __init__(self, values):
        # Checks if there are enough values.
        if 81 != len(values):
            raise TypeError("Sudoku puzzles require precisely 81 values.")
        
        # Checks all values are integers 1-9.
        for value in values:
            if   not type(value) == int:
                raise TypeError("Sudoku puzzles require integers.")
            elif not 0 < value < 10:
                print value
                raise TypeError("Sudoku puzzles require integers 1-9.")

        self.M = {}     # self.M   is the entire matrix of values
        self.row = []   # self.row is the list of values in each row
        self.col = []   # self.col is the list of values in each column
        self.sec = []   # self.sec is the list of values in each sector
        
        # There are 9 rows, columns and sectors.
        for w in xrange(9):
            self.row.append([])
            self.col.append([])
            self.sec.append([])

        # Shall we begin?
        # Adds each value to...
        index = -1
        for r in xrange(9):
            for c in xrange(9):
                index += 1
                Key = str(r)+","+str(c)
                # ...the entire matrix.
                self.M[Key] = values[index]
                # ...their appropriate row.
                self.row[r].append(values[index])
                # ...their appropriate column.
                self.col[c].append(values[index])
                # ...their appropriate sector.
                self.sec[((r/3)*3)+(c/3)].append(values[index])

    def __str__(self):
        # Creates a string to be returned
        string = ""
        for row in xrange(9):
            string += "[ "
            
            # Adds each row to the string
            for value in xrange(9):
                string += str(self.row[row][value])+" "

                # Inserting vertical seperators for sectors
                if value == 2 or value == 5:
                    string += "| "
            string += "]\n"
            
            # Inserting horizontal seperators for sectors
            if row == 2 or row == 5:
                string += ("_"*25)+"\n"
        return string

    def setvalue(self,r,c,value):
        """Sets the value located at row number r, column number c, to the
        value provided."""
        self.M[str(r)+","+str(c)] = value
        self.row[r][c] = value
        self.col[c][r] = value
        self.sec[(r/3)*3 + c/3][c - (c/3)*3 + (r%3)*3] = value

    def setrow(self,r,values):
        """Sets the values of row r to the values provided."""
        if len(values) != 9:
            raise TypeError("Rows require exactly 9 values.")
        
        for c in xrange(9):
            self.M[str(r)+","+str(c)] = values[c]
            self.row[r][c] = values[c]
            self.col[c][r] = values[c]
            self.sec[(r/3)*3 + c/3][c - (c/3)*3 + (r%3)*3] = values[c]

    def setcol(self,c,values):
        """Sets the values of col c to the values provided."""
        if len(values) != 9:
            raise TypeError("Columns require exactly 9 values.")
        
        for r in xrange(9):
            self.M[str(r)+","+str(c)] = values[r]
            self.row[r][c] = values[r]
            self.col[c][r] = values[r]
            self.sec[(r/3)*3 + c/3][c - (c/3)*3 + (r%3)*3] = values[r]

    def swaprow(self,r1,r2):
        """Swaps row r1 with row r2."""
        newr1 = []
        newr2 = []
        for item in self.row[r1]:   newr2.append(item)
        for item in self.row[r2]:   newr1.append(item)    
        self.setrow(r1,newr1)
        self.setrow(r2,newr2)

    def swapcol(self,c1,c2):
        """Swaps col c1 with col c2."""
        newc1 = []
        newc2 = []
        for item in self.col[c1]:   newc2.append(item)
        for item in self.col[c2]:   newc1.append(item)    
        self.setcol(c1,newc1)
        self.setcol(c2,newc2)

    def Mass_Replacement(self,replacements):
        """Replaces all 1s with the first value in the list, all 2s with the
        second, etc."""
        for c in xrange(9):
            for r in xrange(9):
                self.setvalue(r,c,replacements[(self.M[str(r)+","+str(c)])-1])

    def isvalid(self):
        """Returns True if the puzzle's values do not violate Sudoku rules,
        otherwise returns False."""
        TF = True
        for row in self.row:
            if any_duplicates(row):
                print "Duplicates in row",row
                TF = False
        for col in self.col:
            if any_duplicates(col):
                print "Duplicates in col",col
                TF = False
        for sec in self.sec:
            if any_duplicates(sec):
                print "Duplicates in sec",sec
                TF = False
        return TF
    
    def isconsistent(self):
        """Returns True if the puzzle's values in self.row/col/sec match the
        values in self.M, otherwise returns False."""
        TF = True
        for c in xrange(9):
            for r in xrange(9):
                if not (self.M[str(r)+","+str(c)] == self.row[r][c] == self.col[c][r] == self.sec[((r/3)*3)+(c/3)][c - (c/3)*3 + (r%3)*3]):
                    TF =  False
                    print "Value at",r,c,"inconsistent:"
                    print "self.M   ==",self.M[str(r)+","+str(c)]
                    print "self.row ==",self.row[r][c]
                    print "self.col ==",self.col[c][r]
                    print "self.sec ==",self.sec[((r/3)*3)+(c/3)][c - (c/3)*3 + (r%3)*3]
        return TF

    def issolvable(self):
        """Returns True if the puzzle can be solved as-is, otherwise returns
        False."""
        
        pass

    def isunique(self):
        """Returns True if there is only one solution for the puzzle as-is,
        otherwise returns False."""
        pass
