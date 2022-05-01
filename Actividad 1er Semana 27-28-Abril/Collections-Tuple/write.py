#Tuples
import pickle

WebDev = ('1.visual Studio Code','Visual Studio','Notepad++','IntelliJ','Vim',
       'Sublime Text','Android Studio','Eclipse','Atom','Pycharm',
       'PHPStorm','Xcode','IPython/Jupyter','NetBeans','Emacs',
       'RStudio','RubyMine','TextMate','Coda','Komodo','Zend',
       'Light Table')

#con with open podemos trabajar con binarios ademas de wb(se utilza para escritura),
#podria interpretarse como write bin ya que esa es la funcion, entonces se crea un
#archivo .bin que llame Tuples y escribo lo que hay en WebDev ya que no se puede
#abrir el contenido en binario si no que se utiliza mas como llamado a otra parte o
#archivo de codigo.
with open ('Tuples.bin','wb') as fh:
    pickle.dump(WebDev,fh)
    
    #Aqui con type confirmo que efectivamente la clase de mi elmento WebDev es tuple
    print("La clase de mi elemento WebDev es ",(type(WebDev)))
    print("Archivo binario creado")