import unittest, Puzzle, Answer_Generator, Answer_Unsolver

class TestPuzzle(unittest.TestCase):
    def setUp(self):
        self.Seed = [9,8,6,7,3,1,4,5,2,2,7,3,5,4,8,9,1,6,5,1,4,9,2,6,3,7,8,\
                     4,6,5,2,8,7,1,3,9,1,2,8,3,5,9,6,4,7,7,3,9,6,1,4,2,8,5,\
                     6,4,2,8,7,3,5,9,1,8,9,1,4,6,5,7,2,3,3,5,7,1,9,2,8,6,4]
    def test_any_duplicates(self):
        """Tests any_duplicates()"""
        la = [1,0]                  # No duplicates
        lb = [1,1]                  # 1 duplicate
        lc = [1,2,3,4,5,6,7,8,9,0]  # Longer list, no duplicates
        ld = [1,1,2,3,4,5,6,7,8,9]  # Longer list, 1 duplicate
        le = [1,1,2,2,3,3,4,4,5,5]  # Longer list, multiple duplicates
        # Makes sure it spots duplicates
        self.assertTrue(Puzzle.any_duplicates(lb))
        self.assertTrue(Puzzle.any_duplicates(ld))
        self.assertTrue(Puzzle.any_duplicates(le))
        # Makes sure it knows there are none
        self.assertFalse(Puzzle.any_duplicates(la))
        self.assertFalse(Puzzle.any_duplicates(lc))

    def test_Gsec(self):
        """Tests Gsec()"""
        for r in range(3):
            for c in range(3):    self.assertEqual(Puzzle.Gsec(r,c),0)
            for c in range(3,6):  self.assertEqual(Puzzle.Gsec(r,c),1)
            for c in range(6,9):  self.assertEqual(Puzzle.Gsec(r,c),2)
        for r in range(3,6):
            for c in range(3):    self.assertEqual(Puzzle.Gsec(r,c),3)
            for c in range(3,6):  self.assertEqual(Puzzle.Gsec(r,c),4)
            for c in range(6,9):  self.assertEqual(Puzzle.Gsec(r,c),5)
        for r in range(6,9):
            for c in range(3):    self.assertEqual(Puzzle.Gsec(r,c),6)
            for c in range(3,6):  self.assertEqual(Puzzle.Gsec(r,c),7)
            for c in range(6,9):  self.assertEqual(Puzzle.Gsec(r,c),8)

##    def test_Gslt(self):
##        """Tests Gslt()"""

    def test_break__init__(self):
        """Tests denial of invalid inputs to Sudoku objects."""
        # Creates invalid lists for testing a list with...
        a = []  # not enough values
        b = []  # too many values
        c = []  # nothing in it
        f = []  # floats
        s = []  # strings
        b = []  # booleans
        l = []  # lists
        t = []  # tuples
        z = []  # a list
        # Fills these lists
        for x in xrange(81):
            a.append(7)
            b.append(7)
            f.append(float(x))
            s.append(str(x))
            b.append(True)
            l.append([x])
            t.append((x))
            z.append(x)
        b.append(a.pop())
        # Tests that Sudoku objects won't accept these as valid input
        self.assertRaises(TypeError,Puzzle.Sudoku) # Tests
        self.assertRaises(TypeError,Puzzle.Sudoku,a)
        self.assertRaises(TypeError,Puzzle.Sudoku,b)
        self.assertRaises(TypeError,Puzzle.Sudoku,c)
        self.assertRaises(TypeError,Puzzle.Sudoku,f)
        self.assertRaises(TypeError,Puzzle.Sudoku,s)
        self.assertRaises(TypeError,Puzzle.Sudoku,b)
        self.assertRaises(TypeError,Puzzle.Sudoku,l)
        self.assertRaises(TypeError,Puzzle.Sudoku,t)
        self.assertRaises(TypeError,Puzzle.Sudoku,z)
        
    def test__init__(self):
        """Confirms Sudoku Objects are created properly."""
        P = Puzzle.Sudoku(self.Seed)

        # Tests the matrix was appended to correctly
        for N in xrange(81):
            self.assertEqual(P.M[str(N/9)+","+str(N%9)],self.Seed[N])
        
        for N in xrange(9):
            # Tests that rows were appended to correctly
            CorrectRow = self.Seed[N*9:N*9 +9]
            self.assertEqual(P.row[N],CorrectRow)
            
            # Tests that columns were appended to correctly
            CorrectCol = []
            for x in xrange(9): CorrectCol.append(self.Seed[N+(x*9)])
            self.assertEqual(P.col[N],CorrectCol)
            
            # Tests that sectors were appended to correctly
            A = (N/3)*27
            B = (N%3)*3
            self.assertEqual(P.sec[N],
                             self.Seed[(0+A):(9+A)][(0+B):(3+B)]\
                             + self.Seed[(9+A):(18+A)][(0+B):(3+B)]\
                             + self.Seed[(18+A):(27+A)][(0+B):(3+B)])

    def test__str__(self):
        """Confirms Sudoku Puzzles are converting to strings properly."""
        P = Puzzle.Sudoku(self.Seed)
        G = Puzzle.Sudoku(self.Seed)
        G.row[0][0] = ' '
        Pstring = "[ 9 8 6 | 7 3 1 | 4 5 2 ]\n[ 2 7 3 | 5 4 8 | 9 1 6 ]\n" \
                  +"[ 5 1 4 | 9 2 6 | 3 7 8 ]\n_________________________\n"\
                  +"[ 4 6 5 | 2 8 7 | 1 3 9 ]\n[ 1 2 8 | 3 5 9 | 6 4 7 ]\n"\
                  +"[ 7 3 9 | 6 1 4 | 2 8 5 ]\n_________________________\n"\
                  +"[ 6 4 2 | 8 7 3 | 5 9 1 ]\n[ 8 9 1 | 4 6 5 | 7 2 3 ]\n"\
                  +"[ 3 5 7 | 1 9 2 | 8 6 4 ]\n"
        Gstring = "[   8 6 | 7 3 1 | 4 5 2 ]\n[ 2 7 3 | 5 4 8 | 9 1 6 ]\n" \
                  +"[ 5 1 4 | 9 2 6 | 3 7 8 ]\n_________________________\n"\
                  +"[ 4 6 5 | 2 8 7 | 1 3 9 ]\n[ 1 2 8 | 3 5 9 | 6 4 7 ]\n"\
                  +"[ 7 3 9 | 6 1 4 | 2 8 5 ]\n_________________________\n"\
                  +"[ 6 4 2 | 8 7 3 | 5 9 1 ]\n[ 8 9 1 | 4 6 5 | 7 2 3 ]\n"\
                  +"[ 3 5 7 | 1 9 2 | 8 6 4 ]\n"
        self.assertEqual(   str(P),Pstring)
        self.assertEqual(   str(G),Gstring)
        self.assertNotEqual(str(P),Gstring)
        self.assertNotEqual(str(G),Pstring)

##class TestAnswer_Generator(unittest.TestCase):

##class TestAnswer_Unsolver(unittest.TestCase):

unittest.main()
