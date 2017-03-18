from functools import reduce
def format_name(s):
   return s.title()

print (list(map(format_name, ['adam', 'LISA', 'barT'])))

def prod(x, y):
    return x*y

print (reduce(prod, [2, 4, 5, 7, 12]))


