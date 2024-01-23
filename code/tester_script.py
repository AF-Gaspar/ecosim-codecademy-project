from creature import *

test = Creature()
test2 = Creature([1,1], 50, .1)

test.consume(test2)

print(test2.is_alive)
print(test.age)
print(test.mass)