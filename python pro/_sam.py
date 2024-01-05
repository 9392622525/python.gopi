def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def cal(func):
    def inner(func):
        return func
    return inner
add = cal(add)
print(add)

