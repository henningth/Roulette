# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:31:53 2019

@author: HTH
"""

from src.BinBuilder import BinBuilder

#import os

from src.Bin import Bin
from src.Outcome import Outcome

import random

class Wheel:
    
    def __init__(self):
        
        """
        This constructor creates a wheel with 38 bins,
        and calls uses the methods of the BinBuilder class
        to create Outcomes and assign them to the Bins.
        """
                
        # Creates the wheel with 38 bins
        # Right now, it is a list with 38 entries
        self.bins = list( Bin() for i in range(38) )
        
        # Collection of all outcomes
        # Used in getOutcome to return a desired outcome
        self.allOutcomes = dict()
        
        # Populates the allOutcomes dictionary
        self.populateOutcomeDict()
        
        """
        We then call the buildBins() function in the 
        BinBuilder class.
        """
        BinBuilder.buildBins(self, self)
        
    def populateOutcomeDict(self):
        
        """
        This function fills the allOutcomes dict with the outcomes and their odds.
        The reason is that the definition of odds is done in one place only.
        Note: The assignment of outcomes into bins is *not* done here, 
        but in the addOutcome function (which is called from the 
        BinBuilder class.)
        TODO: Maybe move to separate builder class.
        """
        
        # Straight bets (single numbers)
        self.allOutcomes["Number 00"] = Outcome("Number 00", 35)
        
        for number in range(37):
            
            self.allOutcomes["Number " + str(number)] = Outcome("Number " + str(number), 35)
        
    def addOutcome(self, number, outcome):
        
        # Adds outcomes to bins
        
        if number == "00":
            self.bins[37] = self.bins[37].union(Bin([outcome]))
            
            #self.allOutcomes["Number 00"] = outcome
        else:
            number = int(number)
            self.bins[number] = self.bins[number].union(Bin([outcome]))
            #self.allOutcomes["Number " + str(number)] = outcome
            
    # Returns outcome if name matches it
    # Factory function
    def getOutcome(self, name):
        
        # Iterate over all outcomes, return matching ones
        for outcome in self.allOutcomes.values():
            
            if outcome.name.lower() == name.lower():
                
                return outcome
        
        return None
        
    def next(self):
        
        return random.choice(self.bins) # Returns one of the bins at random
    
    def get(self, number): # Returns bin at index number
        
        return self.bins[number]