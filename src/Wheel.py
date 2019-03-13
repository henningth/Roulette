# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:31:53 2019

@author: HTH
"""

from src.BinBuilder import BinBuilder

#import os

from src.Bin import Bin

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
        
    def addOutcome(self, number, outcome):
        
        print("In Wheel.addOutcome")
        
        if number == "00":
            self.bins[37] = outcome
        else:
            number = int(number)
            self.bins[number] = outcome
        
    def next(self):
        
        return self.rng
    
    def get(self, number):
        
        return self.bins[number]