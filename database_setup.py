import pandas as pd
from sqlalchemy import create_engine, text

# Criando a conexão com o Banco de dados do SQLite

engine = create_engine('sqlite:///logistica_db.sqlite')


def inicializar_banco():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS volumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo_carga TEXT,
                volume_m3 REAL,
                peso_kg REAL,
                data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        conn.commit()
        print("Base de dados inicializada com sucesso no WSL!!!")

if __name__ == "__main__":
    inicializar_banco()

