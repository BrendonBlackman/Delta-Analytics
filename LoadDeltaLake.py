import pandas as pd
import kagglehub
from deltalake.writer import write_deltalake
import os
import shutil

# Config
dataset = kagglehub.dataset_download("datarspectrum/retail-data-warehouse-12-table-1m-rows-dataset")
local_temp_base = r"C:\temp_delta_load" #local folder on PC
remote_base = r"Z:\Deltalake" #remote folder

# List of tables to load
tables = ["customers", "stores", "employees", "categories", "suppliers", 
    "products", "promotions", "orders", "order_items", "payments", 
    "shipments", "returns"
]

for table in tables:
    # Paths
    csv_path = os.path.join(dataset, f"{table}.csv")
    local_table_path = os.path.join(local_temp_base, table)
    remote_table_path = os.path.join(remote_base, table)
    
    # Load
    df = pd.read_csv(csv_path)
    
    print(f"Processing {table}...")
    
    # Write to local disk
    if os.path.exists(local_table_path):
        shutil.rmtree(local_table_path) # Clean start
    write_deltalake(local_table_path, df, mode="overwrite")
    
    # Move to remote folder
    print(f"Moving {table} to {remote_base}...")
    if os.path.exists(remote_table_path):
        shutil.rmtree(remote_table_path)
    shutil.move(local_table_path, remote_table_path)

print(f"All tables successfully moved to {remote_base}.")