def subtract(x: int, y: int):
  sub = x - y
  return sub

operation = subtract(10, 5)

print(operation)

print(subtract(10,5))

# Second exercise
def median(l: list[float]) -> float:

 l = sorted(l)
 mid = len(l) // 2

 if len (l) % 2 != 0: # dispari
  mediana = l[mid]
 else: #pari
  mediana = l[mid] + l[mid - 1]

 return mediana

list = [1, -4, 45, 23]

list2 = [-3, 80, 2, 43, 9]

print(median(list))
print(median(list2))


