import unittest

class Calculations:
    
    def __init__(self, a: int, b: float) -> None:
        
        self.a: float = a
        self.b: float = b
        
    def get_sum(self):
        
        return self.a + self.b
    
    def get_difference(self):
        
        return self.a - self.b
    
    def get_product(self):
        
        return self.a * self.b
    
    def get_quotient(self):
        
        return self.a / self.b
    
    
    


        