import unittest


class NumberTest(unittest.TestCase):
    # @unittest.expectedFailure
    def test_even(self):
        for i in range(0, 6):
            self.assertEqual(i % 2, 0)

    # @unittest.expectedFailure
    def test_even_with_subtest(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

if __name__ == '__main__':
    unittest.main()
