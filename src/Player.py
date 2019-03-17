# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:15:15 2019

Player class

@author: HTH
"""

from src.Bet import Bet

class Player:
    
    def __init__(self, name, table, stake, roundsToGo):
        
        self.name = name
        self.table = table
        self.stake = stake
        self.roundsToGo = roundsToGo # Should this be included?
        
    def playing(self):
        
        # Return true if player is active.
        
        pass
    
    def placeBets(self, game):
        
        # Update table with player's bets
        
        try:
            
            #chosenCommand = input("Enter one or several bets, q to stop betting this round.")
            
            chosenCommand = ""
            
            while chosenCommand != "q": # Player can bet as long as he has money
                
                chosenOutcome = input("Enter outcome to bet on: ")
                
                chosenOutcome = "Number " + chosenOutcome
                
                chosenOutcome = game.wheel.getOutcome(chosenOutcome)
                
                chosenAmount = int(input("Enter amount to bet: "))
                
                bet = Bet(chosenAmount, chosenOutcome)
                
                self.table.placeBet(bet)
                
                self.stake -= bet.amount
                
                print("Stake left: ", self.stake)
                
                chosenCommand = input("Enter q to stop betting, any other key to continue.")
            
        except KeyboardInterrupt:
            print("Quitting")
            exit()
    
    def win(self, bet):
        
        # Called by game if this players bet was a winning bet
        # Amount won is returned by bet.winAmount()
        self.stake += bet.amount
    
    def lose(self, bet):
        
        pass