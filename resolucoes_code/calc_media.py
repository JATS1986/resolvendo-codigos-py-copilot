# Recebendo dois dados diferentes do usuário e concatena-los em uma única string

# Resolução segundo o Gemini 

def calcular_media():
  """Calcula a média de três notas."""

  # Obtendo as notas do usuário
  nota1 = float(input("Digite a primeira nota: "))
  nota2 = float(input("Digite a segunda nota: "))
  nota3 = float(input("Digite a terceira nota: "))

  # Calculando a média
  media = (nota1 + nota2 + nota3) / 3

  # Imprimindo o resultado
  print("A média das notas é:", media)

# Chamando a função
calcular_media()