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

#├── app
#│   └── home.py
#├── data
#│   ├── info
#│   │   ├── cod_situacao_deputados.json
#│   │   ├── freq_eventos.csv
#│   │   ├── ocupacoes.csv
#│   │   └── remuneracoes.csv
#│   ├── processed
#│   │   ├── deputados.json
#│   │   ├── eventos.csv
#│   │   ├── presencas.csv
#│   │   ├── votacoes_2020-01.csv
#│   │   ├── votacoes_2020-02.csv
#│   │   ├── votacoes_2020-03.csv
#│   │   ├── votacoes_2020-04.csv
#│   │   ├── votacoes_2020-05.csv
#│   │   ├── votacoes_2020-06.csv
#│   │   ├── votacoes_2020-07.csv
#│   │   ├── votacoes_2020-08.csv
#│   │   ├── votacoes_2020-09.csv
#│   │   ├── votacoes_2020-10.csv
#│   │   ├── votacoes_2020-11.csv
#│   │   ├── votacoes_2020-12.csv
#│   │   ├── votacoes_2021-01.csv
#│   │   ├── votacoes_2021-02.csv
#│   │   ├── votacoes_2021-03.csv
#│   │   ├── votacoes_2021-04.csv
#│   │   ├── votacoes_2021-05.csv
#│   │   ├── votacoes_2021-06.csv
#│   │   ├── votacoes_2021-07.csv
#│   │   ├── votacoes_2021-08.csv
#│   │   ├── votacoes_2021-09.csv
#│   │   ├── votacoes_2021-10.csv
#│   │   ├── votacoes_2021-11.csv
#│   │   ├── votacoes_2021-12.csv
#│   │   ├── votacoes_2022-01.csv
#│   │   ├── votacoes_2022-02.csv
#│   │   ├── votacoes_2022-03.csv
#│   │   ├── votacoes_2022-04.csv
#│   │   ├── votacoes_2022-05.csv
#│   │   ├── votacoes_2022-06.csv
#│   │   ├── votacoes_2022-07.csv
#│   │   ├── votacoes_2022-08.csv
#│   │   ├── votacoes_2022-09.csv
#│   │   ├── votacoes_2022-10.csv
#│   │   ├── votacoes_2022-11.csv
#│   │   ├── votacoes_2022-12.csv
#│   │   ├── votacoes_2023-01.csv
#│   │   ├── votacoes_2023-02.csv
#│   │   ├── votacoes_2023-03.csv
#│   │   ├── votacoes_2023-04.csv
#│   │   ├── votacoes_2023-05.csv
#│   │   ├── votacoes_2023-06.csv
#│   │   ├── votacoes_2023-07.csv
#│   │   ├── votacoes_2023-08.csv
#│   │   ├── votacoes_2023-09.csv
#│   │   ├── votacoes_2023-10.csv
#│   │   ├── votacoes_2023-11.csv
#│   │   ├── votacoes_2023-12.csv
#│   │   ├── votacoes_2024-01.csv
#│   │   ├── votacoes_2024-02.csv
#│   │   ├── votacoes_2024-03.csv
#│   │   ├── votacoes_2024-04.csv
#│   │   ├── votacoes_2024-05.csv
#│   │   ├── votacoes_2024-06.csv
#│   │   ├── votacoes_2024-07.csv
#│   │   ├── votacoes_2024-08.csv
#│   │   ├── votacoes_2024-09.csv
#│   │   ├── votacoes_2024-10.csv
#│   │   ├── votacoes_2024-11.csv
#│   │   ├── votacoes_2024-12.csv
#│   │   ├── votacoes_2025-01.csv
#│   │   ├── votacoes_2025-02.csv
#│   │   ├── votacoes_2025-03.csv
#│   │   ├── votacoes_2025-04.csv
#│   │   ├── votacoes_2025-05.csv
#│   │   ├── votacoes_2025-06.csv
#│   │   ├── votacoes_2025-07.csv
#│   │   ├── votacoes_2025-08.csv
#│   │   ├── votacoes_2025-09.csv
#│   │   └── votacoes_2025-10.csv
#│   └── quality
#│       └── descricao_arquivos.csv
#├── docs
#│   ├── relatorios
#│   │   └── Relatório do Projeto Extensionista - Primeira Iteração.pdf
#│   └── sobre
#│       ├── fase1.md
#│       ├── fase2.md
#│       └── fase3.md
#├── lab
#│   ├── 01_coleta_dados.ipynb
#│   ├── 02_descricao_dados.ipynb
#│   ├── 03_analise_exploratoria.ipynb
#│   ├── 04_verificacao_qualidade.ipynb
#│   └── resumo.txt
#├── README.md
#└── requirements.txt
#
#(coleta) nemo@pop-os:~/puc/tde_coleta/TDE-Coleta$ python test.py 
#
#================================================================================
# DEPUTADOS (data/processed/deputados.json)
#================================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 513 entries, 0 to 512
# Data columns (total 9 columns):
 #   Column         Non-Null Count  Dtype 
