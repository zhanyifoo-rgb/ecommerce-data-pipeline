import pandas as pd

def extract():
    file_path = "data/raw/Online Retail.xlsx"

    df = pd.read_excel(
        file_path,
        engine="openpyxl"
    )

    print("Original shape:", df.shape)

    # Remove rows with missing Description
    df = df.dropna(subset=["Description"])

    # Remove duplicate rows
    df = df.drop_duplicates()

    print("Cleaned shape:", df.shape)

    # Load (to processed file)
    output_path = "data/processed/online_retail_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"\nSaved cleaned data to: {output_path}")

    print("\nRemaining missing values:")
    print(df.isnull().sum())

if(__name__ == "__main__"):
    extract()