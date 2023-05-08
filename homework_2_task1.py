# ex1

# part a
a = 7
b = 9

c = a
a = b
b = c
print("Часть первая: a =", a, "b =", b)

# part b
a = 10
b = 11
a, b = b, a
print("Часть вторая: a =", a, "b =", b)

# part c
a = 20
b = 25
a = a + b
b = a - b
a = a - b
print("Часть третья: a =", a, "b =", b)

