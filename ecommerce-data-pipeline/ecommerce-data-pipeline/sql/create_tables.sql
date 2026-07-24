Create Table DimCustomer(
    CustomerID INT PRIMARY KEY,
    Country VARCHAR(100)
);

Create Table DimProduct(
    StockCode VARCHAR(50) PRIMARY KEY,
    Description VARCHAR(255)
);

Create Table FactSales(
    SalesID SERIAL PRIMARY KEY,
    InvoiceNo VARCHAR(20),
    CustomerID INT,
    StockCode VARCHAR(50),
    InvoiceDate DATE,
    Quantity INT,
    UnitPrice decimal(10,2),
    FOREIGN KEY (CustomerID)
        REFERENCES DimCustomer(CustomerID),

    FOREIGN KEY (StockCode)
        REFERENCES DimProduct(StockCode)
);