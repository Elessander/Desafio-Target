import json

with open('dados.json', 'r') as file:
    faturamento = json.load(file)

valores = [d['valor'] for d in faturamento if d['valor'] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_media = len([v for v in valores if v > media_mensal])

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media} Dias")
