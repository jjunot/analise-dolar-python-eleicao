import yfinance as yf
import pandas as pd

# 1. Configurações
ticker = "USDBRL=X"
data_inicio = "2010-01-01"
data_fim = "2026-04-07"

# 2. Download dos dados
print("Descarregando dados históricos desde 2010...")
df = yf.download(ticker, start=data_inicio, end=data_fim)

# 3. Cálculo de Valorização (Ajustado com .item() para evitar o erro de Series)
preco_inicial = df['Close'].iloc[0].item()
preco_atual = df['Close'].iloc[-1].item()

valorizacao_total = ((preco_atual - preco_inicial) / preco_inicial) * 100

# 4. Cálculo da Média Anual (CAGR)
num_anos = 2026 - 2010 + (97/365) 
valorizacao_media_anual = (((preco_atual / preco_inicial) ** (1/num_anos)) - 1) * 100

print("\n" + "="*40)
print(f"RESUMO DA VALORIZAÇÃO (2010 - 2026)")
print("="*40)
print(f"Preço em Jan/2010: R$ {preco_inicial:.2f}")
print(f"Preço em Abr/2026: R$ {preco_atual:.2f}")
print("-" * 40)
print(f"Valorização Total no Período: {valorizacao_total:.2f}%")
print(f"Valorização Média Anual: {valorizacao_media_anual:.2f}% ao ano")
print("="*40)

# 5. Ver a valorização nos últimos 5 anos
df_anual = df['Close'].resample('YE').last().pct_change() * 100
print("\nValorização por ano (últimos 5 anos):")
print(df_anual.tail(5))