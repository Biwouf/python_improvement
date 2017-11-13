#! /usr/bin/env python3
# coding: utf-8

import logging as lg

lg.basicConfig(level=lg.DEBUG) 

def number(func):
        def inner(self, *args, **kwargs):
            print('Nombre de manchots :', self.TOTAL)
            return func(self, *args, **kwargs)
        return inner

class Penguins:
    TOTAL = 2
    
    
    @classmethod
    def total(self):
        return self.TOTAL
    
    @number
    def add(self):
        self.TOTAL += 1
    
    @number
    def remove(self):
        self.TOTAL -= 1
        
if __name__ == "__main__":
    p = Penguins()
    p.add()
    p.remove()
    print(Penguins.total())