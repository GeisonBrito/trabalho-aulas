print("**********************************")
print("*********NOTAS ESCOLARES**********")
print("**********************************")
Nome = input("Digite seu nome: ")
print("Olá", Nome)
print("Vamo começar!")

nota1 = float(input('Nota primeiro trimestre: '))
if(nota1 < 0 or nota1 > 10):
    print("use apenas números de 0 a 10")

nota2 = float(input('Segunda trimestre: '))
nota3 = float(input('Terceiro trimestre: '))
nota4 = float(input('Quarto trimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('Media: ', media)

if(media >= 7):
    print("Aprovado")

else:
    media <= 6.9
    print  ("Reprovado")

