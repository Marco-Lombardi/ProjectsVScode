# Exercise 2 
# 07/05/2024

class Student:

    def __init__(self, name :str, studyProgram :str, age: int, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age=age
        self.gender=gender
    
    def infoperson(self)->str:
        return(f'name is: {self.name} studyprogram is: {self.studyProgram} age is: {self.age} gender: {self.gender}')
        
          

    

Marco = Student("Marco", "Cloud Developer", 23, "Male")
Marwan = Student("Marwan", "Cloud Developer", 19, "Male")

print(Marco.infoperson())      
print(Marwan.infoperson())






        





