# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:31:53 2019

@author: HTH
"""

from src.BinBuilder import BinBuilder

#import os

from src.Bin import Bin
from src.Outcome import Outcome

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
        
        """
        We then call the buildBins() function in the 
        BinBuilder class.
        """
        BinBuilder.buildBins(self, self)
        
        self.allOutcomes = None # Collection of all outcomes (TODO)
        
    def addOutcome(self, number, outcome):
        
        # TODO: Add other outcomes here.
        
        if number == "00":
            self.bins[37] = self.bins[37].union(Bin([outcome]))
        else:
            number = int(number)
            self.bins[number] = self.bins[number].union(Bin([outcome]))
            
    def getOutcome(self, name): # Returns outcome if name matches it
        
        # Iterate over all outcomes, return matching ones
        for outcome in self.allOutcomes:
            
            if outcome.name.lower().contains(name.lower()):
                
                return set([outcome])
            
            else:
                
                return set([])
        
    def next(self):
        
        return self.rng
    
    def get(self, number):
        
        return self.bins[number]