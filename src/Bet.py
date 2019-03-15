# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:43:34 2019

Bet class.

@author: HTH
"""

class Bet:
    
    def __init__(self, amount, outcome):
        
        self.amount = amount
        self.outcome = outcome
        
    def winAmount(self):
        
        # Returns amount won
        # Run this function if player's bet contains an
        # outcome which is equal to the Bin outcome
        pass
    
    def loseAmount(self):
        
        # Returns amount lost
        pass
        
    def __str__(self):
        
        return str(self.amount) + " on " + str(self.outcome)
    
    def __repr__(self):
        
        return "Bet(" + str(self.amount) + "," + str(self.outcome) + ")"