import logging

import pandas as pd


def hr_transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica reglas de negocio para limpiar y normalizar el dataframe de RRHH.
    """
    logging.info("Iniciando la transformacion de datos::::.")

    df_clean = df.copy()

    try:
        logging.info("Iniciamos la estandarizacion de columnas de texto:::::.")
        cols_to_strip = ["Employee_Name", "Department", "Position", "ManagerName"]
        for col in cols_to_strip:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].astype(str).str.strip().str.title()

        logging.info("Estandarizacion de columnas de texto completada.")
        logging.info("Convirtiendeo formatos de fechas :::::::.")
        if "DOB" in df_clean.columns:
            df_clean['DOB'] = pd.to_datetime(df_clean['DOB'], format='%m/%d/%y', errors='coerce')
        
        date_cols_4_digits = [
            "DateofHire",
            "DateofTermination",
            "LastPerformanceReview_Date",
        ]
        for col in date_cols_4_digits:
            if col in df_clean.columns:
                # errors='coerce' convierte fechas inválidas o nulos en NaT (Not a Time)
                df_clean[col] = pd.to_datetime(df_clean[col], format='%m/%d/%Y', errors='coerce')
        logging.info("Conversión de formatos de fechas completada.")

        logging.info("Validando reglas de negocio para valores nulos::::::.")
        df_clean["TermReason"] = df_clean["TermReason"].fillna("Not Applicable")
        # Eliminamos la columna de ManagerID si tiene demasiados nulos inexplicables o la rellenamos con -1 (opcional, en este caso la dejaremos intacta para la DB)

        logging.info(
            f"Transformación exitosa. DataFrame listo: {df_clean.shape[0]} filas."
        )
        return df_clean

    except Exception as e:
        logging.error(f"Error crítico durante la transformación: {e}")
        raise
