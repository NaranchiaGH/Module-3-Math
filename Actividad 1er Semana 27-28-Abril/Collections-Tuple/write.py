#Tuples
import pickle

WebDev = ('1.visual Studio Code','Visual Studio','Notepad++','IntelliJ','Vim',
       'Sublime Text','Android Studio','Eclipse','Atom','Pycharm',
       'PHPStorm','Xcode','IPython/Jupyter','NetBeans','Emacs',
       'RStudio','RubyMine','TextMate','Coda','Komodo','Zend',
       'Light Table')

#Vertir datos de mi elemento 'WebDev' a un .bin
with open ('Tuples.bin','wb') as fh:
    pickle.dump(WebDev,fh)
    
    #Aqui con type confirmo que efectivamente la clase de mi elmento WebDev es tuple
    print("La clase de mi elemento WebDev es ",(type(WebDev)))
    print("Archivo binario creado")
