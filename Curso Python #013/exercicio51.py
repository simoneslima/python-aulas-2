#numero que o usuario vai escolher
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
# diferença entre os termos
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:" )
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo)
