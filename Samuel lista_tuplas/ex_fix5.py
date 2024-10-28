lista = []
while True:
    numero_usuario = int(input("Digite um numero: "))
    lista.append(numero_usuario)
    tamanho = len(lista)
    print(numero_usuario)
    if tamanho == 5:
        break
print(lista)