# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:41:56 2019

Test class for the Bin Builder class.

@author: HTH
"""

from src.BinBuilder import BinBuilder
from src.Wheel import Wheel

import unittest

class TestOutcome(unittest.TestCase):
    
    def setUp(self):
        
        self.wheel = Wheel()
        self.bb = BinBuilder()
    
    def test_generateStraightBets(self):
        
        self.bb.generateStraightBets(self.wheel)
    
    def test_builder(self):
        
        self.bb.buildBins(self.wheel)
    
if __name__ == "__main__":
    
    unittest.main()