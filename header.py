#Pacotes De Terceiros
import random

#Classe Jogo
class Game:
    #Método Construtor
    def __init__(self):
        self.arquivo = self.__config(15)
        self.palavras = self.__gerar_palavras(self.arquivo)
        clear()
        self.__menu()
    #End.

    #Métodos Privados
    def __config(self, cursor, opc=0):
        arq_config = open("config.conf", "r")
        arq_config.seek(cursor)
        if opc==1:
            return arq_config.read()
        else:
            for c in arq_config.readline().splitlines():
                return c
    #End.

    def __gerar_palavras(self, arquivo):
        self.__vazio(arquivo)
        arq_palavras = open(arquivo, "r")
        palavras = [x for x in arq_palavras.read().splitlines()]
        arq_palavras.close()
        return palavras
    #End.

    def __incluir_palavras(self, arquivo):
        clear()
        print("JOGO DA VELHA\n")
        arq_palavras = open(arquivo, "a")
        arq_palavras.write("\n")
        print("Favor não incluir palavras com hífens e espaços\n \t Ex.: New York e Hot-Dog\n")
        arq_palavras.write(input("Digite a palavra a ser incluida: "))
        arq_palavras.close()
        if input("Deseja incluir mais uma palavra? (S/N): ").upper() == "S":
            return self.__incluir_palavras("palavras.txt")
        else:
            return self.__menu()
    #End.

    def __resetar_palavras(self, arquivo):
        arq_palavras = open(arquivo, "w")
        arq_palavras.write("")
        arq_palavras.close()
        self.__vazio(arquivo)
        clear()
        print("Arquivo Resetado!\n")
        self.__menu()
    #End.

    def __vazio(self, arquivo):
        with open(arquivo, 'r') as ler:
            primeiro = ler.read(1)
            if not primeiro:
                self.__gerar_arquivo(self.arquivo)
            ler.close()
    #End.

    def __gerar_arquivo(self, arquivo):
        palavras = self.__config(48, 1)[:-2]
        arq_palavras = open(arquivo, "w")
        arq_palavras.write(palavras)
        arq_palavras.close()

    def __jogo(self):
        tentativas = 6
        for i in random.sample(range(len(self.palavras)-1), 1):
            palavra = self.palavras[i]
            palavra_jogador = ["_" for i in palavra]
            letras = []
        while tentativas>0 and tentativas<7:
            clear()
            print("JOGO DA VELHA\n")
            print("Número de Tentativas: ", tentativas)
            for c in palavra_jogador:
                print(c, "", end="")
            print("\t Letras Tentadas: ", letras)
            letra = input("Digite uma letra: ")
            if letra in palavra:
                i = 0
                for c in palavra:
                    if letra==c:
                        palavra_jogador[i] = letra
                    else:
                        pass
                    i += 1
            else:
                letras.append(letra)
                tentativas -= 1

            if not "_" in palavra_jogador:
                clear()
                print("JOGO DA VELHA\n")
                print("Palavra: ", end="")
                for c in palavra_jogador:
                    print(c, "", end="")
                break 
            
        if tentativas>0:
            print("\n   Você Venceu!\n")
            if input("Deseja jogar mais uma vez? (S/N): ").upper() == "S":
                clear()
                return self.__jogo()
            else:
                clear()
                return self.__menu()
        else:
            print("Você perdeu, a palavra era ", palavra, "!")
            if input("Deseja jogar mais uma vez? (S/N): ").upper() == "S":
                clear()
                return self.__jogo()
            else:
                clear()
                return self.__menu()
    #End.

    def __menu(self):
        print("JOGO DA VELHA\n")
        print("1) Jogar")
        print("2) Incluir Palavras")
        print("3) Resetar Palavras")
        print("0) Sair do Jogo\n")
        opcao = int(input("Digite a sua opção: "))
        if opcao == 1:
            return self.__jogo()
        elif opcao == 2:
            return self.__incluir_palavras(self.arquivo)
        elif opcao ==3:
            return self.__resetar_palavras(self.arquivo)
        else:
            return exit()
    #End.
#End.

#Funções Globais
def clear():
    print("\033[H\033[J")
#End.
