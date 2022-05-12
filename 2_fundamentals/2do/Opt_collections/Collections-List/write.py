#List

import random
import pickle

#Lista = random.randint (1,10).
ListWrite = [random.randint(1,10) for x in range(10)]

print("La clase de mi elemento ListRandom es:",(type(ListWrite)))

with open('lista.bin','wb') as fh:
    pickle.dump(ListWrite,fh)
    



    



