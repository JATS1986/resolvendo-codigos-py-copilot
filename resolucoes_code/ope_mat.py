# Solicita como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Resolução segundo o Gemini 

def calculadora_simples():
    """Realiza operações simples entre dois números."""

    # Obtém os números do usuário
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Obtém a operação desejada
    operacao = input("Digite a operação (+, -, *, /): ")

    # Realiza a operação e exibe o resultado
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = abs(num1 - num2)
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Divisão por zero não é permitida.")
        else:
            resultado = num1 / num2
    else:
        print("Operação inválida.")

    if 'resultado' in locals():
        print("Resultado:", resultado)

# Chama a função para executar o programa
calculadora_simples()