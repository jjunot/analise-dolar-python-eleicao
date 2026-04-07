import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configurações Iniciais
ticker = "USDBRL=X"
anos_eleitorais = [2014, 2018, 2022, 2026]

def carregar_dados_eleicao(ano):
    """
    Busca os dados do Yahoo Finance e normaliza os dias para comparação.
    """
    # Define o fim da busca: se for o ano atual, vai até hoje. Se for passado, vai até o fim do ano.
    fim = f"{ano}-12-31" if ano < 2026 else "2026-04-07"
    
    # Download dos dados
    df = yf.download(ticker, start=f"{ano}-01-01", end=fim)
    
    # Tratamento de dados com Pandas
    df = df.reset_index()
    # Criamos a coluna 'Dias_do_Ano' para que o eixo X seja igual para todos os anos (0 a 365)
    df['Dias_do_Ano'] = (df['Date'] - df['Date'].min()).dt.days
    return df

# 2. Criação do Gráfico
plt.figure(figsize=(12, 7))

for ano in anos_eleitorais:
    print(f"Buscando dados de {ano}...")
    dados = carregar_dados_eleicao(ano)
    
    # Plotagem
    plt.plot(dados['Dias_do_Ano'], dados['Close'], label=f"Eleições {ano}", linewidth=2)

# 3. Estilização e Linhas de Referência
plt.title("Comparativo do Dólar (USD/BRL) em Anos de Eleição Presidencial", fontsize=14)
plt.xlabel("Dias decorridos desde o início do ano", fontsize=12)
plt.ylabel("Preço de Fechamento (R$)", fontsize=12)

# Marcar o período aproximado das eleições (Outubro)
plt.axvspan(273, 303, color='gray', alpha=0.1, label='Período Eleitoral (Out)')

# Marcar o dia de hoje no gráfico de 2026 (Abril)
plt.axvline(x=97, color='red', linestyle='--', alpha=0.7, label='Ponto Atual (Abril/2026)')

plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# 4. Salvamento e Exibição
# Salva a imagem antes de mostrar (importante para o seu GitHub)
plt.savefig("grafico_dolar.png", dpi=300)
print("\n" + "="*30)
print("Sucesso! O arquivo 'grafico_dolar.png' foi gerado.")
print("Pressione X na janela do gráfico para encerrar o script.")
print("="*30)

plt.show()