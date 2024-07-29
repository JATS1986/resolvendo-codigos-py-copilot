# Solicita como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Resolução segundo o Gemini 

def repetir_string(string, numero_repeticoes):
    """
    Repete uma string um determinado número de vezes.

    Args:
        string: A string a ser repetida.
        numero_repeticoes: O número de vezes que a string será repetida.
    """

    # A variável _ é usada como contador descartável, em cada iteração, a string é impressa em nova linha
    for _ in range(numero_repeticoes):
        print(string)

# Obtendo a entrada do usuário
texto = input("Digite uma palavra: ")
repeticoes = int(input("Digite o número de repetições: "))

# Chamando a função para repetir a string
repetir_string(texto, repeticoes)