#Calculadora de Média
#Crie uma função que calcule a média de uma lista de números.

def calcular_media(lista):
    if not lista:
        return "Erro: A lista está vazia."

    soma = sum(lista)
    media = soma / len(lista)

    return media

def principal():
    try:
        entrada = input("Digite os números separados por espaço: ")

        # Converte a entrada em uma lista de números (flutuantes)
        lista_numeros = [float(x) for x in entrada.split()]

        resultado = calcular_media(lista_numeros)

        print(f"A média dos números é: {resultado}")

    except ValueError:
        print("Erro: Entrada inválida! Digite apenas números, por favor. :)")


if __name__ == "__main__":
    principal()
