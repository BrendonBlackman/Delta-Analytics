Retail Data Lakehouse & BI Model
🏗️ Project Overview
This project demonstrates the implementation of a modern Data Lakehouse architecture hosted on a private Proxmox infrastructure. Using the Retail Data Warehouse Dataset, I am building an end-to-end pipeline that transforms 1M+ rows of raw retail data into optimized Delta Parquet files.

The goal is to produce a sophisticated Power BI star schema capable of handling a "Galaxy" of multiple fact tables (Sales, Returns, Shipments) sharing common dimensions.

🛠️ Key Technologies
Infrastructure: Proxmox VE (Virtualization), Samba/SMB (Networked Storage).

Processing Engine: Python (pandas, deltalake).

Storage Format: Delta Lake / Parquet (Columnar storage).

Visualization: Power BI Desktop (Advanced DAX & Dimensional Modeling).

🚀 Build Progress
✅ Phase 1: Environment & Storage (Complete)
[x] Deployed dedicated Virtual Machine/Container on Proxmox.

[x] Configured a Samba share to act as the centralized Data Lake.

[x] Verified network connectivity between the processing environment and Windows BI client.

🏗️ Phase 2: ETL & Optimization (In Progress)
[ ] Scripting the ingestion of 12 relational CSV tables via Python.

[ ] Local version: generates Delta tables to a local DeltaFiles folder.

[ ] Remote version: generates Delta tables directly to the Samba share.

[ ] Converting raw files into Delta Parquet to enable predicate pushdown.

📅 Phase 3: Dimensional Modeling (Upcoming)
[ ] Architecting a Galaxy Schema in Power BI.

[ ] Linking multiple fact tables through shared dimensions (Customers, Stores, Products).

[ ] Developing DAX measures for cross-process KPIs (e.g., Return Rate vs. Shipping Lag).

📊 Data Schema
The model is built on 12 related tables representing a realistic enterprise retail environment:

Facts: orders, order_items, payments, shipments, returns.

Dimensions: customers, stores, employees, categories, suppliers, products, promotions.

💡 Why This Architecture?
By moving data from local CSVs to a Samba-hosted Parquet environment, this project simulates a professional enterprise environment where storage is decoupled from compute. This setup ensures high query performance in Power BI and allows for easy scaling as the dataset grows.
