import prog1
import unittest

class Testpalin(unittest.TestCase):
    def test_p(self):
        s = 'hello'
        v = prog1.p(s)
        self.assertEqual(v,'not palindrome')
    def test_not(self):
        s = 'reer'
        n = prog1.p(s)
        self.assertEqual(n,'It is a palindrome') #can't be a negative number 
    def test_notwork(self):
        s = 're3er'
        v = prog1.p(s)
        self.assertEqual(v,'error')




if __name__ == '__main__':
    unittest.main()