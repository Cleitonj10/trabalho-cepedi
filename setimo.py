livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40}
]

grupos = {}

for livro in livros:
    ano = livro["ano"]
    if ano not in grupos:
        grupos[ano] = []
    grupos[ano].append(livro["preco"])

for ano in sorted(grupos):
    media = sum(grupos[ano]) / len(grupos[ano])
    print(f"Ano: {ano} → Preço médio: {media:.2f}")
