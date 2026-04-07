# 📊 Monitor Estratégico USD/BRL (Pro)

Este projeto é um Dashboard interativo desenvolvido em Python para análise estratégica da performance histórica do par de moedas **Dólar/Real (USD/BRL)**. A ferramenta utiliza dados em tempo real via API do Yahoo Finance para auxiliar na tomada de decisão financeira e gestão de patrimônio internacional.

## 🌐 Acesso Online
A aplicação está em produção e pode ser acessada através do link abaixo:
**🔗 [Monitor Dólar - Live Demo](https://analise-dolar-python-eleicao.onrender.com)**

## 🚀 Funcionalidades
- **Análise Histórica Completa:** Acesso a dados desde 2010 até o presente.
- **Gráfico Dinâmico com Contexto:** Visualização da série histórica total com destaque (overlay) para o período selecionado, facilitando a análise de ciclos econômicos.
- **Métricas de Performance:** Cálculo instantâneo de Preço de Abertura, Fechamento e Variação Percentual ($\Delta\%$) baseada no intervalo escolhido.
- **Alertas de Volatilidade:** Tabela de fechamento anual com sinalização visual inteligente (Verde para altas >10% e Vermelho para quedas >10%).
- **Interface Otimizada:** Layout limpo com números em alto contraste para máxima legibilidade e foco no dado.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Streamlit**: Framework para criação de interfaces web financeiras.
- **Plotly**: Motor gráfico para visualizações interativas de alta fidelidade.
- **Pandas**: Processamento e manipulação de séries temporais.
- **YFinance**: Extração de dados do mercado financeiro global.

## 💻 Como Rodar o Projeto Localmente
1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt