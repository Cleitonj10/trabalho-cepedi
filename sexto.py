from collections import Counter

frase = input("Digite uma frase: ")

contagem = Counter(frase)

if len(contagem) < 3:
    print("Menos de 3 caracteres únicos na frase.")
else:
    mais_frequentes = contagem.most_common(3)
    terceiro = mais_frequentes[2]
    print(f"3º caractere mais frequente: '{terceiro[0]}'")
    print(f"Quantidade: {terceiro[1]}")
