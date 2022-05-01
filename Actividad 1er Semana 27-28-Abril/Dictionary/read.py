
import pickle
import pprint #para imprimir el dic de forma mas legible en terminal aunque no anida bien

#Para la lectura del binario ahora se utiliza rb, se lee el contenido y se carga gracias
#al archivo binario y el fh para el manejo de archivos
with open('Dictionary.bin','rb') as fh:
    MovDev=pickle.load(fh)
    
    #impresion de la coleccion
    print(MovDev)
    #pprint.pprint(MovDev)
    print(type(MovDev))