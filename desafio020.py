from random import shuffle
a1=input("Digite o nome do primeiro aluno(a): ")
a2=input("Digite o nome do segundo aluno(a): ")
a3=input("Digite o nome do terceiro aluno(a): ")
a4=input("Digite o nome do quarto aluno(a): ")
lista=[a1,a2,a3,a4]
shuffle(lista)
print(f"A ordem da apresentação é: {lista}")
