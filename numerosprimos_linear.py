#numero primo = somente divide 1 e ele mesmo

def ehprimo(n):
    if (n <= 1):
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
primos = []

for k in range(2, n + 1):
    if ehprimo(k):
        primos.append(k)

print(f"p({n}) = {primos}", end="")
