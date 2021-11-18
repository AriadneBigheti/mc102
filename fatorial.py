
def fatorial(x):
    i = x - 1
    if x == 0:
        f = 1
    else:
        f = x
    while i>0:
        f = f*i
        i= i - 1
    return f
