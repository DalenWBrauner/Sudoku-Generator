class Matrix(object):
    """A matrix is a set of numbers arranged in a grid with N rows and M columns."""

    # All a matrix needs is the number of rows and columns, and the values themselves.
    def __init__(self, nRows, nCols, values):

        self.nRows = nRows
        self.nCols = nCols

        # Checks if there are enough values.
        if nRows * nCols != len(values):
            raise TypeError("A matrix of "+str(nRows)+" Rows and "+str(nCols)+" Columns"+\
            " requires precisely "+str(nRows*nCols)+" values.")
        
        # The actual values are stored in a dictionary, with coordinates such as (0,0) & (1,2)
        # being the keys.
        self.M = {}
        
        # What sets apart a Matrix from a Dictionary is being able to access the rows/columns.
        self.row = []
        self.col = []
        
        # The index is only used to keep track of which value needs to be recorded.
        index = -1
        
        for x in xrange(nRows):
            for y in xrange(nCols):
                index += 1
                
                # For each value, the key is a string
                Key = str(x)+","+str(y)
                self.M[Key] = values[index]

                
                # If the row does not yet exist, create the list
                try:
                    self.row[x].append(values[index])
                except IndexError:
                    self.row.append([])
                    self.row[x].append(values[index])
                # If the col does not yet exist, create the list
                try:
                    self.col[y].append(values[index])
                except IndexError:
                    self.col.append([])
                    self.col[y].append(values[index])

    def __str__(self):
        string = ""
        for row in self.row:
            string += "(  "
            for value in row:
                string += str(value)+"  "
            string += ")\n"
        return string

    def dimcol(self):
        return self.nCols

    def dimrow(self):
        return self.nRows

    def getvalue(self,r,c):
        return self.M[str(r)+","+str(c)]

    def getrow(self,x):
        return self.row[r]

    def getcol(self,c):
        return self.col[c]

    def setvalue(self,r,c,value):
        self.M[str(r)+","+str(c)] = value
        self.row[r][c] = value
        self.col[c][r] = value

    def setrow(self,r,values):
        # Checks this request will work in the first place
        if   len(values) > self.nCols:  raise TypeError("Too many values; need "+\
                                                        str(self.nCols)+".")
        elif len(values) < self.nCols:  raise TypeError("Not enough values; need "+\
                                                        str(self.nCols)+".")
        else:
            for n in xrange(self.nCols):
                self.M[str(r)+","+str(n)] = values[n]
                self.row[r][n] = values[n]
                self.col[n][r] = values[n]

    def setcol(self,c,values):
        # Checks this request will work in the first place
        if   len(values) > self.nRows:  raise TypeError("Too many values; need "+\
                                                        str(self.nRows)+".")
        elif len(values) < self.nRows:  raise TypeError("Not enough values; need "+\
                                                        str(self.nRows)+".")
        else:
            for n in xrange(self.nRows):
                self.M[str(n)+","+str(c)] = values[n]
                self.row[n][c] = values[n]
                self.col[c][n] = values[n]

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

class Sudoku(Matrix):

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

        self.M = {}
        self.row = []
        self.col = []
        
        # The row/col lists are given 9 sublists ahead of time.
        for w in xrange(9):
            self.row.append([])
            self.col.append([])
            
        index = -1
        for x in xrange(9):
            for y in xrange(9):
                index += 1
                Key = str(x)+","+str(y)
                self.M[Key] = values[index]
                self.row[x].append(values[index])
                self.col[y].append(values[index])
    
    def __str__(self):
        # The only difference between this string and the original string is that sectors are
        # more clearly visible, and brackets are used instead.
        string = ""
        for row in xrange(9):
            string += "[ "
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
        """Returns True if the puzzle is a valid Sudoku puzzle, False if not."""


        def any_duplicates(theList):
            """Checks if there are any duplicates in a list."""
            for A in xrange(len(theList)):
                for B in xrange(A+1,len(theList)):
                    if theList[A] == theList[B]:
                        return True
            return False

                
        for row in self.row:
            if any_duplicates(row):     return False
        for col in self.col:
            if any_duplicates(col):     return False
        
        return True
               
solved_puzzle = [2,4,8,3,9,5,7,1,6,5,7,1,6,2,8,3,4,9,9,3,6,7,4,1,5,8,2,6,8,2,5,3,9,1,7,4,3,5, \
                 9,1,7,4,6,2,8,7,1,4,8,6,2,9,5,3,8,6,3,4,1,7,2,9,5,1,9,5,2,8,6,4,3,7,4,2,7,9, \
                 5,3,8,6,1]
