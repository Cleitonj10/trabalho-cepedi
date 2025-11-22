dados = [("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]

alunos = {}

for nome, nota in dados:
    if nome not in alunos:
        alunos[nome] = []
    alunos[nome].append(nota)

medias = {nome: sum(notas) / len(notas) for nome, notas in alunos.items()}

ordenado = sorted(medias.items(), key=lambda x: x[1])

print("Alunos em ordem crescente de média:")
for nome, media in ordenado:
    print(f"{nome}: {media:.2f}")
