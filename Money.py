#!/usr/bin/python
# -*- coding: utf-8 -*-

#from Sum import *

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, money):
        return self.amount == money.amount and self.currency == money.currency

    def __add__(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def reduce(self, bank, to):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)

    @classmethod
    def doller(cls, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(cls, amount):
        return Money(amount, "CHF")


class Sum:
    def __init__(self, augend, addend ):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        augendAmount = self.augend.reduce(bank, to).amount
        addendAmount = self.addend.reduce(bank, to).amount
        return Money(augendAmount + addendAmount, to)

    def __add__(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))
