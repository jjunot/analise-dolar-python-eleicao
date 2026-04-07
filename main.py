import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Definir o símbolo do Dólar em relação ao Real
ticker = "USDBRL=X"

# 2. Criar uma função para buscar e organizar os dados de cada ano
def carregar_dados_eleicao(ano):
    # Se for 2026, pegamos até a data de hoje (07/04/2026)
    fim = f"{ano}-12-31" if ano < 2026 else "2026-04-07"
    df = yf.download(ticker, start=f"{ano}-01-01", end=fim)
    
    # Resetar o índice para que a data vire uma coluna e possamos contar os dias
    df = df.reset_index()
    # Criar uma coluna que conta quantos dias se passaram desde 1º de janeiro
    df['Dias_do_Ano'] = (df['Date'] - df['Date'].min()).dt.days
    return df

# 3. Lista dos anos que queremos comparar
anos_eleitorais = [2014, 2018, 2022, 2026]

# 4. Criar o gráfico
plt.figure(figsize=(12, 6))

for ano in anos_eleitorais:
    dados = carregar_dados_eleicao(ano)
    # Plotar: Dias do ano no eixo X e Preço de Fechamento (Close) no eixo Y
    plt.plot(dados['Dias_do_Ano'], dados['Close'], label=f"Ano {ano}")

# 5. Estilização do gráfico
plt.title("Comparativo do Dólar em Anos Eleitorais (2014 - 2026)")
plt.xlabel("Dias decorridos desde o início do ano")
plt.ylabel("Preço do Dólar (R$)")
plt.legend()
plt.grid(True, alpha=0.3)

# Marcar onde estamos hoje em 2026 (aprox. dia 97)
plt.axvline(x=97, color='red', linestyle='--', label='Hoje (Abril)')

print("Gráfico gerado com sucesso! Feche a janela da imagem para encerrar o script.")
plt.show()