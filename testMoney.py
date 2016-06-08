#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from Money import Money
from Bank import Bank
from Money import Sum


class testMoney(unittest.TestCase):

    def testMultiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def testCurrency(self):
        self.assertEqual("USD", Money.doller(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)

    def testEquality(self):
        self.assertTrue(Money.doller(5) == Money.doller(5))
        self.assertTrue(Money.doller(5) != Money.doller(6))
        self.assertTrue(Money.doller(5) != Money.franc(5))

    def testReduceSum(self):
        sum = Sum(Money.doller(3), Money.doller(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(7), result)

    def testReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.doller(1), "USD")
        self.assertEquals(Money.doller(1), result)

    def testReduceMoneyDifferentCurrency(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEquals(Money.doller(1), result)

    def testIdentityRate(self):
        bank = Bank()
        self.assertEquals(1, bank.rate("USD", "USD"))

    def testSimpleAddition(self):
        five = Money.doller(5)
        sum = five + five
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(10), reduced)

    def testPlusReturnsSum(self):
        five = Money.doller(5)
        sum = five + five
        self.assertEquals(five, sum.augend)
        self.assertEquals(five, sum.addend)

    def testMixedAddition(self):
        fiveBucks = Money.doller(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks + tenFrancs, "USD")
        self.assertEquals(Money.doller(10), result)

    def testSumPlusMoney(self):
        fiveBucks = Money.doller(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(fiveBucks, tenFrancs) + fiveBucks
        result = bank.reduce(sum, "USD")
        self.assertEquals(Money.doller(15), result)

    def testSumTimes(self):
        fiveBucks = Money.doller(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(fiveBucks, tenFrancs).times(2)
        result = bank.reduce(sum, "USD")
        self.assertEquals(Money.doller(20), result)

    def testPlusSameCurrencyReturnMoney(self):
        oneBuck1 = Money.doller(1)
        oneBuck2 = Money.doller(1)
        sum = oneBuck1 + oneBuck2
        self.assertTrue(isinstance(sum, Sum))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testMoney)
    unittest.TextTestRunner(verbosity=1).run(suite)
