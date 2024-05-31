import unittest

from Classe import Calculations

class TestCalc(unittest.TestCase):
    
    def test_sum(self):
        
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_sum()
        
        self.assertEqual(result, 5, msg=f"Error Test Failde the goal was 5, the function returned {result}")    
    
    def test_diff(self):
        
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_difference()
        
        self.assertEqual(result, 5, msg=f"Error Test Failde the goal was 5, the function returned {result}")    
    
    def test_div(self):
        
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_product()
        
        self.assertEqual(result, 5, msg=f"Error Test Failde the goal was 5, the function returned {result}")    
    
if __name__ == "__main__":
    
    unittest.main() 
          