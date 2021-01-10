def A():
    x = sum([x for x in range(101)])
    return x*x
    
def B():
    return sum([x*x for x in range(101)])

print(A()-B())