#---  ------         --------------  ----- 
# 0   id             513 non-null    int64 
# 1   uri            513 non-null    object
# 2   nome           513 non-null    object
# 3   siglaPartido   513 non-null    object
# 4   uriPartido     513 non-null    object
# 5   siglaUf        513 non-null    object
# 6   idLegislatura  513 non-null    int64 
# 7   urlFoto        513 non-null    object
# 8   email          513 non-null    object
# dtypes: int64(2), object(7)
# memory usage: 36.2+ KB
#
#
#================================================================================
# EVENTOS (data/processed/eventos.csv)
#================================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5340 entries, 0 to 5339
# Data columns (total 11 columns):
 #   Column          Non-Null Count  Dtype 
# ---  ------          --------------  ----- 
# 0   id              5340 non-null   int64 
# 1   uri             5340 non-null   object
# 2   dataHoraInicio  5340 non-null   object
# 3   dataHoraFim     4245 non-null   object
# 4   situacao        5340 non-null   object
# 5   descricaoTipo   5340 non-null   object
# 6   descricao       5340 non-null   object
# 7   localExterno    503 non-null    object
# 8   orgaos          5340 non-null   object
# 9   localCamara     5340 non-null   object
# 10  urlRegistro     3414 non-null   object
# dtypes: int64(1), object(10)
# memory usage: 459.0+ KB
#
#      id  ...                                  urlRegistro
# 0  58552  ...  https://www.youtube.com/watch?v=8nCRrBvYb5k
# 1  59129  ...  https://www.youtube.com/watch?v=W6BJtsxBhlY
# 2  59130  ...                                          NaN
# 3  59186  ...  https://www.youtube.com/watch?v=RZ-itW-y6vM
# 4  59216  ...  https://www.youtube.com/watch?v=9409iCdznyc
#
# [5 rows x 11 columns]
#
#
#================================================================================
# PRESENCAS (data/processed/presencas.csv)
#================================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 564081 entries, 0 to 564080
# Data columns (total 4 columns):
 #   Column         Non-Null Count   Dtype  
# ---  ------         --------------   -----  
# 0   id_evento      564081 non-null  int64  
# 1   id_deputado    564081 non-null  int64  
# 2   tipo_presenca  0 non-null       float64
# 3   ano_origem     564081 non-null  int64  
# dtypes: float64(1), int64(3)
# memory usage: 17.2 MB
#
#   id_evento  id_deputado  tipo_presenca  ano_origem
# 0      58552        69871            NaN        2020
# 1      58552        73466            NaN        2020
# 2      58552        73696            NaN        2020
# 3      58552        74057            NaN        2020
# 4      58552        74200            NaN        2020
#
#
#================================================================================
# REMUNERACOES (data/info/remuneracoes.csv)
#================================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 513 entries, 0 to 512
# Data columns (total 4 columns):
 #   Column       Non-Null Count  Dtype 
