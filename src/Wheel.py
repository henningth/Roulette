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
        
        self.allOutcomes = dict() # Collection of all outcomes
        
        """
        We then call the buildBins() function in the 
        BinBuilder class.
        """
        BinBuilder.buildBins(self, self)
        
    def addOutcome(self, number, outcome):
        
        # TODO: Add other outcomes here.
        
        if number == "00":
            self.bins[37] = self.bins[37].union(Bin([outcome]))
            
            self.allOutcomes["Number 00"] = outcome
        else:
            number = int(number)
            self.bins[number] = self.bins[number].union(Bin([outcome]))
            self.allOutcomes["Number " + str(number)] = outcome
            
    def getOutcome(self, name): # Returns outcome if name matches it
        
        # Iterate over all outcomes, return matching ones
        for outcome in self.allOutcomes:
            
            if outcome.name.lower().contains(name.lower()):
                
                return set([outcome])
            
            else:
                
                return set([])
        
    def next(self):
        
        return random.choice(self.bins) # Returns one of the bins at random
    
    def get(self, number): # Returns bin at index number
        
        return self.bins[number]