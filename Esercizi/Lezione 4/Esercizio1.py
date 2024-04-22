def subtract_all(x: list[float], y: float) -> list[float]:
    subt: list = []
    for n in x:
        subt.append(n-y)
    return subt


mylist: list = [2, 4, 6, 7, 8]
x: float = 5
print(subtract_all(mylist, x))

print(subtract_all(mylist, 7))

# Second exercise
def subtract_twolist(x: list[float], y:list[float]) -> list[float]:
    res: list[float] = []
    for i in range(len(x)):
        diff = (x[i] - y[i])
        res.append(diff)
    return res

list1: list = [1,2,3,4] 
list2: list = [3,6,9,8]   

print(subtract_twolist(list1, list2,))





    











  