# ---  ------       --------------  ----- 
# 0   id_deputado  513 non-null    int64 
# 1   cargo        513 non-null    object
# 2   situacao     513 non-null    object
# 3   data_inicio  513 non-null    object
# dtypes: int64(1), object(3)
# memory usage: 16.2+ KB
#
#   id_deputado     cargo   situacao data_inicio
# 0       204379   Titular  Exercício  2023-02-01
# 1       220714   Titular  Exercício  2023-02-01
# 2       221328  Suplente  Exercício  2024-03-21
# 3       204560   Titular  Exercício  2023-02-01
# 4       204528   Titular  Exercício  2023-02-01
#
#================================================================================
# VOTACOES (data/processed/votacoes_2020-01.csv)
#================================================================================
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 11 columns):
 #   Column               Non-Null Count  Dtype  
# ---  ------               --------------  -----  
# 0   id                   100 non-null    object 
# 1   uri                  100 non-null    object 
# 2   data                 100 non-null    object 
# 3   dataHoraRegistro     100 non-null    object 
# 4   siglaOrgao           100 non-null    object 
# 5   uriOrgao             100 non-null    object 
# 6   uriEvento            98 non-null     object 
# 7   proposicaoObjeto     75 non-null     object 
# 8   uriProposicaoObjeto  75 non-null     object 
# 9   descricao            100 non-null    object 
# 10  aprovacao            94 non-null     float64
# dtypes: float64(1), object(10)
# memory usage: 8.7+ KB

#          id  ... aprovacao
# 0  2229565-3  ...       1.0
# 1  2236329-2  ...       1.0
# 2  2236478-5  ...       1.0
# 3  2236481-5  ...       1.0
# 4  2234561-5  ...       1.0
#
# [5 rows x 11 columns]


import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from pandas.errors import EmptyDataError
import plotly.express as px

# ------------------------------------------------------------------------------
# CONFIGURAÇÃO DO STREAMLIT
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Presença, Votações e Remuneração dos Deputados",
    layout="wide"
)

# ------------------------------------------------------------------------------
# LOCALIZAÇÃO DOS DADOS
# ------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
PROC_DIR = DATA_DIR / "processed"
INFO_DIR = DATA_DIR / "info"


# ------------------------------------------------------------------------------
# CARREGAMENTO INTELIGENTE DE DADOS
# ------------------------------------------------------------------------------
@st.cache_data
def load_data():
    # Deputados
    deputados = pd.read_json(PROC_DIR / "deputados.json", orient="records")

    # Eventos (sessões)
    eventos = pd.read_csv(PROC_DIR / "eventos.csv")
    eventos["dataHoraInicio"] = pd.to_datetime(eventos["dataHoraInicio"])
    eventos["ano"] = eventos["dataHoraInicio"].dt.year

    # Presenças
    presencas = pd.read_csv(PROC_DIR / "presencas.csv")

    # Remunerações -> NÃO EXISTE VALOR, usamos valor oficial ANUAL (proxy)
    # R$ 41.650,92/mês -> 499.811,04/ano
    salario_anual = 499_811.04
    remuneracoes = deputados[["id"]].rename(columns={"id": "id_deputado"})
    remuneracoes["ano"] = 2020  # proxy: todos os mandatos
    remuneracoes["valor_bruto"] = salario_anual

    # Votações -> não têm id_deputado: proxy = presença em sessão
    vot_files = sorted(PROC_DIR.glob("votacoes_*.csv"))
    vot_list = []
    for vf in vot_files:
        try:
            if vf.stat().st_size == 0:
                continue
            df = pd.read_csv(vf)
            if df.empty or len(df.columns) == 0:
                continue
            df["data"] = pd.to_datetime(df["data"], errors="coerce")
            df["ano"] = df["data"].dt.year
            vot_list.append(df)
        except EmptyDataError:
            continue

    votacoes = pd.concat(vot_list, ignore_index=True) if vot_list else pd.DataFrame()

    return deputados, eventos, presencas, remuneracoes, votacoes


deputados, eventos, presencas, remuneracoes, votacoes = load_data()


# ------------------------------------------------------------------------------
# DIMENSÕES CONSISTENTES
# ------------------------------------------------------------------------------
deputados_dim = deputados.rename(columns={
    "id": "id_deputado",
    "nome": "nome",
    "siglaPartido": "partido",
    "siglaUf": "uf"
})[["id_deputado", "nome", "partido", "uf"]].drop_duplicates()


