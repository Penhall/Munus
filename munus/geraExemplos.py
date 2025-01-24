import csv
import random
from datetime import datetime, timedelta

# Gerar 300 registros de vendas
file_name = 'vendas_300_registros.csv'
columns = ['ID da Venda', 'Data da Venda', 'Produto', 'Quantidade', 'Valor Unitário', 'Valor Total', 'Cliente']

# Lista de produtos e clientes
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
clientes = [f'Cliente {i}' for i in range(1, 21)]  # 20 clientes

def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(columns)  # Escrever cabeçalhos

    for id_venda in range(1, 301):
        produto = random.choice(produtos)
        quantidade = random.randint(1, 10)
        valor_unitario = round(random.uniform(10.0, 100.0), 2)
        valor_total = round(quantidade * valor_unitario, 2)
        cliente = random.choice(clientes)
        data_venda = generate_random_date(start_date, end_date).strftime('%Y-%m-%d')

        writer.writerow([id_venda, data_venda, produto, quantidade, valor_unitario, valor_total, cliente])

print(f"Arquivo '{file_name}' gerado com sucesso com 300 registros de vendas!")