# Databricks notebook source
catalog = "devopsworkflow_practice"
schema = "bronze"
table = "sales_transaction_v_4_a"

# Caminho da tabela
table_path = f"{catalog}.{schema}.{table}"
df = spark.table(table_path)

df.show()
