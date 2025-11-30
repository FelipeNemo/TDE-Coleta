#home

# Nomenclaturas ou conceitos desconhecidos ao leitor, dispõe-se os conceitos necessários abaixo: 

# ●  Deputado Federal: Parlamentar eleito para atuar no Congresso Nacional, responsável por criar e 
# votar leis de abrangência nacional. 
# ●  Sessão Deliberativa: Reunião oficial da Câmara dos Deputados onde são debatidas e votadas 
# propostas legislativas. 
# ●  Presença em Sessão: Registro de que o deputado participou de uma sessão deliberativa. 
# ●  Falta Justificada: Ausência em uma sessão ou votação registrada oficialmente, com justificativa 
# aceita (ex.: licença por interesse particular ou missão oficial). 
# ●  Missão Oficial: Atividade relacionada ao mandato do deputado, como viagens nacionais ou 
# internacionais, participação em comissões ou eventos representando o país. 
# ●  Licença por Interesse Particular: Direito do deputado de se ausentar de sessões e votações por 
# motivos pessoais, sem perda de remuneração. 
# ●  Ganho por Dia Trabalhado: Indicador calculado dividindo-se a remuneração total bruta do deputado 
#pelo número de presenças em sessões deliberativas. 
# ●  Ganho por Votação Participada: Indicador calculado dividindo-se a remuneração total bruta do 
# deputado pelo número de votações participadas. 
# ●  CLT: Consolidação das Leis de Trabalho, conjunto de normas que rege os direitos e deveres de 
# trabalhadores formais no Brasil. 

# Objetivos de mineração e critérios de sucesso 
#  A mineração de dados para este projeto tem como objetivo extrair, organizar e analisar informações 
# sobre presenças, participações em votações e faltas de deputados federais a partir de dados oficiais 
# disponibilizados pela Câmara dos Deputados. As análises visam: 

# 1.  Calcular a presença de cada deputado; 
# 2.  Calcular a taxa de votações participadas por cada deputado; 
# 3.  Aplicar filtros baseados no regime CLT para simular limites de faltas e jornadas de trabalho; 
# 4.  Calcular o ganho efetivo por dia trabalhado e por votação participada por cada deputado; 
# 5.  Identificar padrões e evidências de desigualdade entre agentes políticos e agentes civis. 

# Para que haja sucesso na mineração dos dados, estabelecem-se os critérios: 
# ●  Dados corretamente coletados, tratados e organizados de forma consistente; 
# ●  Métricas calculadas de maneira precisa e reproduzível; 
# ●  Resultados que permitam comparar quantitativamente o desempenho dos deputados com 
#parâmetros da CLT; 
# ●  Visualizações e relatórios claros, que evidenciem as conclusões desejadas e permitam confirmar ou 
#efutar as hipóteses iniciais. 

# Avaliação inicial de técnicas e ferramentas  
# Serão majoritariamente utilizados recursos computacionais para coleta, filtragem, tratamento 
# visualizações dos dados necessários para a realização da pesquisa, são eles, de forma geral: 

import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="LegisCheck",
    layout="wide",
    initial_sidebar_state="collapsed",  # sidebar começa escondida
)

st.title("LegisCheck")
st.write("Comparativo de presença, votações, faltas e padrões de jornada dos parlamentares")

# ============================
# DADOS REAIS:
df_dep_presenca = pd.read_csv("data/graphs/df_dep_presenca.csv")
df_dep_votacao = pd.read_csv("data/graphs/df_dep_votacao.csv")
df_dep_injustificado = pd.read_csv("data/graphs/df_dep_injustificado.csv")
df_dep = pd.read_csv("data/graphs/df_dep_ganhos.csv")
# ============================


# Trabalhadores CLT (fictícios)
data_civ = {
    "ganho_por_dia_trabalhado": [
        90, 110, 100, 95, 120, 80, 130, 105, 115, 98,
        85, 125, 140, 92, 102,
    ],
    "grupo": ["Trabalhador CLT"] * 15,
}
df_civ = pd.DataFrame(data_civ)

df_dep_gain = pd.DataFrame(
    {
        "ganho_por_dia_trabalhado": df_dep["ganho_por_dia_trabalhado"],
        "grupo": "Deputado Federal",
    }
)

df_violin = pd.concat([df_dep_gain, df_civ], ignore_index=True)

# ============================
# SIDEBAR – APENAS TAXA DE PRESENÇA
# ============================
with st.sidebar:
    st.markdown("### Filtro de presença")

    faixa_presenca_pct = st.slider(
        "Faixa de presença (%)",
        min_value=0,
        max_value=100,
        value=(0, 100),
        help="Filtra deputados pela taxa de presença em sessões deliberativas.",
    )

# converter de % para fração 0–1
min_frac = faixa_presenca_pct[0] / 100
max_frac = faixa_presenca_pct[1] / 100

# aplicar filtro
df_filtrado = df_dep_presenca[
    (df_dep_presenca["taxa_presenca"] >= min_frac)
    & (df_dep_presenca["taxa_presenca"] <= max_frac)
].copy()


# ============================
# PALETA DE CORES
# ============================
# Laranja principal (deputados), amarelo/âmbar (CLT/limites),
# ciano/teal (grupo CLT), e um laranja mais claro para contraste.
palette_main = "#ff7f0e"      # laranja principal
palette_amber = "#f2c94c"     # amarelo/âmbar (destaques, CLT)
palette_teal = "#00b894"      # teal (Trabalhador CLT)
palette_light_orange = "#f2994a"

