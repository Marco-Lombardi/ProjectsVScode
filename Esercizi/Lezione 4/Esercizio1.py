def subtract_all(x: list[float], y: float) -> list[float]:
    subt: list = []
    for n in x:
        subt.append(n-y)
    return subt


mylist: list = [2, 4, 6, 7, 8]
x: float = 5
print(subtract_all(mylist, x))

print(subtract_all(mylist, 7))







  
