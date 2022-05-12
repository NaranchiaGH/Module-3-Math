#
# select and write 
# one of the following stat functions
#
#def sum(lst): pass
#def avg(l): pass
#def min(l): pass
#def max(l): pass
#def range(l): pass
#def std(l): pass
#def mode(l): pass
@author: "naran"
import random
import statistics


def mode(array):
    List = [random.randint(1, 10) for x in range(50)]
    print(List)
    moda = statistics.mode(List)
    pass
    return moda


print("La moda de este conjunto de numeros aleatorios es: ", mode(10))
