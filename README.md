# ETL Pipeline with AWS Redshift

This repository demonstrates a simple **Extract–Transform–Load (ETL)** pipeline built with Python, AWS S3, and Amazon Redshift.

## Overview
1. **Extract**: Load data from CSV (local or S3).
2. **Transform**: Clean and format data with Pandas.
3. **Load**: Use Redshift `COPY` command to load data efficiently.
4. **Orchestration**: Run the full pipeline via `pipeline.py`.

## Tech Stack
- Python 3.10+
- AWS Redshift
- AWS S3
- Pandas
- redshift-connector

## Project Structure
```
etl-redshift-demo/
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
├── sql/
│   ├── create_tables.sql
│   └── upsert.sql
├── tests/
│   └── test_transform.py
├── config_example.yml
├── requirements.txt
└── README.md
```

## Quickstart
1. Clone repo & install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `config_example.yml` → `config.yml` and fill in values (S3 bucket, Redshift host, IAM role, etc).

3. Run the pipeline:
   ```bash
   python scripts/pipeline.py
   ```

## Example Redshift SQL
After loading, you can query your Redshift cluster:
```sql
SELECT COUNT(*) FROM demo_table;
```

---
**License:** MIT
