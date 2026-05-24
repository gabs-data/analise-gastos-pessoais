import sqlite3
import pandas as pd

# =========================================
# CONECTAR AO BANCO
# =========================================

conn = sqlite3.connect('gastos.db')

# =========================================
# LER TABELA
# =========================================

query = "SELECT * FROM gastos"

df = pd.read_sql_query(query, conn)

print("\nTabela completa:")
print(df)

# =========================================
# GASTOS POR CATEGORIA
# =========================================

query_categoria = """
SELECT categoria,
       SUM(valor) AS total
FROM gastos
GROUP BY categoria
ORDER BY total DESC
"""

df_categoria = pd.read_sql_query(query_categoria, conn)

print("\nGastos por categoria:")
print(df_categoria)

# =========================================
# GASTOS POR MÊS
# =========================================

query_mes = """
SELECT strftime('%Y-%m', data) AS mes,
       SUM(valor) AS total
FROM gastos
GROUP BY mes
ORDER BY mes
"""

df_mes = pd.read_sql_query(query_mes, conn)

print("\nGastos por mês:")
print(df_mes)

# =========================================
# TOP 3 MAIORES GASTOS
# =========================================

query_top = """
SELECT *
FROM gastos
ORDER BY valor DESC
LIMIT 3
"""

df_top = pd.read_sql_query(query_top, conn)

print("\nTop 3 maiores gastos:")
print(df_top)

# =========================================
# INSIGHTS
# =========================================

maior_categoria = df_categoria.iloc[0]

print("\nINSIGHTS:")
print(f"Categoria com maior gasto: {maior_categoria['categoria']}")
print(f"Total gasto: R$ {maior_categoria['total']:.2f}")

# =========================================
# FECHAR CONEXÃO
# =========================================

conn.close()