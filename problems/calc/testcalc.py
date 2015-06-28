'''
Created on Jan 22, 2015

@author: Superman
'''
import unittest
from calculator import Calculator
class testCalc(unittest.TestCase):
    def testAdd(self):
        calculator = Calculator()
        result = calculator.add(operanda=2, operandb=3)
        self.assertEqual(result, 5, "Addition fail")