import unittest

from ReverseWordsInAString import ReverseWordsInAString


class ReverseWordsInAStringTest(unittest.TestCase):
    def testReverseWords(self):
        testTarget = ReverseWordsInAString()
        self.assertEqual("ghi def abc", testTarget.reverse_words("abc def  ghi"))


if __name__ == '__main__':
    unittest.main()