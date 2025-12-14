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

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # pasta do home.py
ROOT_DIR = BASE_DIR.parent                  # volta pra /app (seu projeto usa app/home.py)
DATA_DIR = ROOT_DIR / "data" / "graphs"

@st.cache_data(show_spinner=False)
def load_csvs():
    paths = {
        "df_dep_presenca": DATA_DIR / "df_dep_presenca.csv",
        "df_dep_votacao": DATA_DIR / "df_dep_votacao.csv",
        "df_dep_injustificado": DATA_DIR / "df_dep_injustificado.csv",
        "df_dep": DATA_DIR / "df_dep_ganhos.csv",
    }

    missing = [name for name, p in paths.items() if not p.exists()]
    if missing:
        # mostra exatamente o que faltou no deploy
        raise FileNotFoundError(
            "Arquivos CSV não encontrados no deploy:\n"
            + "\n".join([f"- {k}: {paths[k]}" for k in missing])
        )

    return (
        pd.read_csv(paths["df_dep_presenca"]),
        pd.read_csv(paths["df_dep_votacao"]),
        pd.read_csv(paths["df_dep_injustificado"]),
        pd.read_csv(paths["df_dep"]),
    )


st.set_page_config(
    page_title="LegisCheck",
    layout="wide",
    initial_sidebar_state="collapsed",  # sidebar começa escondida
)

st.title("LegisCheck")
st.write("Comparativo de presença, votações, faltas e padrões de jornada dos parlamentares")

# ============================
# DADOS REAIS:
with st.spinner("Carregando dados..."):
    try:
        df_dep_presenca, df_dep_votacao, df_dep_injustificado, df_dep = load_csvs()
    except Exception as e:
        st.error("Falha ao carregar os dados do app.")
        st.exception(e)
        st.stop()


# ============================
# SIDEBAR – FILTROS + PARÂMETROS CLT
# ============================
with st.sidebar:
    st.markdown("### Deputados")

    # --- filtro por nome de deputado ---
    opcoes_deps = sorted(df_dep["deputado"].dropna().unique().tolist())
    deps_selecionados = st.multiselect(
        "Deputados",
        options=opcoes_deps,
        default=None,
        help="Selecione um ou mais deputados para focar a análise.",
    )
    
    # --- filtro por id_deputado (opcional) ---
    opcoes_ids = sorted(df_dep["id_deputado"].dropna().unique().tolist())
    ids_selecionados = st.multiselect(
        "Filtrar por id_deputado (opcional)",
        options=opcoes_ids,
        default=[],
        help="Selecione um ou mais ids específicos de deputados, se desejar.",
    )

    # --- filtro por partido ---
    if "siglaPartido" in df_dep_presenca.columns:
        opcoes_partidos = sorted(df_dep_presenca["siglaPartido"].dropna().unique().tolist())
    else:
        opcoes_partidos = []
    partidos_selecionados = st.multiselect(
        "Partidos",
        options=opcoes_partidos,
        default=None,
        help="Filtra deputados pelos partidos selecionados.",
    )

    # --- faixa de presença (já existia) ---
    faixa_presenca_pct = st.slider(
        "Faixa de presença (%)",
        min_value=0,
        max_value=100,
        value=(0, 100),
        help="Mantém apenas deputados dentro dessa faixa de taxa de presença.",
    )

    st.markdown("---")
    st.markdown("### Parâmetros de referência(CLT)")

    # limite de faltas CLT (usado no gráfico 3)
    limite_faltas_clt = st.number_input(
        "Limite de faltas injustificadas (CLT simulada)",
        min_value=0,
        max_value=30,
        value=5,
        step=1,
        help="Usado como linha de referência no gráfico de faltas injustificadas.",
    )

    # ganho diário CLT (usado para gerar/interpretar df_civ)
    ganho_clt_referencia = st.number_input(
        "Ganho diário CLT (R$)",
        min_value=0,
        max_value=1000,
        value=100,
        step=10,
        help="Valor de referência para o ganho diário de um trabalhador CLT.",
    )

    # remuneração de referência do deputado (para reescalar ganhos)
    remuneracao_ref = st.number_input(
        "Remuneração bruta mensal do deputado (referência, R$)",
        min_value=10000,
        max_value=100000,
        value=46000,
        step=1000,
        help="Usada para calcular ganho por dia trabalhado e por votação participada.",
    )
    
# ============================
# APLICAÇÃO DOS FILTROS GERAIS
# ============================

# 1) ponto de partida: df_dep (ganhos) como universo de deputados
df_dep_base = df_dep.merge(
    df_dep_presenca[["id_deputado", "taxa_presenca", "siglaPartido"]],
    on="id_deputado",
    how="left",
)

# 2) faixa de presença
min_frac = faixa_presenca_pct[0] / 100
max_frac = faixa_presenca_pct[1] / 100
mask = (df_dep_base["taxa_presenca"] >= min_frac) & (df_dep_base["taxa_presenca"] <= max_frac)

# 3) filtro por deputado (se houver seleção)
if deps_selecionados:
    mask &= df_dep_base["deputado"].isin(deps_selecionados)

# 4) filtro por partido (se houver seleção)
if partidos_selecionados:
    mask &= df_dep_base["siglaPartido"].isin(partidos_selecionados)


# 5) filtro por id_deputado (se houver seleção)
if ids_selecionados:
    mask &= df_dep_base["id_deputado"].isin(ids_selecionados)

# ids finais
ids_filtrados = df_dep_base.loc[mask, "id_deputado"].unique()

# 6) aplica aos demais dataframes
df_dep_presenca = df_dep_presenca[df_dep_presenca["id_deputado"].isin(ids_filtrados)]
df_dep_votacao = df_dep_votacao[df_dep_votacao["id_deputado"].isin(ids_filtrados)]
df_dep_injustificado = df_dep_injustificado[df_dep_injustificado["id_deputado"].isin(ids_filtrados)]
df_dep = df_dep[df_dep["id_deputado"].isin(ids_filtrados)]

# 7) reescalar ganhos pela remuneração de referência (se quiser)
FATOR_REMUNERACAO = remuneracao_ref / 46000  # assume que df_dep_ganhos foi gerado com 46k
df_dep["ganho_por_dia_trabalhado"] *= FATOR_REMUNERACAO
df_dep["ganho_por_votacao_participada"] *= FATOR_REMUNERACAO

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
# PALETA DE CORES
# ============================
# Laranja principal (deputados), amarelo/âmbar (CLT/limites),
# ciano/teal (grupo CLT), e um laranja mais claro para contraste.
palette_main = "#ff7f0e"      # laranja principal
palette_amber = "#00b894"     # amarelo/âmbar (destaques, CLT)
palette_teal = "#00b894"      # teal (Trabalhador CLT)
palette_light_orange = "#f2c54a"

# ======================================================================
# Presença por Deputado
# ======================================================================

df_plot1 = df_dep_presenca.sort_values("taxa_presenca", ascending=True)

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
        "ganho_por_dia_trabalhado": "Dia trabalhado",
        "ganho_por_votacao_participada": "Votação participada",
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
fig4.update_xaxes(tickangle=0)
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
        "ganho_por_votacao_participada": "Votação participada",
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
        "ganho_por_dia_trabalhado": "Dia trabalhado (R$)",
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