# ======================================================================
# Presença por Deputado
# ======================================================================

df_plot1 = df_dep_presenca.sort_values("taxa_presenca", ascending=True)
df_plot1 = df_filtrado.sort_values("taxa_presenca", ascending=True)

fig1 = px.bar(
    df_plot1,
    x="taxa_presenca",          # fração 0–1
    y="deputado",
    orientation="h",
    labels={
        "taxa_presenca": "Taxa de presença",
        "deputado": "Deputado",
    },
    title="Presença por Deputado",
    color_discrete_sequence=[palette_main],
)

fig1.update_xaxes(
    range=[0, 1],
    tick0=0,
    dtick=0.1,
    tickformat=".0%",  # 0.85 → 85%
)


# ======================================================================
# Sessões por Votações Participada
# ======================================================================
fig2 = px.scatter(
    df_dep_votacao,
    x="presencas",
    y="taxa_votacao",
    size="presencas",
    hover_name="deputado",
    color="deputado",
    color_discrete_sequence=[palette_main, palette_light_orange],
    labels={
        "presencas": "Número de sessões comparecidas",
        "taxa_votacao": "Taxa de votações participadas",
        "presencas": "Presenças",
        "deputado": "Deputado",
    },
    title="Sessões por Votações Participada",
)
fig2.update_layout(yaxis_tickformat=".0%")

# ======================================================================
# Faltas injustificadas vs limite CLT
# ======================================================================
limite_faltas_clt = 5  # mantém aqui

df_plot3 = df_dep_injustificado.sort_values("faltas_injustificadas", ascending=False)

fig3 = px.bar(
    df_plot3,
    x="deputado",
    y="faltas_injustificadas",
    labels={
        "faltas_injustificadas": "Faltas injustificadas",
        "deputado": "Deputado",
    },
    title="Faltas Injustificadas vs Limite CLT",
    color_discrete_sequence=[palette_main],
)

fig3.add_hline(
    y=limite_faltas_clt,
    line_dash="dash",
    line_width=3,
    line_color=palette_amber,
    annotation_text=f"Limite CLT = {limite_faltas_clt}",
    annotation_position="top right",
)


# ======================================================================
# Ganho por dia e por votação
# ======================================================================
df_long = pd.melt(
    df_dep,
    id_vars=["deputado"],
    value_vars=["ganho_por_dia_trabalhado", "ganho_por_votacao_participada"],
    var_name="tipo_ganho",
    value_name="valor",
)
df_long["tipo_ganho"] = df_long["tipo_ganho"].map(
    {
        "ganho_por_dia_trabalhado": "Ganho por dia trabalhado",
        "ganho_por_votacao_participada": "Ganho por votação participada",
    }
)
fig4 = px.box(
    df_long,
    x="tipo_ganho",
    y="valor",
    color="tipo_ganho",
    color_discrete_sequence=[palette_main, palette_light_orange],
    points="outliers",
    labels={"tipo_ganho": "Tipo de ganho", "valor": "R$"},
    title="Ganho por Dia Trabalhado e por Votação",
)

# ======================================================================
# Desigualdade: Deputados x CLT
# ======================================================================
fig5 = px.violin(
    df_violin,
    x="grupo",
    y="ganho_por_dia_trabalhado",
    box=True,
    points="outliers",
    color="grupo",
    color_discrete_sequence=[palette_main, palette_teal],
    labels={
        "grupo": "Grupo",
        "ganho_por_dia_trabalhado": "Ganho por dia trabalhado (R$)",
    },
    title="Ganho por Dia Trabalhado: Deputados x Trabalhadores CLT",
)

# ======================================================================
# Ganho por dia e por votação
# ======================================================================
df_long = pd.melt(
    df_dep,
    id_vars=["deputado"],
    value_vars=["ganho_por_dia_trabalhado", "ganho_por_votacao_participada"],
    var_name="tipo_ganho",
    value_name="valor",
)
df_long["tipo_ganho"] = df_long["tipo_ganho"].map(
    {
        "ganho_por_dia_trabalhado": "Ganho por dia trabalhado",
        "ganho_por_votacao_participada": "Ganho por votação participada",
    }
)
fig4 = px.box(
    df_long,
    x="tipo_ganho",
    y="valor",
    color="tipo_ganho",
    color_discrete_sequence=[palette_main, palette_light_orange],
    points="outliers",
    labels={"tipo_ganho": "Tipo de ganho", "valor": "R$"},
    title="Ganho por Dia Trabalhado e por Votação",
)

# 👉 aqui:
fig4.update_yaxes(type="log")

# ======================================================================
# Desigualdade: Deputados x CLT
# ======================================================================
fig5 = px.violin(
    df_violin,
    x="grupo",
    y="ganho_por_dia_trabalhado",
    box=True,
    points="outliers",
    color="grupo",
    color_discrete_sequence=[palette_main, palette_teal],
    labels={
        "grupo": "Grupo",
        "ganho_por_dia_trabalhado": "Ganho por dia trabalhado (R$)",
    },
    title="Ganho por Dia Trabalhado: Deputados x Trabalhadores CLT",
)

# 👉 e aqui também, se quiser:
fig5.update_yaxes(type="log")

# ======================================================================
# LAYOUT: 3 GRÁFICOS ACIMA, 2 ABAIXO
# ======================================================================

col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
with col3:
    st.plotly_chart(fig3, use_container_width=True)

col4, col5 = st.columns(2)
with col4:
    st.plotly_chart(fig4, use_container_width=True)
with col5:
    st.plotly_chart(fig5, use_container_width=True)
