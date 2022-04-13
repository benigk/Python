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


def view(re):
    ice = 4
    def k(means):
        return re(means)
    return k

def review(pr):
    return re(pr * 2)

ice = 3
re = view(lambda pr: pr * ice)

review(1)