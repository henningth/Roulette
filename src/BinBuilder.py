# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:58:31 2019

@author: HTH
"""

from src.Outcome import Outcome

class BinBuilder:
    
    def __init__(self):
        
        pass
    
    def generateStraightBets(self, wheel):
        
        for binIdx in range(37):
            
            #wheel.addOutcome(binIdx, Outcome("Number " + str(binIdx), 35))
            wheel.addOutcome(binIdx, wheel.getOutcome("Number " + str(binIdx)))
            
        # Add 0 and 00
        #wheel.addOutcome(0, Outcome("Number 0", 35))
        #wheel.addOutcome(37, Outcome("Number 00", 35))
        #wheel.addOutcome(0, wheel.getOutcome("Number 0"))
        wheel.addOutcome(37, wheel.getOutcome("Number 00"))
        
    def buildBins(self, wheel):
                
        """
        This function takes a wheel as argument, 
        and assigns Outcomes to Bins
        The outcomes are based on the Roulette rules. 
        """
                
        BinBuilder.generateStraightBets(self, wheel)