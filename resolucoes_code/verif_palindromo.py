# Recebendo dois dados diferentes do usuário e concatena-los em uma única string

# Resolução segundo o Gemini 

def verificar_palindromo(palavra):
  """Verifica se uma palavra é um palíndromo."""

  # Inverte a palavra utilizando slicing
  palavra_invertida = palavra[::-1]

  # Compara a palavra original com a invertida
  if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
  else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

# Obtendo a palavra do usuário
palavra = input("Digite uma palavra: ")

# Chamando a função para verificar
verificar_palindromo(palavra)