#solução linear Fibonacci
#ex sequencia fibonacci: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21...
n = int(input())

if n < 0:
    print("Entrada Inválida")
elif n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    termo1 = 0
    termo2 = 1
    cont = 2

    while cont <= n:
        termo3 = termo1 + termo2
        termo1 = termo2
        termo2 = termo3
        cont = cont + 1

    print(termo2)


