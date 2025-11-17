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

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from pandas.errors import EmptyDataError

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
# Não existe voto individual → usamos presença em sessão deliberativa
# Taxa de participação = taxa de presenças
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
vot_por_dep["total_votacoes"] = votacoes_sel.shape[0]  # quantidade de votações no período
vot_por_dep["taxa_participacao"] = vot_por_dep["votacoes_participadas"] / vot_por_dep["total_votacoes"]


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
if "taxa_presenca" not in fato.columns:
    fato["taxa_presenca"] = 0.0
if "taxa_participacao" not in fato.columns:
    fato["taxa_participacao"] = 0.0
if "valor_bruto" not in fato.columns:
    fato["valor_bruto"] = 0.0

# ⭐ Adicionar total de sessões para todos os deputados
fato["total_sessoes"] = total_sessoes

# Se não existir a coluna, cria
if "taxa_presenca" not in fato.columns:
    fato["taxa_presenca"] = 0.0

if "taxa_participacao" not in fato.columns:
    fato["taxa_participacao"] = 0.0

if "presencas" not in fato.columns:
    fato["presencas"] = 0

if "votacoes_participadas" not in fato.columns:
    fato["votacoes_participadas"] = 0

# Remuneração sempre existe, mas garantir
if "valor_bruto" not in fato.columns:
    fato["valor_bruto"] = 0.0

# Preencher NA sem quebrar os tipos
fato["taxa_presenca"] = fato["taxa_presenca"].fillna(0.0)
fato["taxa_participacao"] = fato["taxa_participacao"].fillna(0.0)
fato["presencas"] = fato["presencas"].fillna(0).astype(int)
fato["votacoes_participadas"] = fato["votacoes_participadas"].fillna(0).astype(int)
fato["valor_bruto"] = fato["valor_bruto"].fillna(0.0)

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

### Conceitos importantes
- **Presença**: deputado apareceu na sessão (proxy válido pela estrutura dos dados).  
- **Votação participada**: proxy baseada em presença em sessão.  
- **Ganho por dia/votação**: salário anual dividido pelos eventos efetivamente trabalhados.  
- **Simulação CLT**: limite proporcional de faltas aceito.
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
# TABELA DETALHADA
# ------------------------------------------------------------------------------
st.subheader("📄 Tabela Detalhada por Deputado")

cols = [
    "nome", "partido", "uf",
    "total_sessoes", "presencas", "taxa_presenca",
    "votacoes_participadas", "taxa_participacao",
    "valor_bruto", "ganho_por_dia", "ganho_por_votacao",
    "respeita_CLT"
]

tabela = fato[cols].copy()
tabela["taxa_presenca"] *= 100
tabela["taxa_participacao"] *= 100

st.dataframe(tabela.sort_values("ganho_por_dia", ascending=False))


# ------------------------------------------------------------------------------
# GRÁFICO PRESENÇA vs GANHO POR DIA
# ------------------------------------------------------------------------------
st.subheader("📉 Relação: Presença (%) x Ganho por Dia (R$)")

scatter = fato[["nome", "taxa_presenca", "ganho_por_dia"]].copy()
scatter["taxa_presenca"] *= 100
scatter = scatter.dropna()

st.scatter_chart(scatter, x="taxa_presenca", y="ganho_por_dia")

st.markdown("""
### Interpretação

- Deputados com **baixa presença** tendem a ter **ganho por dia muito maior**, pois o salário é fixo.
- O comportamento é facilmente comparável ao regime **CLT**, onde faltas têm impacto direto.
- A análise evidencia padrões de **desigualdade estrutural** entre o trabalho legislativo e o trabalho civil.
""")
