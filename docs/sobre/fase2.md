# Etapa 2:

---

## Compreensão dos Dados:
Esta seção descreve a compreensão inicial sobre os dados. Desde sua coleta inicial, passando por uma análise exploratória até uma avaliação de sua qualidade.

| Aspecto                  | Resumo                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Objetivo da etapa**    | Entender o **escopo, estrutura, qualidade e padrões** dos dados para suportar métricas de assiduidade e participação.                                  |
| **Fontes e contexto**    | **API Dados Abertos da Câmara** (`/deputados`, `/deputados/{id}/eventos`), dados oficiais e públicos.                                                  |
| **Entidades principais** | **Deputados** (metadados e identificadores) e **Eventos** (sessões, reuniões, comissões, visitas técnicas).                                            |
| **Período analisado**    | **2020-01-01** até a data da coleta.                                                                                                                   |
| **Arquivos processados** | `data/processed/deputados.json`, `data/processed/eventos.json`, `data/processed/descritivo_campos.json`.                                               |
| **Principais variáveis** | `id`, `nome`, `siglaPartido`, `siglaUf`, `idLegislatura`, `dataHoraInicio`, `descricaoTipo`, `situacao`, `id_deputado`.                                |
| **Operações realizadas** | Coleta paginada; tipagem de datas; junção Deputados×Eventos; contagens e estatísticas; gráficos de distribuição e ranking.                             |
| **Qualidade observada**  | Sem duplicados de deputados; **nulos elevados** em campos opcionais de eventos (ex.: `dataHoraFim`, `localExterno`, `urlRegistro`); sem datas futuras. |
| **Limitações**           | Campos aninhados (`orgaos`, `localCamara`) e informativos frequentemente nulos; necessidade de paginação.                                              |
| **Próximos passos**      | Limpeza leve, normalização mínima (quando necessário), definição de métricas de assiduidade e integração para análises comparativas.                   |

---

## Coleta dos dados:
Descrição de como os dados foram adquiridos. Seu contexto, fontes, métodos de aquisição e problemas encontrados.

| Item                          | Decisão/Implementação                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------- |
| **Fonte oficial**             | API Dados Abertos da Câmara dos Deputados                                                   |
| **Endpoints**                 | `/deputados`, `/deputados/{id}/eventos`                                                     |
| **Período**                   | `dataInicio=2020-01-01` até a data da coleta (`dataFim=YYYY-MM-DD`)                         |
| **Parâmetros**                | `itens=100` (máx. por página), `ordenarPor=dataHoraInicio`, `ordem=ASC`, `pagina=1..N`      |
| **Método de aquisição**       | Requisições HTTP `GET` com `requests` (Python) + paginação em loop                          |
| **Controle de paginação**     | Incremento de `pagina` até a resposta vir vazia (`dados=[]`)                                |
| **Tratamento de erro**        | `status_code` verificado; log simples por deputado/página em caso de erro                   |
| **Formatação e persistência** | JSON com `orient="records"`, `indent=2`, `force_ascii=False`                                |
| **Arquivos gerados**          | `data/processed/deputados.json`, `data/processed/eventos.json`                              |
| **Automação/execução**        | Notebooks `lab/01_coleta_dados.ipynb` (coleta) e `lab/02_descricao_dados.ipynb` (descrição) |

- **⚠️ Problemas encontrados e mitigação:**

| Problema                                                                                                   | Impacto                                                       | Mitigação aplicada                                                                                      |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Campos opcionais ausentes em eventos (ex.: `dataHoraFim`, `localExterno`, `urlRegistro`, campos aninhados) | Aumenta contagem de nulos, mas não afeta contagem de presença | Manter `NaN`/`None`; foco em campos essenciais (`id`, `dataHoraInicio`, `descricaoTipo`, `id_deputado`) |
| Necessidade de paginação                                                                                   | API não retorna tudo de uma vez                               | Laço `pagina=1..N` até `dados` vazio                                                                    |
| Estruturas aninhadas (`orgaos`, `localCamara`)                                                             | Dificulta agregações diretas                                  | Normalizar somente se necessário em análises temáticas                                                  |
| Possível instabilidade pontual da API                                                                      | Requisição pode falhar em alguns IDs/páginas                  | Verificação de `status_code` e log do erro; reexecução idempotente por deputado                         |
| Performance ao coletar muitos anos                                                                         | Tempo de execução mais alto                                   | Coleta por lotes (subconjuntos de deputados) durante desenvolvimento                                    |

