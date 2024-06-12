reader = open("/home/user/ProjectsVScode/esempio.txt")

try:
    
    reader.readline()
    print("Sono nell try")
    raise Exception("Eccezzione!")
    
except Exception:
    
    print("sini nella classe")
    
finally:
    
    print(reader)
    reader.close()
    
    print("sono nella finally")
    
# Secondo Metodo    
    
with open("/home/user/ProjectsVScode/esempio.txt") as reader:
        
    reader.readline()
    
    
class ContexManager:
    
    def __enter__(self):
        
        print("Ciao sono nell enter")
        
        return self 
    
    def __exit__(self, exc_type, exc_value, traceback):
        
        if exc_type is not None:
            
            print("Eccezione")
            
        return False
    
try:
    
    with ContexManager() as cm:
        
        print("Ciao")
        print(cm)
        
except Exception:
    
    print()
    
    

               
    
    
        



    






