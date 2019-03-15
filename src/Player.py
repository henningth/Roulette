# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:15:15 2019

Player class

@author: HTH
"""

class Player:
    
    def __init__(self, table, stake, roundsToGo):
        
        self.table = table
        self.stake = stake
        self.roundsToGo = roundsToGo # Should this be included
        
    def playing(self):
        
        pass
    
    def placeBets(self):
        
        pass
    
    def win(self, bet):
        
        # Called by game if this players bet was a winning bet
        # Amount won is returned by bet.winAmount()
        pass
    
    def lose(self, bet):
        
        pass