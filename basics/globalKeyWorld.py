a = 10
print(id(a))
def local():
    a = 15
    print("local", a)
    x = globals()['a']
    print(id(a))
    a = 20
    print("global inside", a)

    globals()['a'] = 90


local()

print("outside", a)
