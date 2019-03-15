# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:38:46 2019

Game class.

@author: HTH
"""

from src.Bin import Bin
from src.Outcome import Outcome
from src.Wheel import Wheel

class Game:
    
    def __init__(self, wheel, table):
        
        self.wheel
        self.table
    
    def cycle(self, player):
        # Cycles though the steps for a given player
        
        # The player places his bets
        player.placeBets()
        
        # Spin the roulette wheel to get next number
        winningBin = self.wheel.next()
        
        # Check player's bets which are on the table for win or loss
        # Note: For now only assumes one play, we need to change this later 
        # if we want several players
        for bet in self.table.bets:
            
            for outcome in self.wheel.bins:
            
                pass
                #if bet.outcome == wheel