# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:38:46 2019

Game class.

@author: HTH
"""

from src.Bin import Bin
from src.Outcome import Outcome
from src.Player import Player
from src.Table import Table
from src.Wheel import Wheel

class Game:
    
    def __init__(self, wheel, table):
        
        self.wheel = wheel
        self.table = table
    
    def cycle(self, player):
        # Cycles though the steps for a given player
        
        # The player places his bets
        player.placeBets(self)
        
        print("Bets on table: ")
        
        for bet in self.table.bets:
            
            print(bet, " by player ", player.name)
        
        # Spin the roulette wheel to get next number
        winningBin = self.wheel.next()
        
        print("Winning bin: ", winningBin)
        
        # Check player's bets which are on the table for win or loss
        # Note: For now only assumes one play, we need to change this later 
        # if we want several players
        for bet in self.table.bets: # Cycle through all bets placed on the table
                        
            for outcome in winningBin: # Cycle through all outcomes in the winning bin
                            
                if bet.outcome == outcome:
                    
                    print("Congratulations, you won!")
                    
                    player.win(bet)
                    
                #else:
                    
                    #print("Sorry, this bet didn't win!")
                    
                    #player.lose(bet)

if __name__ == "__main__":
    
    # Main entry point of the game
    
    wheel = Wheel()
    table = Table(100,1)
    game = Game(wheel, table)
    
    # Creates a player
    playerName = input("Choose player name: ")
    
    player = Player(playerName, table, 100, 5)
    
    # Runs the Roulette game
    game.cycle(player)
    