import os

from tkinter import filedialog

class Sistema:
    def __init__(self):
        self.pasta = None
        self.arquivo = None

    def setArquivo(self):
        self.arquivo = filedialog.askopenfilename()

    def setPasta(self):
        self.pasta = filedialog.askdirectory()

    def encontrar_arquivos_na_pasta(self):
        for raiz, diretorios, arquivos in os.walk(self.pasta):
            for arquivo in arquivos:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
                if extensao_arquivo =='.exe':
                    print('é um arquivo exe')


    def executar_jogo(self,arquivo):
        os.startfile(arquivo)

if __name__ == "__main__":
    sistema = Sistema()
    sistema.setPasta()
    sistema.encontrar_arquivos_na_pasta()
