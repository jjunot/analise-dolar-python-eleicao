# 📊 Monitor Estratégico USD/BRL

Dashboard interativo desenvolvido em Python para análise de performance histórica do par de moedas Dólar/Real (USD/BRL) com dados em tempo real.

## 🚀 Funcionalidades
- **Navegação Histórica:** Análise de dados desde 2010 via integração com Yahoo Finance.
- **Gráfico de Contexto:** Visualização do histórico total com destaque em azul escuro para o período selecionado.
- **Métricas Dinâmicas:** Cálculo automático de Preço Inicial, Final e Variação Percentual baseado nas datas escolhidas.
- **Alertas de Volatilidade:** Tabela anual com sinalização visual (Verde para altas >10% e Vermelho para quedas >10%).
- **Atualização On-demand:** Botão integrado para limpar cache e buscar cotações do dia.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Streamlit**: Interface do Dashboard.
- **Plotly**: Gráficos interativos.
- **Pandas**: Manipulação e análise de dados.
- **YFinance**: Extração de dados financeiros.

## 💻 Como Rodar o Projeto
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt