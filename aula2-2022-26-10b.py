#pede o nome do aluno e sua nota de 0 a 10
#E se ele tirou nota 10 mostra "você é o bixão mesmo em!!!"
nome = input("digite seu nome: ")
nota = float(input("Qual sua nota da prova: "))
if nota == 10:
  print(f"{nome}, Você é o bixão mesmo em!!!")
elif (nota >= 6 and nota < 10):
  print(f"Bom trabalho {nome}, mas precisa estudar mais!")
else:
  print("Burro dms ave maria!!!")