# ------------------------------------------------------------------------------
# PROXY DE PRESENÇA
# ------------------------------------------------------------------------------
# Regra: SE APARECEU EM id_evento → PRESENÇA
presencas["is_presente"] = True

# Extrair ano do evento associado
presencas = presencas.merge(
    eventos[["id", "ano"]].rename(columns={"id": "id_evento"}),
    on="id_evento",
    how="left"
)

# ------------------------------------------------------------------------------
# PROXY DE PARTICIPAÇÃO EM VOTAÇÕES
# ------------------------------------------------------------------------------
votacoes_anos = votacoes["ano"].unique().tolist() if not votacoes.empty else []


# ------------------------------------------------------------------------------
# SIDEBAR — FILTROS
# ------------------------------------------------------------------------------
st.sidebar.header("Filtros")

anos_disponiveis = sorted(eventos["ano"].unique().tolist())
ano_inicio, ano_fim = st.sidebar.select_slider(
    "Período (ano)",
    options=anos_disponiveis,
    value=(anos_disponiveis[0], anos_disponiveis[-1])
)

partidos = ["(Todos)"] + sorted(deputados_dim["partido"].dropna().unique().tolist())
ufs = ["(Todos)"] + sorted(deputados_dim["uf"].dropna().unique().tolist())

partido_sel = st.sidebar.selectbox("Partido", partidos)
uf_sel = st.sidebar.selectbox("UF", ufs)

# filtrar deputados
dep_filtro = deputados_dim.copy()
if partido_sel != "(Todos)":
    dep_filtro = dep_filtro[dep_filtro["partido"] == partido_sel]
if uf_sel != "(Todos)":
    dep_filtro = dep_filtro[dep_filtro["uf"] == uf_sel]

dep_nomes = ["(Todos)"] + sorted(dep_filtro["nome"].tolist())
dep_sel = st.sidebar.selectbox("Deputado", dep_nomes)

if dep_sel != "(Todos)":
    ids_dep = dep_filtro[dep_filtro["nome"] == dep_sel]["id_deputado"].tolist()
else:
    ids_dep = dep_filtro["id_deputado"].tolist()


# ------------------------------------------------------------------------------
# APLICAR FILTROS TEMPORAIS
# ------------------------------------------------------------------------------
eventos_sel = eventos[eventos["ano"].between(ano_inicio, ano_fim)]
presencas_sel = presencas[
    (presencas["id_deputado"].isin(ids_dep)) &
    (presencas["ano"].between(ano_inicio, ano_fim))
]
rem_sel = remuneracoes  # remuneração anual é fixa
votacoes_sel = votacoes[votacoes["ano"].between(ano_inicio, ano_fim)]


# ------------------------------------------------------------------------------
# CÁLCULO 1 — PRESENÇAS
# ------------------------------------------------------------------------------
total_sessoes = eventos_sel["id"].nunique()

pres_por_dep = (
    presencas_sel.groupby("id_deputado")["is_presente"]
    .sum()
    .reset_index()
    .rename(columns={"is_presente": "presencas"})
)
pres_por_dep["total_sessoes"] = total_sessoes
pres_por_dep["taxa_presenca"] = pres_por_dep["presencas"] / pres_por_dep["total_sessoes"]


# ------------------------------------------------------------------------------
# CÁLCULO 2 — TAXA DE PARTICIPAÇÃO EM VOTAÇÕES (proxy)
# ------------------------------------------------------------------------------
# Como não há votos individuais → participação = presença
vot_por_dep = pres_por_dep.rename(columns={"presencas": "votacoes_participadas"})
total_votacoes_periodo = max(votacoes_sel.shape[0], 1)  # evitar divisão por zero
vot_por_dep["total_votacoes"] = total_votacoes_periodo
vot_por_dep["taxa_participacao"] = (
    vot_por_dep["votacoes_participadas"] / vot_por_dep["total_votacoes"]
)


