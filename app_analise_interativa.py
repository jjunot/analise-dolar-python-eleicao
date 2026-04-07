import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# 1. Configuração da Página e Estilos
st.set_page_config(page_title="USD/BRL Pro", layout="wide", initial_sidebar_state="collapsed")

# CSS para layout, botão e remover margens
st.markdown("""
    <style>
        .block-container {padding-top: 1rem; padding-bottom: 0rem;}
        .stButton button {float: right; margin-top: 25px;}
        [data-testid="stMetricValue"] {font-size: 1.6rem !important;}
        section[data-testid="stSidebar"] {display: none;}
    </style>
    """, unsafe_allow_html=True)

# 2. Função de Busca de Dados
@st.cache_data(ttl=3600)
def load_data():
    try:
        data = yf.download("USDBRL=X", start="2010-01-01", end=datetime.now().strftime('%Y-%m-%d'))
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        df = data.reset_index()
        return df
    except Exception:
        return pd.DataFrame()

# 3. Lógica de Cores da Tabela
def colorir_variacao(val):
    if val > 10:
        return 'background-color: rgba(0, 255, 0, 0.3); color: black;' # Verde
    elif val < -10:
        return 'background-color: rgba(255, 0, 0, 0.3); color: black;' # Vermelho
    return ''

df = load_data()

if not df.empty:
    # --- CABEÇALHO ---
    col_t, col_b = st.columns([0.7, 0.3])
    with col_t:
        st.title("📊 Monitor Estratégico USD/BRL")
    with col_b:
        if st.button("🔄 Atualizar Cotações", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

    st.markdown("---")

    # --- CONTROLES SINCRONIZADOS ---
    d_min = df['Date'].min().to_pydatetime()
    d_max = df['Date'].max().to_pydatetime()

    c_slider, c_inputs = st.columns([2, 1])
    
    with c_slider:
        start_date, end_date = st.slider(
            "Selecione o período de análise:",
            min_value=d_min,
            max_value=d_max,
            value=(d_min, d_max),
            format="DD/MM/YYYY"
        )

    with c_inputs:
        col_d1, col_d2 = st.columns(2)
        d1 = col_d1.date_input("Início", start_date, min_value=d_min, max_value=d_max)
        d2 = col_d2.date_input("Fim", end_date, min_value=d_min, max_value=d_max)

    # Filtragem Baseada na Seleção
    df_sel = df[(df['Date'] >= pd.Timestamp(d1)) & (df['Date'] <= pd.Timestamp(d2))]

    # --- MÉTRICAS ---
    if not df_sel.empty:
        p_i = float(df_sel['Close'].iloc[0])
        p_f = float(df_sel['Close'].iloc[-1])
        var = ((p_f - p_i) / p_i) * 100
        
        st.latex(r"\text{Variação } \% = \left( \frac{P_{final} - P_{inicial}}{P_{inicial}} \right) \times 100")

        m1, m2, m3 = st.columns(3)
        m1.metric(f"Preço em {d1.strftime('%d/%m/%y')}", f"R$ {p_i:.2f}")
        m2.metric(f"Preço em {d2.strftime('%d/%m/%y')}", f"R$ {p_f:.2f}")
        m3.metric("Variação Selecionada", f"{var:+.2f}%", delta=f"{var:.2f}%")

        st.markdown("---")

        # --- LAYOUT PRINCIPAL: GRÁFICO E TABELA ---
        g_col, t_col = st.columns([2.2, 1])

        with g_col:
            st.write("**Gráfico Histórico com Destaque Selecionado**")
            fig = go.Figure()
            
            # 1. CAMADA DE FUNDO: Histórico Inteiro (Cinza Claro)
            fig.add_trace(go.Scatter(
                x=df['Date'], 
                y=df['Close'], 
                mode='lines', 
                line=dict(color='rgba(0,0,0,0.15)', width=1.5), 
                name="Histórico Total",
                hoverinfo='skip' # Ignora o hover para não poluir
            ))
            
            # 2. CAMADA DE DESTAQUE: Período Selecionado (Azul)
            fig.add_trace(go.Scatter(
                x=df_sel['Date'], 
                y=df_sel['Close'], 
                mode='lines', 
                fill='tozeroy',
                fillcolor='rgba(31, 119, 180, 0.1)', # Sombra leve azul
                line=dict(color='#1f77b4', width=3.5), 
                name="Período Selecionado"
            ))

            fig.update_layout(
                template="plotly_white", # Fundo branco para números pretos
                height=550,
                margin=dict(l=0, r=0, t=10, b=0),
                showlegend=False,
                xaxis=dict(
                    type="date", 
                    # MANTÉM O GRÁFICO INTEIRO (Fixa o eixo X no histórico total)
                    range=[df['Date'].min(), df['Date'].max()], 
                    tickfont=dict(size=12, color='black'),
                ),
                yaxis=dict(
                    side="right", 
                    tickfont=dict(size=12, color='black'),
                    gridcolor="rgba(0,0,0,0.05)"
                )
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        with t_col:
            st.write("**Fechamento Anual**")
            df_anual = df.copy()
            df_anual['Ano'] = df_anual['Date'].dt.year
            f_anual = df_anual.groupby('Ano')['Close'].last()
            v_anual = f_anual.pct_change() * 100
            
            tab_final = pd.DataFrame({
                'Ano': f_anual.index, 
                'R$': f_anual.values, 
                'Var %': v_anual.values
            }).sort_values(by='Ano', ascending=False)
            
            st.dataframe(
                tab_final.style.format({'R$': '{:.2f}', 'Var %': '{:+.2f}%'}).map(colorir_variacao, subset=['Var %']),
                use_container_width=True, height=525
            )
else:
    st.error("Erro ao carregar os dados.")