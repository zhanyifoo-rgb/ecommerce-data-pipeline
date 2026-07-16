import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(
    f"postgresql://{os.getenv('ECOMMERCE_POSTGRES_USER')}:{os.getenv('ECOMMERCE_POSTGRES_PASSWORD')}@{os.getenv('ECOMMERCE_POSTGRES_HOST')}:{os.getenv('ECOMMERCE_POSTGRES_PORT')}/{os.getenv('ECOMMERCE_POSTGRES_DB')}"
)

# Read customer data from sales table
customerssql = """
    SELECT DISTINCT
        "CustomerID":: INT as customerid,
        MAX("Country") as country
    FROM sales
    WHERE "CustomerID" IS NOT NULL
    group by "CustomerID"
    """
customerstable = "dimcustomer"

productssql = """
    SELECT DISTINCT
        "StockCode" as stockcode,
        MAX("Description") as description
    FROM sales
    WHERE "StockCode" IS NOT NULL
    group by "StockCode"
    """
productstable = "dimproduct"

factsalessql = """
    SELECT 
        "InvoiceNo" as invoiceno,
        "CustomerID"::INT as customerid,
        "StockCode" as stockcode,
        "InvoiceDate"::Date as invoicedate,
        "Quantity"::INT as quantity,
        "UnitPrice"::Decimal(10,2) as unitprice
    FROM sales
    WHERE "StockCode" IS NOT NULL AND "CustomerID" IS NOT NULL
    """
factsalestable = "factsales"


def read_sql(sql):
    df = pd.read_sql(
    sql,
    engine
    )

    print(df.head())
    print("length of df:", len(df))

    return df

def to_sql(TableName,dataframe):
    try:
        dataframe.to_sql(
        TableName,
        engine,
        if_exists="replace",
        index=False
        )
        print(f"{TableName} loaded")
    except Exception as e:
        print(f"{TableName} is not loaded, {e}")

def load_dimensions():
    customers = read_sql(customerssql)
    customers["customerid"] = customers["customerid"].astype(int)
    to_sql(customerstable,customers)

    products = read_sql(productssql)
    to_sql(productstable,products)

    factsales = read_sql(factsalessql)
    to_sql(factsalestable,factsales)


if(__name__ == "__main__"):
    load_dimensions()



