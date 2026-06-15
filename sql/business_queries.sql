-- Total Revenue
SELECT SUM(Revenue) AS TotalRevenue
FROM RetailSales;

-- Top 10 Products by Revenue
SELECT TOP 10
    Description,
    SUM(Revenue) AS Revenue
FROM RetailSales
GROUP BY Description
ORDER BY Revenue DESC;

-- Top 10 Countries by Revenue
SELECT TOP 10
    Country,
    SUM(Revenue) AS Revenue
FROM RetailSales
GROUP BY Country
ORDER BY Revenue DESC;

-- Monthly Revenue Trend
SELECT
    Year,
    Month,
    SUM(Revenue) AS TotalRevenue
FROM RetailSales
GROUP BY Year, Month
ORDER BY Year, Month;

-- Top Customers
SELECT TOP 10
    CustomerID,
    SUM(Revenue) AS Revenue
FROM RetailSales
GROUP BY CustomerID
ORDER BY Revenue DESC;
