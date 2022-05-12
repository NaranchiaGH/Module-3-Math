
import pickle
import statistics #para calcular el 'average' y 'moda'

#Ahora a diferencia de el otro archivo aqui se cambia el 'wb'
#por un 'rb' esto se refiere a que el archivo lista.bin se
#pondra en modo de lectura, ya que solo recibira datos.
with open('lista.bin','rb') as fh:
    ListRead = pickle.load(fh)
    #Aqui creo un nuevo elemento que llamo 'ListRead' este
    #llamara lo que contiene 'lista.bin' y asi podre
    #utilizar esos datos en este documento.
    
    print(type(ListRead)) #Para verificar el tipo
    print(ListRead,"\n")
    
    suma = sum(ListRead) #Calcular la suma del conjunto.
    print("La suma es de:",suma,"\n")
    
    avg = statistics.mean(ListRead) #Calcular el avg o promedio
    print("El promedio de este conjunto de numeros aleatorios es:"
          ,avg,"\n") #El total se divide entre 10 (cantidad de valores)
    
    moda = statistics.mode(ListRead) #Calcular moda
    print("La moda de este conjunto de numeros aleatorios es:"
          ,moda,"\n")
