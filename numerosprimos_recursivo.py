def ehprimo(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def p(n):
    if n == 2: #ponto de parada
        return [2]
    
    primos = p(n-1)
    if ehprimo(n):
            primos.append(n)
    return primos

n = int(input())
primos = p(n)
print(f"p({n}) = {primos}", end="")


