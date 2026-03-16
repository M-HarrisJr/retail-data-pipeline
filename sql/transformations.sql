SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(quantity) AS total_quantity
FROM retail_sales
GROUP BY region
ORDER BY total_sales DESC;
