# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:49:59 2019

Test class for the Outcome class

@author: HTH
"""

from src.Outcome import Outcome

import unittest

class TestOutcome(unittest.TestCase):
    
    def createObjects(self):
        self.oc1 = Outcome("Any craps", 8)
        self.oc2 = Outcome("Any craps", 8)
        
if __name__ == "__main__":
    
    testOutcome = TestOutcome()
    testOutcome.createObjects()