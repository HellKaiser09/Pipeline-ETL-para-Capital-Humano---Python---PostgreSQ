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

## Cómo ejecutarlo localmente

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
  ### Ejecucion de main.py 
  <img width="1738" height="952" alt="image" src="https://github.com/user-attachments/assets/fcaace9b-723d-4b99-a14d-5d5f8ea6e9b9" />  
  
  ### Muestra de tabla en la DB  
  
  ```text
hr_analytics=# SELECT * FROM empleados_activos LIMIT 10;
     Employee_Name     | EmpID | MarriedID | MaritalStatusID | GenderID | EmpStatusID | DeptID | PerfScoreID | FromDiversityJobFairID | Salary | Termd | PositionID |         Position         | State | Zip  |         DOB         | Sex | MaritalDesc | CitizenDesc | HispanicLatino |         RaceDesc          |     DateofHire      |  DateofTermination  |    TermReason     |    EmploymentStatus    |      Department      |   ManagerName   | ManagerID | RecruitmentSource  | PerformanceScore | EngagementSurvey | EmpSatisfaction | SpecialProjectsCount | LastPerformanceReview_Date | DaysLateLast30 | Absences
-----------------------+-------+-----------+-----------------+----------+-------------+--------+-------------+------------------------+--------+-------+------------+--------------------------+-------+------+---------------------+-----+-------------+-------------+----------------+---------------------------+---------------------+---------------------+-------------------+------------------------+----------------------+-----------------+-----------+--------------------+------------------+------------------+-----------------+----------------------+----------------------------+----------------+----------
 Adinolfi, Wilson  K   | 10026 |         0 |               0 |        1 |           1 |      5 |           4 |                      0 |  62506 |     0 |         19 | Production Technician I  | MA    | 1960 | 1983-07-10 00:00:00 | M   | Single      | US Citizen  | No             | White                     | 2011-07-05 00:00:00 |                     | N/A-StillEmployed | Active                 | Production           | Michael Albert  |        22 | LinkedIn           | Exceeds          |              4.6 |               5 |                    0 | 2019-01-17 00:00:00        |              0 |        1
 Ait Sidi, Karthikeyan | 10084 |         1 |               1 |        1 |           5 |      3 |           3 |                      0 | 104437 |     1 |         27 | Sr. Dba                  | MA    | 2148 | 1975-05-05 00:00:00 | M   | Married     | US Citizen  | No             | White                     | 2015-03-30 00:00:00 | 2016-06-16 00:00:00 | career change     | Voluntarily Terminated | It/Is                | Simon Roup      |         4 | Indeed             | Fully Meets      |             4.96 |               3 |                    6 | 2016-02-24 00:00:00        |              0 |       17
 Akinkuolie, Sarah     | 10196 |         1 |               1 |        0 |           5 |      5 |           3 |                      0 |  64955 |     1 |         20 | Production Technician Ii | MA    | 1810 | 1988-09-19 00:00:00 | F   | Married     | US Citizen  | No             | White                     | 2011-07-05 00:00:00 | 2012-09-24 00:00:00 | hours             | Voluntarily Terminated | Production           | Kissy Sullivan  |        20 | LinkedIn           | Fully Meets      |             3.02 |               3 |                    0 | 2012-05-15 00:00:00        |              0 |        3
 Alagbe,Trina          | 10088 |         1 |               1 |        0 |           1 |      5 |           3 |                      0 |  64991 |     0 |         19 | Production Technician I  | MA    | 1886 | 1988-09-27 00:00:00 | F   | Married     | US Citizen  | No             | White                     | 2008-01-07 00:00:00 |                     | N/A-StillEmployed | Active                 | Production           | Elijiah Gray    |        16 | Indeed             | Fully Meets      |             4.84 |               5 |                    0 | 2019-01-03 00:00:00        |              0 |       15
 Anderson, Carol       | 10069 |         0 |               2 |        0 |           5 |      5 |           3 |                      0 |  50825 |     1 |         19 | Production Technician I  | MA    | 2169 | 1989-09-08 00:00:00 | F   | Divorced    | US Citizen  | No             | White                     | 2011-07-11 00:00:00 | 2016-09-06 00:00:00 | return to school  | Voluntarily Terminated | Production           | Webster Butler  |        39 | Google Search      | Fully Meets      |                5 |               4 |                    0 | 2016-02-01 00:00:00        |              0 |        2
 Anderson, Linda       | 10002 |         0 |               0 |        0 |           1 |      5 |           4 |                      0 |  57568 |     0 |         19 | Production Technician I  | MA    | 1844 | 1977-05-22 00:00:00 | F   | Single      | US Citizen  | No             | White                     | 2012-01-09 00:00:00 |                     | N/A-StillEmployed | Active                 | Production           | Amy Dunn        |        11 | LinkedIn           | Exceeds          |                5 |               5 |                    0 | 2019-01-07 00:00:00        |              0 |       15
 Andreola, Colby       | 10194 |         0 |               0 |        0 |           1 |      4 |           3 |                      0 |  95660 |     0 |         24 | Software Engineer        | MA    | 2110 | 1979-05-24 00:00:00 | F   | Single      | US Citizen  | No             | White                     | 2014-11-10 00:00:00 |                     | N/A-StillEmployed | Active                 | Software Engineering | Alex Sweetwater |        10 | LinkedIn           | Fully Meets      |             3.04 |               3 |                    4 | 2019-01-02 00:00:00        |              0 |       19
 Athwal, Sam           | 10062 |         0 |               4 |        1 |           1 |      5 |           3 |                      0 |  59365 |     0 |         19 | Production Technician I  | MA    | 2199 | 1983-02-18 00:00:00 | M   | Widowed     | US Citizen  | No             | White                     | 2013-09-30 00:00:00 |                     | N/A-StillEmployed | Active                 | Production           | Ketsia Liebig   |        19 | Employee Referral  | Fully Meets      |                5 |               4 |                    0 | 2019-02-25 00:00:00        |              0 |       19
 Bachiochi, Linda      | 10114 |         0 |               0 |        0 |           3 |      5 |           3 |                      1 |  47837 |     0 |         19 | Production Technician I  | MA    | 1902 | 1970-02-11 00:00:00 | F   | Single      | US Citizen  | No             | Black or African American | 2009-07-06 00:00:00 |                     | N/A-StillEmployed | Active                 | Production           | Brannon Miller  |        12 | Diversity Job Fair | Fully Meets      |             4.46 |               3 |                    0 | 2019-01-25 00:00:00        |              0 |        4
 Bacong, Alejandro     | 10250 |         0 |               2 |        1 |           1 |      3 |           3 |                      0 |  50178 |     0 |         14 | It Support               | MA    | 1886 | 1988-01-07 00:00:00 | M   | Divorced    | US Citizen  | No             | White                     | 2015-01-05 00:00:00 |                     | N/A-StillEmployed | Active                 | It/Is                | Peter Monroe    |         7 | Indeed             | Fully Meets      |                5 |               5 |                    6 | 2019-02-18 00:00:00        |              0 |       16
(10 rows
  ```
## Próximos pasos

- Programar la ejecución del pipeline de forma automática (cron / scheduler)
- Agregar pruebas unitarias para las funciones de transformación
- Documentar el esquema de la tabla destino en PostgreSQL

## Nota
Proyecto de análisis independiente con fines de portafolio, construido para practicar arquitectura ETL end-to-end.
