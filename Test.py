import unittest, Puzzle, Answer_Generator, Answer_Unsolver

class TestPuzzle(unittest.TestCase):
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

    def test_111(self):
        """Tests basic Sudoku Object functionality."""
        # Creates a Sudoku puzzle of all 1s.
        v = []
        for x in xrange(81):    v.append(1)
        P = Puzzle.Sudoku(v)
        # Confirms the Sudoku Puzzle is converting to a string properly.
        Pstring =  "[ 1 1 1 | 1 1 1 | 1 1 1 ]\n[ 1 1 1 | 1 1 1 | 1 1 1 ]\n" \
                  +"[ 1 1 1 | 1 1 1 | 1 1 1 ]\n_________________________\n" \
                  +"[ 1 1 1 | 1 1 1 | 1 1 1 ]\n[ 1 1 1 | 1 1 1 | 1 1 1 ]\n" \
                  +"[ 1 1 1 | 1 1 1 | 1 1 1 ]\n_________________________\n" \
                  +"[ 1 1 1 | 1 1 1 | 1 1 1 ]\n[ 1 1 1 | 1 1 1 | 1 1 1 ]\n" \
                  +"[ 1 1 1 | 1 1 1 | 1 1 1 ]\n"
        self.assertEqual(str(P),Pstring)

    def test_break__init__(self):
        """Tests denial of invalid inputs to Sudoku objects."""
        # I can't test this until THIS ONE line of code works
        # self.assertRaises(IndexError,[].pop())
##        # Creates invalid lists for testing a list with...
##        a = []  # not enough values
##        b = []  # too many values
##        c = []  # nothing in it
##        f = []  # floats
##        s = []  # strings
##        b = []  # booleans
##        l = []  # lists
##        t = []  # tuples
##        z = []  # a list
##        # Fills these lists
##        for x in xrange(81):
##            a.append(7)
##            b.append(7)
##            f.append(float(x))
##            s.append(str(x))
##            b.append(True)
##            l.append([x])
##            t.append((x))
##            z.append(x)
##        b.append(a.pop())
##        # Tests that Sudoku objects won't accept these as valid input
##        self.assertRaises(TypeError,Puzzle.Sudoku()) # Tests
##        self.assertRaises(TypeError,Puzzle.Sudoku(a))
##        self.assertRaises(TypeError,Puzzle.Sudoku(b))
##        self.assertRaises(TypeError,Puzzle.Sudoku(c))
##        self.assertRaises(TypeError,Puzzle.Sudoku(f))
##        self.assertRaises(TypeError,Puzzle.Sudoku(s))
##        self.assertRaises(TypeError,Puzzle.Sudoku(b))
##        self.assertRaises(TypeError,Puzzle.Sudoku(l))
##        self.assertRaises(TypeError,Puzzle.Sudoku(t))
##        self.assertRaises(TypeError,Puzzle.Sudoku(z))

        def test_Gsec(self):
            """Tests Gsec()"""
            for r in range(3):
                for c in range(3):    assertEquals(Puzzle.Sudoku.Gsec(r,c),1)
                for c in range(3,6):  assertEquals(Puzzle.Sudoku.Gsec(r,c),4)
                for c in range(6,9):  assertEquals(Puzzle.Sudoku.Gsec(r,c),7)
            for r in range(3,6):
                for c in range(3):    assertEquals(Puzzle.Sudoku.Gsec(r,c),2)
                for c in range(3,6):  assertEquals(Puzzle.Sudoku.Gsec(r,c),5)
                for c in range(6,9):  assertEquals(Puzzle.Sudoku.Gsec(r,c),8)
            for r in range(6,9):
                for c in range(3):    assertEquals(Puzzle.Sudoku.Gsec(r,c),3)
                for c in range(3,6):  assertEquals(Puzzle.Sudoku.Gsec(r,c),6)
                for c in range(6,9):  assertEquals(Puzzle.Sudoku.Gsec(r,c),9)

        def test_Gslt(self):
            """Tests Gslt()"""
            pass
            

class TestAnswer_Generator(unittest.TestCase):
    pass

class TestAnswer_Unsolver(unittest.TestCase):
    pass

unittest.main()
