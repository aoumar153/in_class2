import unittest 
import prog2
class Testpalin(unittest.TestCase):
    def test_p(self):
        s = 'hello world it is me , and I know you hate me '
        v = prog2.word(s)
        self.assertEqual(v,11)
    def test_not(self):
        s = 354
        n = prog2.word(s)
        self.assertEqual(n,'error') #can't be a negative number 
    def test_notwork(self):
        s = 'reser was hella cool today'
        v = prog2.word(s)
        self.assertEqual(v,5)




if __name__ == '__main__':
    unittest.main()