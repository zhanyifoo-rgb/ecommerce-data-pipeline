import pandas as pd
from sqlalchemy import create_engine
import os

def load():
    file_path = "data/processed/online_retail_clean.csv"

    df = pd.read_csv(file_path)

    print("Rows loaded:", len(df))

    # Database connection
    engine = create_engine(
        f"postgresql://{os.getenv('ECOMMERCE_POSTGRES_USER')}:{os.getenv('ECOMMERCE_POSTGRES_PASSWORD')}@{os.getenv('ECOMMERCE_POSTGRES_HOST')}:{os.getenv('ECOMMERCE_POSTGRES_PORT')}/{os.getenv('ECOMMERCE_POSTGRES_DB')}"
    )   

    # Load into PostgreSQL
    df.to_sql(
        "sales",
        engine,
        if_exists="replace",
        index=False
    )


    print("Data loaded successfully!")

if(__name__ == "__main__"):
    load()