---

## Descrição dos dados:
Descrição de cada base de dados, incluindo cada campo, tipo de dados, unidade utilizada, códigos etc.

- **Deputados (data/processed/deputados.json):**

| Campo           | Tipo (pandas) | Exemplo                        | Descrição / Unidade / Código                                 |
| --------------- | ------------- | ------------------------------ | ------------------------------------------------------------ |
| `id`            | int64         | `220595`                       | **ID único** do parlamentar (chave primária).                |
| `nome`          | object        | `Coronel Fernanda`             | Nome civil do(a) deputado(a).                                |
| `siglaPartido`  | object        | `PL`                           | **Sigla do partido** atual (código partidário oficial).      |
| `siglaUf`       | object        | `MT`                           | **UF** de representação (código de estado, ex.: `SP`, `RJ`). |
| `idLegislatura` | int64         | `57`                           | Número da legislatura (inteiro).                             |
| `email`         | object        | `dep.nome@camara.leg.br`       | E-mail institucional.                                        |
| `uri`           | object        | `https://.../deputados/220595` | URL do recurso do deputado na API.                           |
| `uriPartido`    | object        | `https://.../partidos/37906`   | URL do recurso do partido na API.                            |
| `urlFoto`       | object        | `https://.../220595.jpg`       | URL da foto oficial.                                         |

- **Eventos (data/processed/eventos.json):**

| Campo            | Tipo (pandas)          | Exemplo                               | Descrição / Unidade / Código                                              |
| ---------------- | ---------------------- | ------------------------------------- | ------------------------------------------------------------------------- |
| `id`             | int64                  | `79992`                               | **ID único** do evento (chave primária do evento).                        |
| `descricaoTipo`  | object                 | `Sessão Deliberativa`                 | Tipo do evento (categoria textual).                                       |
| `descricao`      | object                 | `Sessão Deliberativa Extraordinária…` | Título/descrição pública do evento.                                       |
| `situacao`       | object                 | `Encerrada` / `Cancelada`             | Situação do evento.                                                       |
| `dataHoraInicio` | object → datetime      | `2025-10-23T10:00`                    | Início (ISO-8601). Converter para `datetime` nas análises.                |
| `dataHoraFim`    | object → datetime/null | `2025-10-23T11:48`                    | Fim (ISO-8601). Pode ser **nulo** (ex.: eventos cancelados/sem registro). |
| `localExterno`   | object/null            | `Scala Data Centers – Barueri, SP`    | Local fora da Câmara (texto livre). Pode ser **nulo**.                    |
| `localCamara`    | object (dict)          | `{nome, predio, sala, andar}`         | Local dentro da Câmara (estrutura aninhada). Pode conter **nulos**.       |
| `orgaos`         | object (lista)         | `[ { id, sigla, nome, ... } ]`        | Órgãos/comissões relacionados (estrutura aninhada).                       |
| `urlRegistro`    | object/null            | `https://www.youtube.com/...`         | Link de registro/transmissão. Pode ser **nulo**.                          |
| `id_deputado`    | int64                  | `160527`                              | **FK** para `deputados.id` (relaciona evento ↔ deputado).                 |

- **🔐 Chaves e Relacionamentos:**

| Relação             | Chave de junção                        | Cardinalidade                                       |
| ------------------- | -------------------------------------- | --------------------------------------------------- |
| Deputados ↔ Eventos | `deputados.id` = `eventos.id_deputado` | **1 : N** (um deputado participa de vários eventos) |

- **📏 Convenções / Códigos / Unidades:**

| Campo                            | Convenção / Código                                | Observações                                                    |
| -------------------------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| `siglaUf`                        | Código UF (`AC`, `AL`, `AM`, …, `SP`, `RJ`)       | Padrão IBGE/UF.                                                |
| `siglaPartido`                   | Sigla partidária oficial (`PL`, `UNIÃO`, `PT`, …) | Obtida da própria API (coerente com `uriPartido`).             |
| `dataHoraInicio` / `dataHoraFim` | ISO-8601 (`YYYY-MM-DDTHH:MM`)                     | Converter para `datetime` (timezone não explicitado pela API). |
| `situacao`                       | Categorias textuais                               | Ex.: `Encerrada`, `Cancelada`, `Realizada`.                    |
| `descricaoTipo`                  | Categorias textuais                               | Ex.: `Sessão Deliberativa`, `Visita Técnica`, `Reunião`.       |


---

