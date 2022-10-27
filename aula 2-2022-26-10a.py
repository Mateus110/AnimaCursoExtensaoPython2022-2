# comando input(): quero permitir que 
# o usuário digite algo...
nome = input("Digite seu nome: ")
#exibir o nome
print(f"Boa noite {nome}, seja bem vindo!")
#exibir idade
idade = int(input("digite sua idade: "))
#colocar o int para ele mudar para numero
#e se eu quisesse mostrar o dobro da idade...
dobro = idade * 2
print(f"o dobro da sua idade é {dobro}")

#estrutura condicional- famoso "Se" (if)
#Se a pessoa for maior de idade, mostre "você é maior de idade, ótimo! Ja pode beber ou dirigir."
if idade >= 18:
  print("Você é maior de idade, ótimo! já pode beber ou dirigir.")
else:
  print("você é jovem ainda!")
#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("informe seu genero? M=masculino ou F=feminino: ")
if idade >= 18 and genero == "M" or "masculino" or "Masculino":
  print("...E você precisa ou precisou prestar serviço militar obrigatório!")