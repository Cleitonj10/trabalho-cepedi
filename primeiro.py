def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = [2, 3, 4, 5, 8, 11, 15, 17, 20]

primos = [n for n in numeros if eh_primo(n)]
nao_primos = [n for n in numeros if not eh_primo(n)]

print("Números primos:", primos)
print("Números não primos:", nao_primos)
