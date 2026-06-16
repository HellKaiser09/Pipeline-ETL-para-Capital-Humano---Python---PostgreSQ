import os
import pandas as pd
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_data_to_postgres(df: pd.DataFrame, table_name: str) -> None:
    """
        Carga un DataFrame de Pandas hacia una base de datos PostgreSQL.
    """
    logging.info("Iniciando fase de carga de datos hacia la base de datos ::::::::")

    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    try:
        #3. Crear el "Motor" (Engine) de conexión usando SQLAlchemy
        logging.info(f"conectando a la base de datos: {db_name} en {db_host}....")
        engine = create_engine(db_url)
        # 4. Inyectar los datos a la base de datos
        # if_exists='replace' borra la tabla si ya existe y la vuelve a crear.
        # En producción se suele usar 'append' con lógicas de actualización.
        logging.info(f"Escribiendo {df.shape[0]} registros en la tabla '{table_name}'...")
        df.to_sql(name = table_name, con = engine, if_exists = "replace", index = False)
        logging.info("Carga finalizada exitosamente.")

    except Exception as e:
        logging.error(f"Error crítico al conectar o escribir en la base de datos: {e}")
        raise
