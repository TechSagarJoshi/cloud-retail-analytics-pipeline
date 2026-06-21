**## Cloud Retail Analytics Pipeline**

**## Project Overview**

This project demonstrates an end-to-end retail analytics pipeline built using Microsoft Azure services and Databricks.

The pipeline processes more than 500,000 retail transactions, performs data cleaning and transformation using PySpark, stores processed data in Azure services, and prepares datasets for business intelligence reporting in Power BI.

+------------------+
| Online Retail CSV|
+------------------+
          |
          v
+------------------+
| Azure Blob Store |
+------------------+
          |
          v
+------------------+
| Azure Databricks |
|    PySpark ETL   |
+------------------+
          |
          v
+------------------+
| Azure SQL DB     |
+------------------+
          |
          v
+------------------+
| Power BI         |
| Dashboard        |
+------------------+

**## Tech Stack**

- Azure Databricks
- PySpark
- Azure SQL Database
- Unity Catalog
- Azure Cloud
- SQL
- Power BI

**## Architecture**

Online Retail Dataset
        ↓
Azure Storage / Unity Catalog
        ↓
Azure Databricks (PySpark ETL)
        ↓
Azure SQL Database
        ↓
Power BI Dashboard

**## Dataset**

Online Retail Dataset

Records: 525,936+

**## Data Engineering Tasks**

- Data ingestion
- Data cleaning
- Duplicate removal
- Revenue calculation
- Date transformations
- Monthly sales analysis
- Country sales analysis
- Product sales analysis

**## Key Features**

- Built scalable ETL pipeline using PySpark
- Created business metrics and KPIs
- Performed sales aggregation analysis
- Prepared analytical datasets for reporting
- Integrated Azure cloud services

**## Author**

Sagar Joshi
