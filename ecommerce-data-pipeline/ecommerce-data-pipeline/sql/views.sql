create or replace view vw_monthly_sales as 
SELECT
    DATE_TRUNC('month', invoicedate) AS month,
    SUM(quantity * unitprice) AS revenue,
    COUNT(DISTINCT invoiceno) AS total_orders,
    COUNT(DISTINCT customerid) AS customers,
    SUM(quantity) AS quantity_sold
FROM factsales
GROUP BY DATE_TRUNC('month', invoicedate)
ORDER BY month;

CREATE or replace VIEW vw_country_sales AS
SELECT
    d.country,
    SUM(f.quantity * f.unitprice) AS revenue,
    COUNT(DISTINCT f.invoiceno) AS orders
FROM factsales f
join dimcustomer d
on d.customerid = f.customerid
GROUP BY d.country
ORDER BY revenue DESC;

CREATE or replace VIEW vw_top_products AS
SELECT
    d.description,
    SUM(f.quantity * f.unitprice) AS revenue,
    SUM(f.quantity) AS units_sold
FROM factsales f
join dimproduct d
on d.stockcode = f.stockcode
GROUP BY d.description
ORDER BY revenue DESC;