## Análise exploratória dos dados:
Descrição da exploração inicial dos dados, incluindo objetivos de exploração. Quais operações ou métodos foram realizados, quais padrões nos dados foram encontrados, sejam esperados ou não. Conclusões em relação aos objetivos de mineração e ao que deve ser realizado na etapa de preparação dos dados (limpeza, transformação, pré-processamento).

- **🎯 Objetivos e Perguntas de EDA:**

| Objetivo                    | Pergunta de análise                                      | Métrica/Indicador                                           | Interpretação esperada                                                            |
| --------------------------- | -------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Quantificar atuação         | Quantos eventos cada deputado teve desde 2020?           | `num_eventos = groupby(id_deputado).size()`                 | Distribuição assimétrica; existência de outliers (muito acima da média).          |
| Entender tendência temporal | Houve aumento/diminuição de eventos por ano (2020→2025)? | Contagem por `ano = year(dataHoraInicio)`                   | Variação anual; possíveis quedas em anos eleitorais/recessos.                     |
| Tipificar atividades        | Quais tipos de eventos são mais comuns?                  | `value_counts(descricaoTipo)`                               | Predominância de **Sessões Deliberativas**; menor frequência de visitas técnicas. |
| Comparar grupos             | Há diferenças por partido/UF?                            | Média/mediana de `num_eventos` por `siglaPartido`/`siglaUf` | Heterogeneidade entre grupos; identificar extremos.                               |
| Identificar extremos        | Quem são os Top 10 em participações?                     | `sort_values(num_eventos).tail(10)`                         | Concentração de participações em poucos parlamentares.                            |

- **🛠️ Operações e Métodos Executados Etapa:**

| Tema                      | Evidência (exemplos)                                            | Como validar no notebook                  | Implicação                                              |
| ------------------------- | --------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| Distribuição              | **Assimétrica**: muitos com poucos eventos e poucos com muitos. | Histograma de `num_eventos`; `describe()` | Necessário tratar outliers em comparações.              |
| Concentração              | **Top 10** concentram fração relevante das participações.       | `Top 10` (barplot)                        | Considerar métricas normalizadas (por período/mandato). |
| Temporalidade             | Variação por **ano** (2020→2025).                               | Contagem por `ano`                        | Comparar por janela anual para justiça temporal.        |
| Tipologia                 | **Sessões Deliberativas** são as mais frequentes.               | `value_counts(descricaoTipo)`             | Focar nelas para métrica-base de assiduidade.           |
| Heterogeneidade por grupo | Diferenças por **partido/UF**.                                  | Média/mediana por grupo                   | Relatar apenas diferenças robustas (mediana/boxplot).   |

- **📈 Principais Achados/Padrões (preencher com valores do notebook):**

| Tema                      | Evidência (exemplos)                                            | Como validar no notebook                  | Implicação                                              |
| ------------------------- | --------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| Distribuição              | **Assimétrica**: muitos com poucos eventos e poucos com muitos. | Histograma de `num_eventos`; `describe()` | Necessário tratar outliers em comparações.              |
| Concentração              | **Top 10** concentram fração relevante das participações.       | `Top 10` (barplot)                        | Considerar métricas normalizadas (por período/mandato). |
| Temporalidade             | Variação por **ano** (2020→2025).                               | Contagem por `ano`                        | Comparar por janela anual para justiça temporal.        |
| Tipologia                 | **Sessões Deliberativas** são as mais frequentes.               | `value_counts(descricaoTipo)`             | Focar nelas para métrica-base de assiduidade.           |
| Heterogeneidade por grupo | Diferenças por **partido/UF**.                                  | Média/mediana por grupo                   | Relatar apenas diferenças robustas (mediana/boxplot).   |

- **🧭 Conclusões e Próximos Passos para Preparação:**

| Necessidade               | Ação de preparação                                                  | Justificativa                          | Impacto nas métricas                     |
| ------------------------- | ------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------- |
| Normalizar por período    | Calcular `num_eventos` por **ano** e por **janela fixa**            | Comparabilidade entre anos e mandatos  | Métricas mais justas entre parlamentares |
| Tratar nulos não críticos | Manter `NaN`/`None` em `dataHoraFim`, `localExterno`, `urlRegistro` | Não afetam presença/contagem           | Evita distorções desnecessárias          |
| Outliers                  | Reportar, não excluir; usar **mediana** e **IQR** em comparações    | Distribuição assimétrica               | Comparações mais robustas                |
| Tipagem consistente       | Garantir `datetime` em datas                                        | Evitar erros em agregações temporais   | Séries temporais corretas                |
| Flatten seletivo          | Extrair `orgaos.sigla` **quando necessário**                        | Campos aninhados dificultam agregações | Possibilita análises por comissão/órgão  |
| Persistência              | Versões com timestamp                                               | Reprodutibilidade e auditoria          | Histórico claro de coletas               |


