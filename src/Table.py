# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:51:18 2019

Table class.

@author: HTH
"""

from src.Wheel import Wheel

class InvalidBet(Exception):
    
    pass

class Table:
    
    def __init__(self, limit, minimum):
        
        self.limit = limit # Bet limit
        self.minimum = minimum # Minimum bet allowed
        
        self.bets = [] # List of bets
        
    def placeBet(self, bet):
        
        if bet is not Wheel.getOutcome(name):
            
            raise InvalidBet("Invalid bet")
    
    def isValid(self):
        
        pass