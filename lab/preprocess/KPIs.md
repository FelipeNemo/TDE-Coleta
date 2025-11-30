# Preparação dos Dados
Nesta seção, as atividades realizadas para a construção do dataset final devem ser descritas, como limpeza, criação de atributos, inserção de registros, integração de bases etc. Ao final, uma descrição do estado do dataset que será utilizado para a modelagem deve ser realizada.

### Limpeza dos dados
Os dados passaram por etapas de filtragem e remoção de duplicidades, especialmente nos registros de presenças e eventos. Foram selecionados apenas eventos do tipo "Sessão Deliberativa" e removidos registros duplicados de presenças por deputado e evento. Também foi realizada a verificação de valores ausentes (NA) nos dataframes resultantes, utilizando visualização com heatmap para identificar possíveis problemas de integridade.

### Criação de atributos e registros
Foram criados atributos como a flag de presença (0/1) para cada deputado em cada sessão, a contagem de presenças por deputado e o cálculo da taxa de presença (razão entre presenças e total de sessões deliberativas). Além disso, foi criado um rótulo descritivo para cada deputado, combinando nome, partido e UF. Novos dataframes foram gerados para consolidar essas informações, como o dataframe final de presença por deputado.

### Integração de dados
Os dados foram integrados a partir de diferentes fontes: deputados (JSON), eventos (CSV) e presenças (CSV). A integração foi feita por meio de merges utilizando chaves como id_deputado e id_evento. As features aproveitadas incluem nome, partido, UF, além das métricas calculadas de presença. Redundâncias foram tratadas por meio da remoção de duplicatas e seleção de colunas relevantes. O resultado é um dataset consolidado, pronto para análises e modelagem, salvo em CSV para uso posterior.
