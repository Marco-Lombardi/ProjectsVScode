
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if alice.age > bob.age:
    print(alice.age)
else:
    print(bob.age)