# ------------------------------------------------------------------------------
# CÁLCULO 3 — REMUNERAÇÃO E GANHOS
# ------------------------------------------------------------------------------
rem_sel = rem_sel[rem_sel["id_deputado"].isin(ids_dep)]
rem_por_dep = rem_sel.groupby("id_deputado")["valor_bruto"].sum().reset_index()

# Junta tudo num fato único
fato = (
    deputados_dim.merge(pres_por_dep, on="id_deputado", how="left")
    .merge(vot_por_dep, on="id_deputado", how="left")
    .merge(rem_por_dep, on="id_deputado", how="left")
)

# Garantir colunas essenciais
if "presencas" not in fato.columns:
    fato["presencas"] = 0
if "votacoes_participadas" not in fato.columns:
    fato["votacoes_participadas"] = 0
if "taxa_participacao" not in fato.columns:
    fato["taxa_participacao"] = 0.0
if "valor_bruto" not in fato.columns:
    fato["valor_bruto"] = 0.0

# adicionar total de sessões (mesmo valor para todos no período selecionado)
fato["total_sessoes"] = total_sessoes

# preencher NA e tipos
fato["presencas"] = fato["presencas"].fillna(0).astype(int)
fato["votacoes_participadas"] = fato["votacoes_participadas"].fillna(0).astype(int)
fato["taxa_participacao"] = fato["taxa_participacao"].fillna(0.0)
fato["valor_bruto"] = fato["valor_bruto"].fillna(0.0)

# 🔥 RECALCULAR taxa de presença AQUI, DIRETO DA TABELA FATO
fato["taxa_presenca"] = np.where(
    fato["total_sessoes"] > 0,
    fato["presencas"] / fato["total_sessoes"],
    np.nan
)


fato["ganho_por_dia"] = np.where(
    fato["presencas"] > 0,
    fato["valor_bruto"] / fato["presencas"],
    np.nan
)

fato["ganho_por_votacao"] = np.where(
    fato["votacoes_participadas"] > 0,
    fato["valor_bruto"] / fato["votacoes_participadas"],
    np.nan
)

# porcentagem
fato["taxa_presenca_pct"] = fato["taxa_presenca"] * 100
fato["taxa_participacao_pct"] = fato["taxa_participacao"] * 100


# ------------------------------------------------------------------------------
# CÁLCULO 4 — SIMULAÇÃO CLT
# ------------------------------------------------------------------------------
st.sidebar.header("Simulação CLT")

max_faltas_pct = st.sidebar.slider(
    "Máximo permitido de faltas (%)",
    min_value=0, max_value=100, value=30, step=5
)

fato["faltas_rel"] = 1 - fato["taxa_presenca"]
limite = max_faltas_pct / 100
fato["respeita_CLT"] = fato["faltas_rel"] <= limite


# ------------------------------------------------------------------------------
# TÍTULO E GLOSSÁRIO
# ------------------------------------------------------------------------------
st.title("📊 Análise de Presença, Votações e Remuneração — Deputados Federais")

st.markdown("""
Aplicação desenvolvida para o projeto de **Mineração de Dados** da disciplina,
com o objetivo de analisar presença, votações e remuneração de deputados federais,
comparando essas métricas com padrões da CLT.
""")

st.markdown("---")


# ------------------------------------------------------------------------------
# KPIs DO PERÍODO
# ------------------------------------------------------------------------------
st.subheader("📌 Indicadores Gerais")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Presença média (%)", f"{(fato['taxa_presenca'].mean()*100):.1f}%")
with col2:
    st.metric("Participação média (%)", f"{(fato['taxa_participacao'].mean()*100):.1f}%")
with col3:
    st.metric("Ganho médio por dia (R$)", f"{fato['ganho_por_dia'].mean():,.2f}")
with col4:
    st.metric("Ganho médio por votação (R$)", f"{fato['ganho_por_votacao'].mean():,.2f}")

st.write(f"**% que respeitam a CLT:** {(fato['respeita_CLT'].mean()*100):.1f}%")

st.markdown("---")


