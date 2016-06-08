import unittest
import fizzbuzz_main as fbm


class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz3(self):
        actual = fbm.fizzbuzz(3)
        self.assertEqual("Fizz", actual)

    def test_fizzbuzz5(self):
        actual = fbm.fizzbuzz(5)
        self.assertEqual("Buzz", actual)

    def test_fizzbuzz4(self):
        actual = fbm.fizzbuzz(4)
        self.assertEqual("4", actual)

    def test_fizzbuzz6(self):
        actual = fbm.fizzbuzz(6)
        self.assertEqual("Fizz", actual)

    def test_fizzbuzz10(self):
        actual = fbm.fizzbuzz(10)
        self.assertEqual("Buzz", actual)

    def test_fizzbuzz8(self):
        actual = fbm.fizzbuzz(8)
        self.assertEqual("8", actual)

    def test_fizzbuzz15(self):
        actual = fbm.fizzbuzz(15)
        self.assertEqual("FizzBuzz", actual)

    def test_fizzbuzzA(self):
        actual = fbm.fizzbuzz("a")
        self.assertEqual("a", actual)

if __name__ == '__main__':
    unittest.main()
