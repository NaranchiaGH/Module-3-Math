import pickle
import pprint 

with open('Dictionary.bin','rb') as fh:
    MovDev=pickle.load(fh)
    
    print(MovDev)
    pprint.pprint(MovDev)
    print(type(MovDev))