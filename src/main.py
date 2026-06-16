import os

from extrack import hr_extract_data
from transform import hr_transform_data
from load import load_data_to_postgres

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "HRDataset_v14.csv")
TABLE_NAME = 'empleados_activos'


def main():

    print("PRUEBAS DEL PIPELINE ETL ")

    # EXTRACCION
    df_raw = hr_extract_data(DATA_PATH)
    print("\n Vistazo rápido a los datos extraídos:")
    print(df_raw.head())

    df_clean = hr_transform_data(df_raw)
    print("\n✅ Departamentos sin espacios extra:")
    print(df_clean["Department"].unique())

    print("\n✅ Tipos de datos actualizados (Fechas reales):")
    print(df_clean[["DOB", "DateofHire"]].dtypes)

    print("\n✅ Validación de reglas de negocio completada:")

    load_data_to_postgres(df_clean, TABLE_NAME)
    print("\n✅ El pipeline terminó de ejecutarse exitosamente.")


if __name__ == "__main__":
    main()
