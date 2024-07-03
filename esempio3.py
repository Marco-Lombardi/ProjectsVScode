# def say_hello(name: str):
    
#     print(f"Hello, {name}")
    
# def say_ciao(name: str) -> None:
    
#     print(f"Ciao, {name}")
    
# def saluta(func):
    
#     func("Flavio")
    
# saluta(say_hello) 
# saluta(say_ciao)

# def parent():
    
#     print(f"Sono in parent")
    
#     def first_child():
        
#         print(f"Sono in first child")
        
#     def second_child(): 
        
#         print(f"Sono in second child")
        
#     return second_child()
    
# parent()

# out_funcion = parent()
# print(out_funcion)
# out_funcion

# def decorator(func):
    
#     def wrapper():
        
#         import time
        
#         start = time.time()
        
#         func()
        
#         end = time.time()
#         elapsed_time = end - start
#         print(f"{elapsed_time}")
        
#     return wrapper    

# def say_hello() -> None:
    
#     print(f"Hello, Flavio")
    
# say_hello = decorator(say_hello)

# say_hello()
# def get_time(func):
    
#     def wrapper(*args):
        
#         import time
        
#         start = time.time()
        
#         func(*args)
        
#         end = time.time()
#         elapsed_time = end - start
#         print(f"{elapsed_time}")
        
#     return wrapper

# @get_time
# def say_hello(name: str) -> None:
     
#     print(f"hello, {name}")
    
# say_hello("Flavio")

# def generator():
    
#     yield "A"
#     yield "B"
#     yield "C"
    
# prova_generatore = generator()
    
# print(next(prova_generatore))
# print(next(prova_generatore))
# print(next(prova_generatore))
    

#import time

#class FileManager:
    
    #def __init__(self, file_name: str, mode: str) -> None:
        
        #self.file_name: str = file_name
        #self.mode: str = mode
        
        
    #def __enter__(self):
        
        #self.file_wrapper = open(self.file_name, self.mode)    
        
import time
        
def funzione(id: int):
    import time
    print(f"{id=} time {time.time()}")
    time.sleep(1.5)
    print(f"{id=} time {time.time()}")
    
if __name__ == "__mian__":
        
    import threading
        
    x: threading.Thread = threading.Thread(target=funzione, args=(1.))
        
    print(f"prima di runnare il thread")
    x.start()
    print(f"ho runnato il therad")
    x.join()    
    print(f"ho finito di runnare il thraed??")
    
    lista_thread: list[threading.Thread] = []
    
    for id in range(3):
        
            x: threading.Thread = threading.Thread(target=funzione, args=(1.))
            lista_thread.append(x)
            print(f"prima di runnare il yherad{time.time}")
            x.start()
            "runnato thread"
            
    for t in lista_thread:
            
            t.join()
            print(f"terminato")
            
            
            
            
            
            
            
            
    
    
    
    
    
            
               