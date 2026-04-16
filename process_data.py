import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_FILE = "formatted_sales_data.csv"

# Read and combine all CSVs in the data folder
csv_files = list(DATA_DIR.glob("*.csv"))
combined = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Keep only Pink Morsel rows (case-insensitive just in case)
pink_morsels = combined[combined["product"].str.lower() == "pink morsel"].copy()

# Calculate sales = quantity * price
# If price has a "$" sign, strip it first
if pink_morsels["price"].dtype == object:
    pink_morsels["price"] = pink_morsels["price"].str.replace("$", "", regex=False).astype(float)

pink_morsels["sales"] = pink_morsels["quantity"] * pink_morsels["price"]

# Keep only the three required columns
output = pink_morsels[["sales", "date", "region"]]

# Sort by date so the output is tidy
output = output.sort_values("date")

# Write to CSV
output.to_csv(OUTPUT_FILE, index=False)

print(f"Done. Wrote {len(output)} rows to {OUTPUT_FILE}")