- **📌 Checklist rápido (EDA):**

| Item                                 | Status |
| ------------------------------------ | ------ |
| Datas convertidas (`dataHoraInicio`) | ☐      |
| `num_eventos` por deputado           | ☐      |
| Histograma de `num_eventos`          | ☐      |
| Top 10 participação                  | ☐      |
| Frequência por `descricaoTipo`       | ☐      |
| Tabela por partido/UF                | ☐      |
| Conclusões e ações de preparação     | ☐      |

---

## Verificação de qualidade dos dados:
Descrição das abordagens e critérios utilizados para avaliar a qualidade dos dados originais e o resultado encontrado com estas avaliações.

- **🧪 Abordagens e critérios de verificação:**

| Aspecto avaliado           | Critério aplicado              | Como foi medido                                         | Limite/Regra                                       |
| -------------------------- | ------------------------------ | ------------------------------------------------------- | -------------------------------------------------- |
| **Completude**             | Percentual de nulos por coluna | `df.isna().sum()` e proporção por total                 | **Campos críticos** (IDs, datas-chave): ≤ 5% nulos |
| **Unicidade**              | Duplicidade de chaves          | `df.duplicated("id")` (deputados)                       | **0** duplicatas para chave primária               |
| **Consistência temporal**  | Datas válidas e não futuras    | `to_datetime` + comparação com `now()`                  | Nenhuma data futura inválida                       |
| **Integridade relacional** | Chave estrangeira presente     | `eventos.id_deputado ∈ deputados.id`                    | 100% das linhas com correspondência                |
| **Tipos de dados**         | Tipagem esperada               | Checagem de `dtypes` e coerção de datas                 | Datas convertidas sem erro (ou `NaT`)              |
| **Campos aninhados**       | Estrutura legível              | Verificação de presença/forma (`orgaos`, `localCamara`) | Normalizar **apenas se necessário** às análises    |


- **📊 Resultados encontrados (execução atual):**

| Métrica                                             | Deputados |             Eventos | Interpretação                                                                                                            |
| --------------------------------------------------- | --------: | ------------------: | ------------------------------------------------------------------------------------------------------------------------ |
| **Campos nulos (contagem total)**                   |     **0** |          **11.386** | Nulos concentrados em campos **não críticos** (ex.: `dataHoraFim`, `localExterno`, `urlRegistro`, estruturas aninhadas). |
| **Duplicados (por `id`)**                           |     **0** |                   — | Chave primária de deputados sem duplicatas.                                                                              |
| **Eventos com data futura**                         |         — |               **0** | Sem inconsistências temporais.                                                                                           |
| **Integridade FK (`id_deputado` ↔ `deputados.id`)** |         — |              **OK** | Relação **1:N** preservada.                                                                                              |
| **Tipagem**                                         |        OK | OK (datas coeridas) | `dataHoraInicio` convertido para `datetime` com `errors="coerce"`.                                                       |


- **🧹 Plano de tratamento (para preparação dos dados):**

| Problema                                              | Impacto                   | Ação                                                                | Efeito esperado                       |
| ----------------------------------------------------- | ------------------------- | ------------------------------------------------------------------- | ------------------------------------- |
| Nulos em `dataHoraFim`, `localExterno`, `urlRegistro` | Baixo (não críticos)      | Manter como `NaN`/`None`; usar apenas `dataHoraInicio` nas métricas | Evita descartar registros válidos     |
| Campos aninhados (`orgaos`, `localCamara`)            | Dificulta agregações      | **Flatten seletivo** quando necessário à análise                    | Possibilita cortes por comissão/órgão |
| Outliers de participação                              | Distorce média            | Reportar; usar **mediana/IQR** em comparações                       | Métricas mais robustas                |
| Tipagem de data                                       | Erros em séries temporais | Forçar `to_datetime` (UTC-safe), checar `NaT`                       | Consistência temporal                 |
| Reprodutibilidade                                     | Auditoria                 | Salvar versão/`timestamp` das coletas                               | Histórico claro de execução           |
