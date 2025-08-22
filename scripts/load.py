import redshift_connector
import yaml

def load_to_redshift(df, table: str, config_path: str = "config.yml"):
    """Load dataframe into Redshift by writing to CSV + COPY command."""
    import tempfile, os
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(tmp.name, index=False, header=True)
    tmp.close()

    with open(config_path) as f:
        config = yaml.safe_load(f)

    conn = redshift_connector.connect(
        host=config['redshift']['host'],
        port=config['redshift']['port'],
        database=config['redshift']['database'],
        user=config['redshift']['user'],
        password=config['redshift']['password']
    )
    cursor = conn.cursor()

    # Here we assume file already in S3. For demo, just show COPY statement.
    copy_sql = f"""COPY {config['redshift']['schema']}.{table}
    FROM 's3://{config['aws']['s3_bucket']}/{table}.csv'
    IAM_ROLE '{config['aws']['iam_role']}'
    FORMAT AS CSV IGNOREHEADER 1;"""

    print("Run this COPY in Redshift:")
    print(copy_sql)
    cursor.close()
    conn.close()
