qtd = 0
soma = 0
par = 0
imp = 0
maior = None
menor = None
media = None
limite = 5
while True:
    if limite == 0:
        print("_______________________")
        print("limite excedido")
        break
    print("\nTela de inicio")
    print("_______________________")
    print("1. digitar numeros")
    print("2. mostrar resultados")
    print("3. resetar dados")
    print("0. sair")
    print("_______________________")
    try:
        opcao = int(input("escolha uma opcao: "))
        print("_______________________")

    except ValueError:
        print("---escolha uma opcao valida---")
        limite -= 1
        continue
    if opcao == 1:
        while True:
            try:
                numero = int and float(input("digite um numero:"))
            except ValueError:
                print("_______________________")
                print("digite um numero valido")
                print("_______________________")
                limite -= 1
                continue
            if numero == 0:

                break
            else:
                qtd += 1
                soma += numero
            if numero % 2 == 0:
                par += 1
            else:
                imp += 1
            if maior is None or numero > maior:
                maior = numero
            if menor is None or numero < menor:
                menor = numero
        if qtd >  0:
            media = soma/qtd

    elif opcao == 2:
        print("------RESULTADOS------")
        print(f"soma total dos numeros digitados:{soma}")
        if media is None:
            print("media: nenhum numero foi digitado")
        else:
            print(f"media: {media}")

        print(f"total de numeros digitados:{qtd}")
        print(f"total de numeros pares:{par}")
        print(f"total de numeros impares:{imp}")
        print(f"o maior numero e: {maior}")
        print(f"o menor numero e: {menor}")
    elif opcao == 3:
        print("----DADOS RESETADOS COM SUCESSO----")
        qtd = 0
        soma = 0
        par = 0
        imp = 0
        maior = None
        menor = None
        media = None
    elif opcao == 0:
        print("----OBRIGADO POR USAR O PROGRAMA----")
        break
    else:
        print("---escolha uma opcao valida---")
        limite -= 1
