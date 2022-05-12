#
import pickle

MovDev = {'1':'Android Studio','2':'Visual Studio Code','3':'Xcode',
          '4':'Visual Studio','5':'IntelliJ','6':'Notepad++',
          '7':'Sublime Text','8':'Vim','9':'Atom','10':'Eclipse',
          '11':'PyCharm','12':'PHPStorm','13':'NetBeans','14':'IPython/Jupyter',
          '15':'Emacs','16':'TextMate','17':'RStudio','18':'RubyMine','19':'Coda',
          '20':'Zend','21':'Komodo','22':'Light Table'}

with open ('Dictionary.bin','wb') as fh:
    pickle.dump(MovDev,fh)
    
    print("La clase de mi elemento MovDev es ",(type(MovDev)))
    print("Archivo binario creado")