# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:37:03 2019

Test class for the wheel class

@author: HTH
"""

from src.Bin import Bin
from src.Outcome import Outcome
from src.Wheel import Wheel

import unittest

class TestOutcome(unittest.TestCase):
    
    def setUp(self):
        
        self.wheel = Wheel()
        
        self.outcome0 = Outcome("Number 0", 36)
        self.outcome00 = Outcome("Number 00", 36)
        
        self.bin0 = Bin([self.outcome0])
        self.bin00 = Bin([self.outcome00])
        
    def test_addOutcomesToWheel(self):
        
        self.wheel.addOutcome("0", self.outcome0)
        self.wheel.addOutcome("00", self.outcome00)
        
    def test_binIncludedInWheel(self):
        
        self.assertIn(self.bin0, self.wheel.bins)
        self.assertIn(self.bin00, self.wheel.bins)
                
if __name__ == "__main__":
    
    unittest.main()