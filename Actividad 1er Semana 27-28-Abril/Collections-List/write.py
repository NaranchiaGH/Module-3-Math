#List

import random
import pickle

#Lista = random.randint (1,10).
ListWrite = [random.randint(1,10) for x in range(10)]

#1. Aqui se comprueba que el elemento ListRandom es del tipo "list".
print("La clase de mi elemento ListRandom es:",(type(ListWrite)))

#2. Aqui los valores que se guardaran en mi elemento "ListWrite" se 
# escribiran o sobreescribiran en el archivo .bin que se llamara
#"lista.bin", este documento binario se creara mediante pickle con
#'with open', y 'wb' (writebin) señalando que esta en modo
#escritura, y el fh como manejador de archivos, una vez realizado esto
#el "ListWrite" solo servira en caso de que se requiera en este caso
#llenar el .bin con nuevos numeros aleatorios.

with open('lista.bin','wb') as fh:
    pickle.dump(ListWrite,fh)
    
    #3. Una vez que el resultado de nuestro "ListWrite" se sobrescriba en "lista.bin"
    #ya podremos llamar este resultado en otro documento para leerlo solo con el
    #archivo .bin y el file handling 'fh'.
    



    



