n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:
    print("""      [1]Somar
      [2]Multiplicar
      [3]Maior
      [4]Novos Números
      [5]Sair do Programa""")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"A soma entre {n1} e {n2} é {n1 + n2}")
    elif opcao == 2:
        print(f"A multiplicação entre {n1} e {n2} é {n1 * n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior número é {n1}")
        elif n2 > n1:
            print(f"O maior número é {n2}")
        else:
            print("Os dois números são iguais.")
    elif opcao == 4:
        print("Digite novos números:")
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
    elif opcao == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida! Tente novamente.")

print("Programa finalizado. Volte sempre!")