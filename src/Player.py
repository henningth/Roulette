# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:15:15 2019

Player class

@author: HTH
"""

from src.Bet import Bet

class Player:
    
    def __init__(self, table, stake, roundsToGo):
        
        self.table = table
        self.stake = stake
        self.roundsToGo = roundsToGo # Should this be included?
        
    def playing(self):
        
        # Return true if player is active.
        
        pass
    
    def placeBets(self):
        
        # Update table with player's bets
        
        try:
            chosenOutcome = input("Enter outcome to bet on: ")
            chosenAmount = int(input("Enter amount to bet: "))
            
            bet = Bet(chosenAmount, chosenOutcome)
            
            self.table.placeBet(bet)
            
        except KeyboardInterrupt:
            print("Quitting")
            exit()
    
    def win(self, bet):
        
        # Called by game if this players bet was a winning bet
        # Amount won is returned by bet.winAmount()
        pass
    
    def lose(self, bet):
        
        pass