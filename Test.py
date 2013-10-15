import unittest, Puzzle, Answer_Generator, Answer_Unsolver

class TestPuzzle(unittest.TestCase):
    def test_any_duplicates(self):
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
        self.assertTrue(not Puzzle.any_duplicates(la))
        self.assertTrue(not Puzzle.any_duplicates(lc))

class TestAnswer_Generator(unittest.TestCase):
    pass

class TestAnswer_Unsolver(unittest.TestCase):
    pass

unittest.main()
