
import pickle

#Para la lectura del binario ahora se utiliza rb, se podria decir que el archivo
#binario se obtiene y se carga para despues imprimirlo entonces de esta forma llamo,
#a mi archivo binario y puedo cargar su contenido
with open('Tuples.bin','rb') as fh:
    WebDev=pickle.load(fh)
    
    #para la impresion de la coleccion se puede utilizar for o map se puede conseguir,
    #que la coleccion salga sin corchete o comillas y esto se usa en general para el
    #manejo de los datos en las colecciones aunque se puede usar para visual en este caso.
    print('\n'.join(map(str, WebDev)))
    print(type(WebDev))