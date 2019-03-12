# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:43:07 2019

Test class for the Bin class.

@author: HTH
"""

from src.Bin import Bin
from src.Outcome import Outcome

import unittest

class TestBin(unittest.TestCase):
    
    def setUp(self):
        
        self.five = Outcome("00-0-1-2-3", 6)
        self.zero = Bin([Outcome("0", 35), self.five])
        self.zerozero = Bin([Outcome("00", 35), self.five])
        
    def test_SetEquality(self):
        
        self.assertSetEqual(self.zero, Bin([Outcome("0", 35), self.five]))
        self.assertSetEqual(self.zerozero, Bin([Outcome("00", 35), self.five]))
        
    def test_SetMembership(self):
        
        self.assertIn(self.five, self.zero)
                        
if __name__ == "__main__":
    
    unittest.main()