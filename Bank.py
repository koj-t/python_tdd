#!/usr/bin/python
# -*- coding: utf-8 -*-

# import Money
# import Pair


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def rate(self, From, To):
        if From == To:
            return 1
        return self.rates[self.Pair(From, To)]

    def addRate(self, From, To, rate):
        self.rates[self.Pair(From, To)] = rate

    def Pair(self, From, To):
        if From == "USD" and To == "CHF":
            return 0
        elif From == To:
            return 1
        else:
            return 2