# ------------------------------------------------------------------------------
# ABAS DE VISUALIZAÇÃO (PLOTLY EXPRESS)
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Distribuição de Presença",
    "Ranking de Presença",
    "Presença x Ganho por Dia",
    "Simulação CLT",
    "Partidos / UF"
])

# ------------------------------------------------------------------------------
# TAB 1 → HISTOGRAMA DE PRESENÇA (Objetivo 1 + 5)
# ------------------------------------------------------------------------------
with tab1:
    st.subheader("Distribuição da Taxa de Presença (%) dos Deputados")

    df_hist = fato.copy()
    df_hist = df_hist[df_hist["taxa_presenca_pct"].notna()]

    if not df_hist.empty:
        df_hist["respeita_CLT_label"] = np.where(
            df_hist["respeita_CLT"], "Respeita CLT", "Não respeita CLT"
        )

        fig_hist = px.histogram(
            df_hist,
            x="taxa_presenca_pct",
            nbins=20,
            color="respeita_CLT_label",
            labels={"taxa_presenca_pct": "Taxa de presença (%)", "count": "Número de deputados"},
            title="Distribuição da presença em sessões deliberativas",
            opacity=0.8,
            barmode="overlay"
        )
        fig_hist.update_layout(legend_title_text="Simulação CLT")
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.info("Não há dados de presença para o período/filtragem selecionados.")


# ------------------------------------------------------------------------------
# TAB 2 → RANKING DE PRESENÇA (Objetivo 1)
# ------------------------------------------------------------------------------
with tab2:
    st.subheader("Ranking de Presença por Deputado")

    df_rank = fato.copy()
    df_rank = df_rank[df_rank["taxa_presenca_pct"].notna()]

    if not df_rank.empty:
        modo = st.radio(
            "Tipo de ranking",
            ["Top 20 mais presentes", "Top 20 menos presentes"],
            horizontal=True
        )

        if modo == "Top 20 mais presentes":
            df_rank = df_rank.sort_values("taxa_presenca_pct", ascending=False).head(20)
        else:
            df_rank = df_rank.sort_values("taxa_presenca_pct", ascending=True).head(20)

        fig_rank = px.bar(
            df_rank,
            x="taxa_presenca_pct",
            y="nome",
            color="partido",
            orientation="h",
            labels={"taxa_presenca_pct": "Taxa de presença (%)", "nome": "Deputado"},
            title="Ranking de presença por deputado"
        )
        fig_rank.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig_rank, use_container_width=True)

        st.markdown("Tabela detalhada dos deputados exibidos:")
        st.dataframe(
            df_rank[["nome", "partido", "uf", "presencas", "total_sessoes", "taxa_presenca_pct"]]
            .rename(columns={"taxa_presenca_pct": "taxa_presenca_%"}),
            use_container_width=True
        )
    else:
        st.info("Não há dados suficientes para montar o ranking de presença.")


