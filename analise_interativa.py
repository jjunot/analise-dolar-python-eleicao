import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Busca de Dados
ticker = "USDBRL=X"
df = yf.download(ticker, start="2010-01-01", end="2026-04-07")
df = df.reset_index()

# 2. Criar Gráfico Interativo com Subplots
# Vamos criar um gráfico de preço e um de variação percentual
fig = make_subplots(rows=2, cols=1, 
                    shared_xaxes=True, 
                    vertical_spacing=0.1,
                    subplot_titles=("Preço Histórico (USD/BRL)", "Variação Diária (%)"))

# Adicionar a linha de Preço
fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], 
                         name="Preço de Fechamento",
                         line=dict(color='blue')), row=1, col=1)

# Adicionar a Variação Percentual
df['Variacao'] = df['Close'].pct_change() * 100
fig.add_trace(go.Bar(x=df['Date'], y=df['Variacao'], 
                     name="Variação Diária",
                     marker=dict(color='orange')), row=2, col=1)

# 3. Adicionar Janela de Observação (Range Slider)
fig.update_layout(
    title="Análise Dinâmica Dólar: 2010 - 2026",
    template="plotly_white",
    height=800,
    showlegend=False,
    xaxis_rangeslider_visible=True, # Aqui cria a janela móvel
    xaxis_rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=5, label="5y", step="year", stepmode="backward"),
            dict(step="all", label="Tudo")
        ])
    )
)

# 4. Salvar como HTML (Ideal para o Render)
fig.write_html("analise_interativa.html")

# 5. Abrir no Navegador
print("Gráfico interativo gerado! Abrindo no seu navegador...")
fig.show()