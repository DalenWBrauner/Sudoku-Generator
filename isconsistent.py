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
