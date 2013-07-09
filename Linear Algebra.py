class Matrix(object):
    """A matrix is a set of numbers arranged in a grid with N rows and M columns."""
    def __init__(self, nRows, nCols, values):
        if nRows * nCols != len(values):
            raise TypeError: "A matrix of "+str(nRows)+" Rows and "+str(nCols)+" Columns"+\
            " requires precisely "+str(nRows*nCols)+" values."
        # The actual values are stored in a dictionary, with coordinates such as (0,0) & (1,2)
        # being the keys.
        self.M = {}
        # What sets apart a Matrix from a Dictionary is being able to access the rows/columns.
        self.row = []
        self.vec = []
        # The index is only used to 
        index = 0
        for x in nRows:
            for y in nCols:
                Key = str(x)+","+str(y)
                self.M[Key] = values[index]
                index += 1
                if self.col.has_key(y): self.col[y].append(values[index])
                else:                   self.col[y] = list(values[index])
                if self.row.has_key(x): self.row[x].append(values[index])
                else:                   self.row[x] = list(values[index])
