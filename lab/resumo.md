# Resumo:

---

# Resultado dos códigos:
## 01_coleta_dados.ipynb

### Datasets criados:

**deputados.json** - id, uri, nome, siglaPartido, uriPartido, siglaUF, idLegislatura, urlFoto e email

**freq_eventos.csv** - id_deputado e num_eventos

**votos_deputados.csv** - id_votacao e id_deputado

**ocupacoes.csv** - id_deputado, titulo

**cod_situacao_deputados.json** - cod(vazio), sigla, nome, descricao

**eventos_sessoes.csv** - id_evento, dataHoraInicio e dataHoraFim


---

## 02_descricao_dados.ipynb


## 03_analise_exploratoria.ipynb


## 04_verificacao_qualidade.ipynb

---

# Perguntas para responder:

## Compreensão dos Dados:
Esta seção descreve a compreensão inicial sobre os dados. Desde sua coleta inicial, passando por uma análise exploratória até uma avaliação de sua qualidade.

- **Resposta:**
Os dados são oficiais da API Dados Abertos da Câmara e cobrem a atividade dos deputados federais no período de 01/01/2020 até a data da coleta. Nesta fase, a assiduidade é estimada por um proxy de presença: a contagem de participações em Sessões Deliberativas por deputado (obtidas a partir dos eventos do parlamentar). Para manter o processo leve e reprodutível, trabalhamos com metadados dos deputados e um agregado de contagens por deputado. Realizamos checagens básicas de qualidade **(unicidade de IDs, integridade de junções e coerência de tipos)** e documentamos limitações como campos opcionais ausentes em eventos e a necessidade futura de dados específicos de votações para complementar a análise.

## Coleta dos dados:
Descrição de como os dados foram adquiridos. Seu contexto, fontes, métodos de aquisição e problemas encontrados.

- **Resposta:**
A aquisição ocorre via requisições HTTP GET paginadas. Primeiro coletamos o universo de parlamentares em /deputados (com itens=100 e pagina=1..N) e, em seguida, para cada id, varremos /deputados/{id}/eventos entre dataInicio=2020-01-01 e dataFim=<hoje>, ordenando por dataHoraInicio. Em vez de salvar todos os eventos, somamos diretamente o número de ocorrências por deputado (preferencialmente filtrando descricaoTipo == "Sessão Deliberativa"), gravando apenas o agregado. Pequenos sleep entre páginas e tratamento simples de erros mitigam limites de taxa e respostas transitórias; a coleta é idempotente e pode ser retomada.

## Descrição dos dados:
Descrição de cada base de dados, incluindo cada campo, tipo de dados, unidade utilizada, códigos etc.

- **Resposta:**
Geramos dois artefatos principais. O data/processed/deputados.json contém: id (chave primária), nome, siglaPartido, siglaUf, idLegislatura, email, urlFoto, além de uri e uriPartido. O data/processed/freq_eventos.csv traz o agregado por parlamentar com id_deputado (chave estrangeira para deputados.id) e num_eventos (contagem no período, idealmente apenas de Sessões Deliberativas). A relação entre as bases é 1:N (deputado → eventos, materializada como contagem) e os tipos são simples: inteiros para IDs/contagens e texto para metadados. Como apoio sem persistência local, consultamos /referencias/deputados/codSituacao para interpretar situações de exercício quando necessário.

## Análise exploratória dos dados:
Descrição da exploração inicial dos dados, incluindo objetivos de exploração. Quais operações ou métodos foram realizados, quais padrões nos dados foram encontrados, sejam esperados ou não. Conclusões em relação aos objetivos de mineração e ao que deve ser realizado na etapa de preparação dos dados (limpeza, transformação, pré-processamento).

- **Resposta:**


## Verificação de qualidade dos dados:
Descrição das abordagens e critérios utilizados para avaliar a qualidade dos dados originais e o resultado encontrado com estas avaliações.

- **Resposta:**

---