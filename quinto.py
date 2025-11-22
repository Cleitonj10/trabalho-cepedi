valor = input("Digite um número: ")

try:
    num = float(valor)

    if "." in valor or "," in valor:
        parte_inteira = int(num)
        parte_decimal = num - parte_inteira
        print("Número decimal")
        print("Parte inteira:", parte_inteira)
        print("Parte decimal:", parte_decimal)
    else:
        num_int = int(num)
        print("Número inteiro")
        if num_int % 2 == 0:
            print("É par")
        else:
            print("É ímpar")

except:
    print("Erro: valor digitado não pode ser convertido para número.")
