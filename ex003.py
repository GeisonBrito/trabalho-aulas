notas = []
continuar = True

while continuar == True:
    nota = float(input("Digite a nota:"))  

    notas.append(nota)
    opcion=input("Voce Deseja colocar outra nota (S/N)")

    if opcion == 'n':
        continuar = False
        operacao = sum(notas) / len(notas)
        print(operacao)
