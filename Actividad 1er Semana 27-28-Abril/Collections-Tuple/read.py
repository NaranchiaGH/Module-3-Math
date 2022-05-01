
import pickle

#Utilizo 'rb' señalando que es para modo lectura,
#y los datos del .bin los transcribo al nuevo elemento,
#WebDev se cargan los datos para utilizarlos despues.
with open('Tuples.bin','rb') as fh:
    WebDev=pickle.load(fh)
    
    #impresion de los datos utilizando map() para mejor,
    #lectura de los mismos.
    print('\n'.join(map(str, WebDev)))
    print(type(WebDev))
