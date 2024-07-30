"""
Conversor de Moedas
Crie uma função que converta uma quantia de uma moeda para
outra com base em uma taxa de câmbio fornecida.
"""

def conversor_moedas(quantia, taxa_cambio):

    if quantia < 0 or taxa_cambio <= 0:
        return "Erro: A quantia e a taxa de câmbio devem ser valores positivos."

    return quantia * taxa_cambio

def principal():
    try:
        quantia = float(input("Digite a quantia de moedas: "))
        taxa_cambio = float(input("Digite a taxa de câmbio para a moeda: "))

        resultado = conversor_moedas(quantia, taxa_cambio)

        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"Quantia convertida: {resultado:.2f}")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos :)")


if __name__ == "__main__":
    principal()
