import random

class Jogo:
    def __init__(self, lista_de_palavras, tentativas):
        self.lista = lista_de_palavras
        self._palavra_aleatoria = self.aleatoriedade_da_palavra()
        self.digitadas = []
        self.acertadas = []
        self.erradas = []
        self.jogadas = 0
        self.tentativas = tentativas
        self.senha = '.' * len(self._palavra_aleatoria)

    def aleatoriedade_da_palavra(self):
        palavra_aleatoria = random.choice(self.lista)
        return palavra_aleatoria

    def tentativa(self):
        letra = input('Digite a letra: ').lower().strip()
        return letra

    def fazer_tentativa(self):
        while self.jogadas < self.tentativas:
            print(self.senha)

            letra_da_tentativa = self.tentativa()

            if letra_da_tentativa in self.digitadas:
                print('Você já digitou essa letra!')

            elif letra_da_tentativa in self._palavra_aleatoria:
                self.digitadas.append(letra_da_tentativa)
                self.acertadas.append(letra_da_tentativa)
                self.atualizar_senha()
                print('Certo')

            else:
                self.digitadas.append(letra_da_tentativa)
                self.erradas.append(letra_da_tentativa)
                print('Incorreto, tente novamente')

            self.jogadas += 1

        print('Fim do jogo. A palavra era:', self._palavra_aleatoria)

    def atualizar_senha(self):
        self.senha = ''.join(letra if letra in self.acertadas else '.' for letra in self._palavra_aleatoria)

# Exemplo de uso:
lista_palavras = ["gato", "cachorro", "passaro", "peixe", "elefante"]
jogo = Jogo(lista_palavras, tentativas=5)
jogo.fazer_tentativa()
