# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:58:31 2019

@author: HTH
"""

from src.Outcome import Outcome
from src.Wheel import Wheel

class BinBuilder:
    
    def __init__(self):
        
        pass
    
    def generateStraightBets(self):
        
        tempBinList = list(range(38))
        
        for binIdx in range(1,37):
            
            tempBinList[binIdx] = Outcome("Number " + binIdx, 35)
            
        # Add 0 and 00
        tempBinList[0] = Outcome("Number 0", 35)
        tempBinList[37] = Outcome("Number 00", 35)
        
        return tempBinList
    
    def buildBins(self, Wheel):
        
        """
        This function takes a wheel as argument, 
        and assigns Outcomes to Bins
        The outcomes are based on the Roulette rules. 
        """
        
        print("In BinBuilder.buildBins")
        
        Wheel.addOutcome(0, Outcome("Number 0", 35))
        
        #tempBinList = self.generateStraightBets()
        
        #Wheel.addOutcome()