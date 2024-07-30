"""
Jogo de Adivinhação
Crie uma função que implemente um jogo de adivinhação onde
o usuário tem que adivinhar um número gerado aleatoriamente.
"""

import random

def jogo_adivinhacao():
    menor = 1
    maior = 100

    numero_secreto = random.randint(menor, maior)
    tentativas = 0
    max_tentativas = 7

    print(f"JOGO DE ADIVINHAÇÃO :)")
    print(f"Tente adivinhar o número entre {menor} e {maior}. Você tem {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite um número como primeira tentativa: "))

            tentativas += 1

            if palpite < numero_secreto:
                print("O número secreto é maior. Tente novamente.")
            elif palpite > numero_secreto:
                print("O número secreto é menor. Tente novamente.")
            else:
                print(f"Uhuuul! Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

    if palpite != numero_secreto:
        print(f"Você não conseguiu adivinhar o número. O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()
