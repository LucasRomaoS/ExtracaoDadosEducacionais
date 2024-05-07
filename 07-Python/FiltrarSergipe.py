import csv

# Lista para armazenar as linhas filtradas
linhas_filtradas = []

# Abra o arquivo CSV em modo de leitura
with open('ProuniRelatorioDadosAbertos2020.csv', newline='') as csvfile:
    # Crie um leitor CSV
    reader = csv.reader(csvfile)

    # Itere sobre as linhas do arquivo CSV
    for row in reader:
        # Verifique se a linha contém ";SE;"
        if ";SE;" in row[0]:  # Supondo que a sigla do estado está na primeira coluna
            # Se sim, adicione a linha à lista de linhas filtradas
            linhas_filtradas.append(row)

# Abra o arquivo CSV em modo de escrita
with open('ProuniRelatorioDadosAbertos2020.csv', 'w', newline='') as csvfile:
    # Crie um escritor CSV
    writer = csv.writer(csvfile)

    # Escreva as linhas filtradas no novo arquivo CSV
    writer.writerows(linhas_filtradas)


