import pickle

with open('Tuples.bin','rb') as fh:
    WebDev=pickle.load(fh)
    
    print('\n'.join(map(str, WebDev)))
    print(type(WebDev))