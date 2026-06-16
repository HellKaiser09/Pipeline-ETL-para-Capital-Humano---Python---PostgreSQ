import logging
import os

import pandas as pd

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def hr_extract_data(file_path) -> pd.DataFrame:
    """
    Extraemos los datos del csv que son los datos crudo para pasarlo a un dataframe en pandas

    Args:
        file_path (str): La ruta relativa o absoluta al archivo CSV.

    Returns:
        pd.DataFrame: Un dataframe de Pandas con los datos en bruto.
    """
    logging.info(f"Se inicio la extraccion de datos desde: {file_path} ::::::::::.")

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No se encontro el archivo en: {file_path}")
        df = pd.read_csv(file_path)

        logging.info(
            f"Extraccion completada: Se extrajeron {df.shape[0]} filas y {df.shape[1]} columnnas {len(df)} registros desde: {file_path}"
        )
        return df
    except pd.errors.EmptyDataError:
        logging.error(f"El archivo {file_path} esta vacio")
        raise
    except Exception as e:
        logging.error(f"Error crítico durante la extracción: {e}")
        raise
