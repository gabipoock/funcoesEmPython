#Conversor de Temperatura
#Crie funções para converter temperaturas entre Celsius, Fahrenheit e Kelvin.

import math

def conversor_temperatura():
    print("Olá, bom dia! Selecione a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5. Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")

    escolha = input("Digite o número da conversão (1/2/3/4/5/6): ")

    if escolha in ['1', '2', '3', '4', '5', '6']:
        valor = float(input("Digite o valor da temperatura: "))

        if escolha == '1':
            print(f"Resultado: {celsius_para_fahrenheit(valor)} °F")
        elif escolha == '2':
            print(f"Resultado: {celsius_para_kelvin(valor)} K")
        elif escolha == '3':
            print(f"Resultado: {fahrenheit_para_celsius(valor)} °C")
        elif escolha == '4':
            print(f"Resultado: {fahrenheit_para_kelvin(valor)} K")
        elif escolha == '5':
            print(f"Resultado: {kelvin_para_celsius(valor)} °C")
        elif escolha == '6':
            print(f"Resultado: {kelvin_para_fahrenheit(valor)} °F")
    else:
        print("Entrada inválida.")

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

if __name__ == "__main__":
    conversor_temperatura()