# Recebendo dois dados diferentes do usuário e concatena-los em uma única string

# Resolução segundo o Gemini 

def concatenar_strings():
  """Concatena duas strings fornecidas pelo usuário."""

  # Solicita os dados ao usuário
  dado1 = input("Digite o primeiro dado: ")
  dado2 = input("Digite o segundo dado: ")

  # Concatena as strings
  string_concatenada = dado1 + " " + dado2

  # Imprime o resultado
  print("A string concatenada é:", string_concatenada)

# Chama a função para executar o código
concatenar_strings()