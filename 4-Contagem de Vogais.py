#Contagem de Vogais
#Crie uma função que conte o número de vogais em uma string.

def contar_vogais(texto):
    # Definindo um conjunto de vogais (considerando maiúsculas e minúsculas)
    vogais = 'aeiouAEIOU'
    contador = 0

    for char in texto:
        if char in vogais:
            contador += 1

    return contador

def principal():
    texto = input("Digite uma palavra ou frase para contar o número de vogais: ")
    resultado = contar_vogais(texto)
    print(f"Número de vogais escritas anteriormente: {resultado}")

if __name__ == "__main__":
    principal()
