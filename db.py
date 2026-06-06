import psycopg2
import os
import time

def connect_db():
    for i in range(5):  # 5 попыток
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            return conn
        except:
            print("DB not ready, retry...")
            time.sleep(2)

    raise Exception("DB connection failed")