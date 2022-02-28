def hany(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

#x = hany(pow)(2)(6)
curried_pow = hany(pow)
two_to_the = curried_pow(2)
x = two_to_the(5)
print(x)
