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
        self.row = {}
        self.col = {}
        
        # The index is only used to keep track of which value needs to be recorded.
        index = -1
        
        for x in xrange(nRows):
            for y in xrange(nCols):
                index += 1
                
                # For each value, the key is a string
                Key = str(x)+","+str(y)
                self.M[Key] = values[index]
                
                # If the column does not yet exist, create the list
                if not self.col.has_key(y):     self.col[y] = []
                self.col[y].append(values[index])
                if not self.row.has_key(x):     self.row[x] = []
                self.row[x].append(values[index])

    def __str__(self):
        superstring = ""
        for row in self.row.values():
            string = "(  "
            for value in row:
                string += str(value)+"  "
            string += ")\n"
            superstring += string
        return superstring

    def getvalue(self,x,y):
        return self.M[str(x)+","+str(y)]

    def getrow(self,x):
        return self.row[x]

    def getcol(self,y):
        return self.col[y]

    def setvalue(self,x,y,value):
        self.M[str(x)+","+str(y)] = value
        self.row[x][y] = value
        self.col[y][x] = value

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
##        for col in self.col:
##            temp = self.col[r1]
##            self.col[r1] = self.col[r2]
##            self.col[r2] = self.col[r1]

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
##        for row in self.row:
##            temp = self.row[c1]
##            self.row[c1] = self.row[c2]
##            self.row[c2] = self.row[c1]
        
