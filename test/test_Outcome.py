# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:49:59 2019

Test class for the Outcome class.

@author: HTH
"""

from src.Outcome import Outcome

#from ..src import Outcome

import unittest

class TestOutcome(unittest.TestCase):
    
    def setUp(self):
        self.oc1 = Outcome("Low", 2)
        self.oc2 = Outcome("Low", 2)
        self.oc3 = Outcome("High", 2)
    
    def test_Equality(self):
        self.assertEqual(self.oc1, self.oc2)
        
    def test_NonEquality(self):
        self.assertNotEqual(self.oc1, self.oc3)
        
if __name__ == "__main__":
    
    unittest.main()