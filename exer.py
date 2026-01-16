lista = []
cont_par = 0
cont_imp = 0
maior = None
menor = None
limite = 5

#aqui os numero sao lidos


while True:
    if limite == 0:
        print("limite excedido, tente novamente")
        break
    try:
        numero = int(input("digite o numero:"))
    except ValueError:
        print("digite um valor valido por favor")
        limite -= 1
        continue

    if numero == 0:
        print("obrigado por usar o programa")
        break
    else:
        lista.append(numero)
        if numero % 2 == 0:
                cont_par += 1
        else:
            cont_imp += 1
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero





print(f"-------lista dos numeros obtidos: {lista}-------")
print(f"o maior numero e: {maior}")
print(f"o menor numero e: {menor}")
print(f"quantidade de numeros pares: {cont_par}")
print(f"quantidade de numeros impares: {cont_imp}")