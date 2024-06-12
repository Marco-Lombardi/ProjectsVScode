
with open("/home/user/ProjectsVScode/esempio.txt") as reader:
    
    #lettura e ciclo while su file
    
    line = reader.readline()
    line_counter = 0
    
    while line != '':
        
        print(f"{line} - number: {line_counter}")
        line = reader.readline()
        line_counter += 1 

        
# scrittura su file

with open("/home/user/ProjectsVScode/esempio.txt" "w") as reader:

 reader.write(f"Ciao sono marco")     
    


            
    
    