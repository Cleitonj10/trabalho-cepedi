def produto_escalar(a, b):
    total = 0
    for x, y in zip(a, b):
        total += x * y
    return total

A = [2, 3, 5]
B = [1, 4, 2]

resultado = produto_escalar(A, B)
print("Produto escalar =", resultado)
