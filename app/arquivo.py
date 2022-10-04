import csv
#diretorio nomeArquivo titulo numeroDeCliques icone

class Csv:
    def __init__(self):
        self.dados = None
        self.ler_arquivo('jogos')

    def setDados(self,dados):
        self.dados = dados

    def salvar_em_arquivo(self,nome):
        if self.dados:
            with open(f'{nome}.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                for i in range (0, len(self.dados)):
                    spamwriter.writerow(self.dados[i])
                csvfile.close()

    def ler_arquivo(self,nome):

        with open(f'{nome}.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
            f.close()


if __name__ == "__main__":
    arquivo = Csv()
    arquivo.setDados([['nomeArquivo', 'diretorio', 'icone', 'jogadoRecentemente'],
                      ['nomeArquivo', 'diretorio', 'icone', 'jogadoRecentemente'],
                      ['nomeArquivo', 'diretorio', 'icone', 'jogadoRecentemente']])

    arquivo.salvar_em_arquivo('jogos')


