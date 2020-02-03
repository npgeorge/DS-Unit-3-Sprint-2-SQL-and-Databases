import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv() # looks inside the .env file for some env vars

# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

connection = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cursor = connection.cursor()

#
#
#

print("------------")

table_name = "titanic"
insertion_query = f"INSERT INTO {table_name} (id, survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare) VALUES %s"

engine = create_engine('sqlite://', echo=False)
df = pd.read_csv('titanic.csv')
df.to_sql('users', con=engine)
insert_titanic = engine.execute("SELECT * FROM users").fetchall()
execute_values(cursor, insertion_query, insert_titanic)
#
#
#

print("------------")

query = """
SELECT * from titanic;
"""
print(query)
cursor.execute(query)

#results = cursor.fetchone()
results = cursor.fetchall()

print(results)
for row in results:
    print(row)

#committing the transaction
#this update the database in TablePlus (or SQL gui)
connection.commit()
