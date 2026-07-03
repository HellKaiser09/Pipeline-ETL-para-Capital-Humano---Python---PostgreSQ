# Pipeline ETL para Datos de Capital Humano
Pipeline de Extracción, Transformación y Carga (ETL) que automatiza la limpieza y estructuración de un dataset de Recursos Humanos, cargando los datos procesados en una base de datos PostgreSQL.

## Problema que resuelve
Los datos de RH suelen llegar en formatos inconsistentes: valores nulos, registros duplicados, formatos de fecha o texto sin normalizar. Este pipeline automatiza ese proceso de limpieza y deja los datos listos para análisis o reportes, sin intervención manual repetitiva.

## Stack
- **Python 3** — lógica de extracción, transformación y carga
- **Pandas** — limpieza y manipulación de datos (nulos, duplicados, normalización de formatos)
- **PostgreSQL** — almacenamiento estructurado del resultado final
- **Docker / Docker Compose** — levanta el servicio de PostgreSQL de forma aislada y reproducible

## Estructura del proyecto

├── src/       
├ ├── extract.py  
├ ├── transform.py  
├ ├── load.py   
├ ├── main.py   
├── docker-compose.yml   # Levanta el contenedor de PostgreSQL  
├── requirements.txt  
└── .gitignore  

## Fuente de datos

Dataset público de Recursos Humanos obtenido de [Kaggle](https://www.kaggle.com/datasets/rhuebner/human-resources-data-set), descargado en formato CSV para procesamiento local.

## 🚀 Cómo ejecutarlo localmente

1. Clona el repositorio:
```bash
  git clone https://github.com/HellKaiser09/Pipeline-ETL-para-Capital-Humano---Python---PostgreSQ
  cd Pipeline-ETL-para-Capital-Humano---Python---PostgreSQ
```

2. Crea y activa un entorno virtual:
```bash
   python -m venv venv

   # En Windows
   venv\Scripts\activate

   # En macOS/Linux
   source venv/bin/activate
```

3. Instala las dependencias:
```bash
   pip install -r requirements.txt
```

4. Levanta el contenedor de PostgreSQL:
```bash
   docker-compose up -d
```

5. Ejecuta el pipeline:
```bash
   python src/main.py
```

## Pruebas visuales 

## Próximos pasos

- Programar la ejecución del pipeline de forma automática (cron / scheduler)
- Agregar pruebas unitarias para las funciones de transformación
- Documentar el esquema de la tabla destino en PostgreSQL

## Nota
Proyecto de análisis independiente con fines de portafolio, construido para practicar arquitectura ETL end-to-end.
