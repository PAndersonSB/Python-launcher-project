class No: # varios methodos de ordenação onde usam o self.proximo
    def __init__(self, nomeArquivo, diretorio, icone, jogadoRecentemente ):
        self.diretorio = diretorio
        self.nomeArquivo = nomeArquivo

        self.icone = icone

        self.jogadoRecentemente = jogadoRecentemente

        self.proximoNomeArquivo = None  # primeiro dado a ser adicionado n tem proximo
        self.anteriorNomeArquivo = None

        self.proximoJogadoRecentemente = None
        self.anteriorJogadoRecentemente = None

    def getProximoNomeArquivo(self):
        return self.proximoNomeArquivo

    def getAnteriorNomeArquivo(self):
        return self.anteriorNomeArquivo

    def getProximoJogadoRecentemente(self):
        return self.proximoJogadoRecentemente

    def getAnteriorJogadoRecentemente(self):
        return self.anteriorJogadoRecentemente

class Lista:
    def __init__(self):
        self.cabecaNomeArquivo = None
        self.cabecaJogadoRecentemente = None

    def adicionarOrdenadoPorNome(self, nomeArquivo, diretorio, icone=None, jogadoRecentemente=None):
        novo_no = No(nomeArquivo, diretorio, icone, jogadoRecentemente)

        if self.cabecaNomeArquivo: #se não for o primeiro elemento a ser adicionado na lista
            ponteiro= self.cabecaNomeArquivo

            while ponteiro.proximoNomeArquivo != self.cabecaNomeArquivo and ponteiro.nomeArquivo <novo_no.nomeArquivo:
                ponteiro = ponteiro.proximoNomeArquivo

            print(ponteiro.nomeArquivo, novo_no.nomeArquivo)

            if ponteiro.diretorio != novo_no.diretorio: #tirando repetição

                if novo_no.nomeArquivo < self.cabecaNomeArquivo.nomeArquivo:#inicio da lista
                    print('inicio')
                    novo_no.proximoNomeArquivo = self.cabecaNomeArquivo
                    novo_no.anteriorNomeArquivo = self.cabecaNomeArquivo.anteriorNomeArquivo

                    ponteiro = self.cabecaNomeArquivo.anteriorNomeArquivo
                    ponteiro.proximoNomeArquivo = novo_no

                    self.cabecaNomeArquivo.anteriorNomeArquivo = novo_no

                    self.cabecaNomeArquivo= novo_no

                elif novo_no.nomeArquivo > ponteiro.nomeArquivo: #fim da lista
                    print('fim')
                    novo_no.proximoNomeArquivo = ponteiro.proximoNomeArquivo
                    novo_no.anteriorNomeArquivo = ponteiro

                    ponteiro.proximoNomeArquivo = novo_no

                    ponteiro = novo_no.proximoNomeArquivo
                    ponteiro.anteriorNomeArquivo = novo_no

                else: #meio da lista
                    print('meio')
                    novo_no.proximoNomeArquivo = ponteiro
                    novo_no.anteriorNomeArquivo = ponteiro.anteriorNomeArquivo

                    ponteiro.anteriorNomeArquivo = novo_no

                    ponteiro = novo_no.anteriorNomeArquivo
                    ponteiro.proximoNomeArquivo = novo_no

            else:
                print('valor repetido')

        else: #se for o primeiro elemento a ser adicionado na lista
            novo_no.proximoNomeArquivo = novo_no
            novo_no.anteriorNomeArquivo = novo_no
            self.cabecaNomeArquivo = novo_no



    def imprimir(self):
        ponteiro = self.cabecaNomeArquivo
        print(ponteiro.nomeArquivo)

        while ponteiro.proximoNomeArquivo != self.cabecaNomeArquivo:
            ponteiro = ponteiro.proximoNomeArquivo

            print(ponteiro.nomeArquivo)


if __name__ == "__main__":
    lista =Lista()
    lista.adicionarOrdenadoPorNome(1, 1)
    lista.adicionarOrdenadoPorNome(20, 20)
    lista.adicionarOrdenadoPorNome(30, 30)
    lista.adicionarOrdenadoPorNome(15, 15)


    lista.imprimir()


