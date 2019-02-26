# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:54:11 2019

Outcome class

@author: HTH
"""

class Outcome:
    
    # Initializer
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds
        
    def winAmount(self, amount):
        return amount*self.odds
    
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
        
    def __ne__(self, other):
        if self.name != other.name:
            return True
        else:
            return False
        
    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return str(self.name) + "(" + str(self.odds) + ":1)"
    
    def __repr(self):
        return "Outcome(" + str(self.name) + ", " + str(self.odds) + ")"