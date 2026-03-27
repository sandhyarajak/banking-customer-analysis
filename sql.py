import pandas as pd
import mysql.connector

Conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root"
)

query= "SELECT * FROM banking_case.banking"
df=pd.read_sql(query,Conn)
print(df)
Conn.close()
print(df.head(5))