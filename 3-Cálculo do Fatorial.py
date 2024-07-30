#Cálculo do Fatorial
#Crie uma função para calcular o fatorial de um número.

def fatorial_iterativo(n):
    if n < 0:
        return "Erro: O fatorial não está definido para números negativos."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(n):
    if n < 0:
        return "Erro: O fatorial não está definido para números negativos."
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

def calculadora_fatorial():
    print("Escolha o método para calcular o fatorial:")
    print("1. Iterativo")
    print("2. Recursivo")

    escolha = input("Digite o número do método (1/2): ")

    if escolha in ['1', '2']:
        numero = int(input("Digite um número inteiro não negativo: "))
        if escolha == '1':
            print(f"Resultado (Iterativo): {fatorial_iterativo(numero)}")
        elif escolha == '2':
            print(f"Resultado (Recursivo): {fatorial_recursivo(numero)}")
    else:
        print("Entrada inválida.")

if __name__ == "__main__":
    calculadora_fatorial()
