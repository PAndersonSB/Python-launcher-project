from lista import *
from sistema import *
from arquivo import *
from pygameTesteEvent import *

#log = os.getlogin() #Retorna o nome do usuário conectado no terminal de controle do processo.
#print(log)

#log =os.times()
#print(log)

class MainApp:
    def __init__(self):
        self.lista = Lista()
        self.csv = Csv()
        self.sistema = Sistema()



if __name__ == "__main__":
    app = MainApp()

    #app.salvar_todos_os_executaveis_da_pasta('C:\Program Files (x86)\Steam\steam\games')

