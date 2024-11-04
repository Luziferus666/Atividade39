#Faça um programa que receba a temperatura média  de cada mês do ano e armazene-as em uma lista.  Em seguida, calcule a média anual das temperaturas  e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = [float(input(f"Digite a temperatura média de {meses[i]}: ")) for i in range(12)]
media_anual = sum(temperaturas) / len(temperaturas)
acima_da_media = [(meses[i], temp) for i, temp in enumerate(temperaturas) if temp > media_anual]
print(f"Média anual de temperatura: {media_anual:.2f}°C")
print("Meses com temperaturas acima da média anual:")
for mes, temp in acima_da_media:
    print(f"{mes}: {temp}°C")