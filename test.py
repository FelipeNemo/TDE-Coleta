import pandas as pd

# Deputados
print("\n" + "=" * 80)
print("DEPUTADOS (data/processed/deputados.json)")
print("=" * 80)
deputados = pd.read_json("data/processed/deputados.json")
deputados.info()
print()

# Eventos
print("\n" + "=" * 80)
print("EVENTOS (data/processed/eventos.csv)")
print("=" * 80)
eventos = pd.read_csv("data/processed/eventos.csv")
eventos.info()
print()
print(eventos.head())
print()

# Presenças
print("\n" + "=" * 80)
print("PRESENCAS (data/processed/presencas.csv)")
print("=" * 80)
presencas = pd.read_csv("data/processed/presencas.csv")
presencas.info()
print()
print(presencas.head())
print()

# Remunerações
print("\n" + "=" * 80)
print("REMUNERACOES (data/info/remuneracoes.csv)")
print("=" * 80)
remuneracoes = pd.read_csv("data/info/remuneracoes.csv")
remuneracoes.info()
print()
print(remuneracoes.head())
print()

# Uma amostra de votações (pega só um arquivo pra entender o schema)
print("\n" + "=" * 80)
print("VOTACOES (data/processed/votacoes_2020-01.csv)")  # ajuste o nome se preciso
print("=" * 80)
votacoes_amostra = pd.read_csv("data/processed/votacoes_2020-02.csv")
votacoes_amostra.info()
print()
print(votacoes_amostra.head())
print()
