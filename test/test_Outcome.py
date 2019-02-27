# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:49:59 2019

Test class for the Outcome class

@author: HTH
"""

from src.Outcome import Outcome

import unittest

class TestOutcome(unittest.TestCase):
    
    def test_Equality(self):
        self.oc1 = Outcome("Low", 2)
        self.oc2 = Outcome("Low", 2)
        self.assertEqual(self.oc1, self.oc2)
        
    def test_NonEquality(self):
        self.oc1 = Outcome("Low", 2)
        self.oc2 = Outcome("High", 2)
        self.assertNotEqual(self.oc1, self.oc2)
        
if __name__ == "__main__":
    
    unittest.main()