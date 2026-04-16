import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_FILE = "formatted_sales_data.csv"

# Read and combine all CSVs
csv_files = list(DATA_DIR.glob("*.csv"))
combined = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Filter to Pink Morsels only
pink = combined[combined["product"].str.lower() == "pink morsel"].copy()

# Force price to numeric, stripping "$" if present
pink["price"] = pink["price"].astype(str).str.replace("$", "", regex=False).astype(float)
pink["quantity"] = pd.to_numeric(pink["quantity"])

# Calculate sales
pink["sales"] = pink["quantity"] * pink["price"]

# Keep only the required columns, sorted by date
output = pink[["sales", "date", "region"]].sort_values("date")

output.to_csv(OUTPUT_FILE, index=False)
print(f"Done. Wrote {len(output)} rows to {OUTPUT_FILE}")
print(output.head())
print(f"\nSales dtype: {output['sales'].dtype}")  # Should say float64