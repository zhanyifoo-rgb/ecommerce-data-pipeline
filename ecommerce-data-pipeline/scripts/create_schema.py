from sqlalchemy import text, create_engine
import os

def create_schema():
    file_path = "sql/create_tables.sql"

    # Database connection
    engine = create_engine(
        f"postgresql://{os.getenv('ECOMMERCE_POSTGRES_USER')}:{os.getenv('ECOMMERCE_POSTGRES_PASSWORD')}@{os.getenv('ECOMMERCE_POSTGRES_HOST')}:{os.getenv('ECOMMERCE_POSTGRES_PORT')}/{os.getenv('ECOMMERCE_POSTGRES_DB')}"
    )  

    with engine.begin() as conn:
        with open(file_path, "r") as file:
            sql = file.read()

        conn.execute(text(sql))


    print("Schema created successfully!")

if(__name__ == "__main__"):
    create_schema()