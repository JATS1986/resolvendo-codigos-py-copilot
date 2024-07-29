# Recebendo dois dados diferentes do usuário e concatena-los em uma única string

# Resolução segundo o Gemini 

def verificar_par_ou_impar():
    """Verifica se um número é par ou ímpar utilizando condicionais."""

    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print("O número", numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")

# Chamando a função
verificar_par_ou_impar()