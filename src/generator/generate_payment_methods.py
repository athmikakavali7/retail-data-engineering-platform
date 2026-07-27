from pathlib import Path

import pandas as pd

REFERENCE_DIR = Path("data/reference")

methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery",
    "Wallet",
]

df = pd.DataFrame({"payment_method": methods})

output_file = REFERENCE_DIR / "payment_methods.csv"

df.to_csv(output_file, index=False)

print(output_file.resolve())