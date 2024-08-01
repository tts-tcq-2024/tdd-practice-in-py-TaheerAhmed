import unittest
from StringCalculator import add
class TestStringCalculator(unittest.TestCase):
        
        def test_expectZeroForEmptyInput(self):
                self.assertEqual(add(""), 0)
                
        def test_expectZeroForSingleZero(self):
                self.assertEqual(add("0"), 0)
                
        def test_expectSumForTwoNumberst(self):
                self.assertEqual(add("1;2"), 3)
                self.assertEqual(add("25;25"),50)
                self.assertEqual(add("4\n5"),9)
                
        def test_ignoreNumbersGreaterThan1000(self):
                self.assertEqual(add("1;1001"), 1)
                self.assertEqual(add("2000;1;4"),5)
                
        def test_expectSumWithCustomDelimiter(self):
                self.assertEqual(add("//;\n1;2"), 3)
                
        def test_expectSumWithNewlineDelimiter(self):
                self.assertEqual(add("1\n2;3"),6);
                self.assertEqual(add("3\n4\n3"),10)
        def test_negative_numbers(self):
                with self.assertRaises(ValueError):
                        add("-1,0,-3")




if __name__ == '__main__':
    unittest.main()
