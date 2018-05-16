import unittest

from django.forms.widgets import Widget

from tdd.portfolio import Portfolio


class PortfolioTest(unittest.TestCase):

    def test_google(self):
        p = Portfolio()
        # p.buy("google", 100, 176.48)
        # self.assertEqual(17648.0, p.cost())

        # Exception Test
        with self.assertRaises(Exception) as context:
            p.buy("google", "many", 176.48)

        self.assertTrue("shares must be an interger", context.exception)

    def test_google_yahoo(self):
        p = Portfolio()
        p.buy("google", 100, 176.48)
        p.buy("Yahoo", 100, 36.15)
        self.assertEqual(21263.0, p.cost())


if __name__ == '__main__':
    unittest.main()
