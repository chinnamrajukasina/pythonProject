x = 1
y = 2
print(id(x), "\n", id(y))

if id(x) == id(y):
    print("given item x :", x, " and y : ", y, "are from same memory location")
else:
    print("given item x :", x, " and y is : ", y, "are from different memory location")

