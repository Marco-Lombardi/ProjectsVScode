try:
    print("Sono nel try")
    raise ValueError()
    
except Exception:
    
    print("sono nell except")
    
else:
    
    print("sono nell'else")
    
finally:
    
    print("sono nel finally")
    
    