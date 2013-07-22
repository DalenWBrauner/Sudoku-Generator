"""
Here are some fun notes about sectors:
    Given a row number r, and column number c:
    (r/3)*3 + c/3
        tells you which of the 9 sectors your value is in.
    c - (c/3)*3 + (r%3)*3
        tells you which of the 9 slots in a sector your value is in.
"""

#
##
### These functions exist primarily to assist Sudoku object functions
### yet are not exclusive to them.

def any_duplicates(theList):
            """Checks if there are any duplicates in a list."""
            for A in xrange(len(theList)):
                for B in xrange(A+1,len(theList)):
                    if theList[A] == theList[B]:
                        return True
            return False
#
##
### Sudoku object ahoy!
            
class Sudoku(Object):
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

    def isvalid(self):
        """Returns True if the puzzle is a valid Sudoku puzzle, otherwise
        Returns False."""
        for row in self.row:
            if any_duplicates(row):     return False
        for col in self.col:
            if any_duplicates(col):     return False
        for sec in self.sec:
            if any_duplicates(sec):     return False    
        return True

    def setvalue(self,r,c,value):
        """Sets the value located at row number r, column number c, to the
        value provided."""
        self.M[str(r)+","+str(c)] = value
        self.row[r][c] = value
        self.col[c][r] = value
        self.sec[(r/3)*3 + c/3][c - (c/3)*3 + (r%3)*3] = value

    def setrow(self,r,values):       
        if len(values) != 9:
            raise TypeError("Columns require exactly 9 values.")
        
        for n in xrange(self.nCols):
            self.M[str(r)+","+str(n)] = values[n]
            self.row[r][n] = values[n]
            self.col[n][r] = values[n]
            ### NEEDS SECTOR FUNCTIONALITY

    def setcol(self,c,values):
        if len(values) != 9:
            raise TypeError("Columns require exactly 9 values.")
        
        for n in xrange(self.nRows):
            self.M[str(n)+","+str(c)] = values[n]
            self.row[n][c] = values[n]
            self.col[c][n] = values[n]
            ### NEEDS SECTOR FUNCTIONALITY

    def swaprow(self,r1,r2):
        """Swaps row r1 with row r2."""
        # Changes the values of M appropriately
        temp = self.row[r1]
        self.row[r1] = self.row[r2]
        self.row[r2] = temp
        
        # Changes the values of the rows appropriately
        for g in xrange(len(self.row[r1])):
            temp = self.M[str(r1)+","+str(g)]
            self.M[str(r1)+","+str(g)] = self.M[str(r2)+","+str(g)]
            self.M[str(r2)+","+str(g)] = temp
            
        # Changes the values of the columns appropriately
        for col in self.col:
            temp = col[r1]
            col[r1] = col[r2]
            col[r2] = temp

        ### NEEDS SECTOR FUNCTIONALITY

    def swapcol(self,c1,c2):
        """Swaps col c1 with col c2."""
        # Changes the values of M appropriately
        temp = self.col[c1]
        self.col[c1] = self.col[c2]
        self.col[c2] = temp
        
        # Changes the values of the columns appropriately
        for g in xrange(len(self.col[c1])):
            temp = self.M[str(g)+","+str(c1)]
            self.M[str(g)+","+str(c1)] = self.M[str(g)+","+str(c2)]
            self.M[str(g)+","+str(c2)] = temp
            
        # Changes the values of the rows appropriately
        for row in self.row:
            temp = row[c1]
            row[c1] = row[c2]
            row[c2] = temp

        ### NEEDS SECTOR FUNCTIONALITY

#
##
### This just makes my life easier for testing        
solved_puzzle = [2,4,8,3,9,5,7,1,6,5,7,1,6,2,8,3,4,9,9,3,6,7,4,1,5,8,2,6,8,2,5,3,9,1,7,4,3,5, \
                 9,1,7,4,6,2,8,7,1,4,8,6,2,9,5,3,8,6,3,4,1,7,2,9,5,1,9,5,2,8,6,4,3,7,4,2,7,9, \
                 5,3,8,6,1]
Puzzle = Sudoku(solved_puzzle)