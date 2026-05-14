import pandas as pd
import kagglehub
from deltalake.writer import write_deltalake
import os
import shutil

# Config
dataset = kagglehub.dataset_download("datarspectrum/retail-data-warehouse-12-table-1m-rows-dataset")
delta_base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "DeltaFiles")

# List of tables to load
tables = ["customers", "stores", "employees", "categories", "suppliers", 
    "products", "promotions", "orders", "order_items", "payments", 
    "shipments", "returns"
]

for table in tables:
    csv_path = os.path.join(dataset, f"{table}.csv")
    table_path = os.path.join(delta_base, table)
    
    df = pd.read_csv(csv_path)
    print(f"Processing {table}...")
    
    if os.path.exists(table_path):
        shutil.rmtree(table_path)
    write_deltalake(table_path, df, mode="overwrite")

print(f"All tables written to {delta_base}.")