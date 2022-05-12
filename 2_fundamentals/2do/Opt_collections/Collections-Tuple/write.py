#Tuples
import pickle

WebDev = ('1.visual Studio Code','Visual Studio','Notepad++','IntelliJ','Vim',
       'Sublime Text','Android Studio','Eclipse','Atom','Pycharm',
       'PHPStorm','Xcode','IPython/Jupyter','NetBeans','Emacs',
       'RStudio','RubyMine','TextMate','Coda','Komodo','Zend',
       'Light Table')

with open ('Tuples.bin','wb') as fh:
    pickle.dump(WebDev,fh)
    
    print("La clase de mi elemento WebDev es ",(type(WebDev)))
    print("Archivo binario creado")