# ------------------------------------------------------------------------------
# TAB 3 → SCATTER PRESENÇA × GANHO POR DIA (Objetivo 4 + 5)
# ------------------------------------------------------------------------------
with tab3:
    st.subheader("Relação entre Presença (%) e Ganho por Dia (R$)")

    df_scatter = fato.copy()
    df_scatter = df_scatter[
        df_scatter["taxa_presenca_pct"].notna() & df_scatter["ganho_por_dia"].notna()
    ]

    if not df_scatter.empty:
        df_scatter["respeita_CLT_label"] = np.where(
            df_scatter["respeita_CLT"], "Respeita CLT", "Não respeita CLT"
        )

        fig_scatter = px.scatter(
            df_scatter,
            x="taxa_presenca_pct",
            y="ganho_por_dia",
            color="respeita_CLT_label",
            hover_data=["nome", "partido", "uf", "presencas"],
            labels={
                "taxa_presenca_pct": "Taxa de presença (%)",
                "ganho_por_dia": "Ganho por dia trabalhado (R$)"
            },
            title="Deputados: presença em sessões x ganho efetivo por dia"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

        st.markdown("""
        - Deputados com **baixa presença** e **ganho por dia elevado** ilustram a desigualdade entre
          remuneração fixa e trabalho efetivo, em comparação ao regime **CLT**.
        """)
    else:
        st.info("Não há dados suficientes para relacionar presença e ganho por dia.")


# ------------------------------------------------------------------------------
# TAB 4 → PIZZA + BARRAS CLT (Objetivo 3)
# ------------------------------------------------------------------------------
with tab4:
    st.subheader("Simulação de CLT: Limite de Faltas")

    df_clt = fato.copy()
    df_clt = df_clt[df_clt["respeita_CLT"].notna()]

    if not df_clt.empty:
        df_clt["respeita_CLT_label"] = np.where(
            df_clt["respeita_CLT"], "Respeita CLT", "Não respeita CLT"
        )

        col_pizza, col_bar = st.columns(2)

        with col_pizza:
            clt_counts = df_clt["respeita_CLT_label"].value_counts().reset_index()
            clt_counts.columns = ["respeita_CLT_label", "qtd"]
            fig_pie = px.pie(
                clt_counts,
                values="qtd",
                names="respeita_CLT_label",
                title="Proporção de deputados que respeitam o limite de faltas (simulação CLT)"
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with col_bar:
            clt_partido = (
                df_clt.groupby(["partido", "respeita_CLT_label"])
                .size()
                .reset_index(name="qtd")
            )

            fig_bar = px.bar(
                clt_partido,
                x="partido",
                y="qtd",
                color="respeita_CLT_label",
                labels={"qtd": "Número de deputados", "partido": "Partido"},
                title="Respeito ao limite de faltas por partido (simulação CLT)",
                barmode="stack"
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown(f"""
        - Limite de faltas usado na simulação: **{max_faltas_pct}%**.
        - Deputados marcados como **“Não respeita CLT”** possuem taxa de faltas acima desse limite.
        """)
    else:
        st.info("Não há dados suficientes para a simulação de CLT.")


# ------------------------------------------------------------------------------
# TAB 5 → BOXPLOTS POR PARTIDO/UF (Objetivo 5)
# ------------------------------------------------------------------------------
with tab5:
    st.subheader("Distribuição de Presença e Ganho por Dia por Partido/UF")

    dim_label = st.selectbox("Agrupar por:", ["Partido", "UF"])
    group_col = "partido" if dim_label == "Partido" else "uf"

    df_box = fato.copy()
    df_box = df_box[
        df_box[group_col].notna() &
        df_box["taxa_presenca_pct"].notna() &
        df_box["ganho_por_dia"].notna()
    ]

    if not df_box.empty:
        # opcional: filtrar grupos com poucos deputados (ex.: pelo menos 5)
        counts = df_box[group_col].value_counts()
        grupos_validos = counts[counts >= 5].index
        df_box = df_box[df_box[group_col].isin(grupos_validos)]

        if df_box.empty:
            st.info("Não há grupos com número suficiente de deputados para exibir boxplots.")
        else:
            col_a, col_b = st.columns(2)

            with col_a:
                fig_box_pres = px.box(
                    df_box,
                    x=group_col,
                    y="taxa_presenca_pct",
                    labels={
                        group_col: dim_label,
                        "taxa_presenca_pct": "Taxa de presença (%)"
                    },
                    title=f"Distribuição da taxa de presença por {dim_label.lower()}"
                )
                st.plotly_chart(fig_box_pres, use_container_width=True)

            with col_b:
                fig_box_ganho = px.box(
                    df_box,
                    x=group_col,
                    y="ganho_por_dia",
                    labels={
                        group_col: dim_label,
                        "ganho_por_dia": "Ganho por dia (R$)"
                    },
                    title=f"Distribuição do ganho por dia por {dim_label.lower()}"
                )
                st.plotly_chart(fig_box_ganho, use_container_width=True)

            st.markdown(f"""
            - Esses boxplots permitem comparar **diferenças estruturais** entre {dim_label.lower()}s,
              tanto em termos de **presença** quanto de **ganho efetivo por dia**.
            """)
    else:
        st.info("Não há dados suficientes para montar boxplots por partido/UF.")
