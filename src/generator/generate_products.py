from pathlib import Path
import random

import pandas as pd

REFERENCE_DIR = Path("data/reference")

products = [
    ("Laptop", "Electronics", 65000),
    ("Smartphone", "Electronics", 35000),
    ("Monitor", "Electronics", 18000),
    ("Keyboard", "Accessories", 1200),
    ("Mouse", "Accessories", 800),
    ("Headphones", "Accessories", 2500),
    ("Office Chair", "Furniture", 8500),
    ("Desk", "Furniture", 12000),
    ("Tablet", "Electronics", 28000),
    ("Power Bank", "Accessories", 1800),
    ("SSD 1TB", "Storage", 7200),
    ("USB Drive", "Storage", 700),
    ("Webcam", "Accessories", 3200),
    ("Printer", "Office", 14500),
    ("Router", "Networking", 4200),
]

records = []

for i in range(1, 501):

    product = random.choice(products)

    records.append(
        {
            "product_id": f"PROD{i:05}",
            "product_name": product[0],
            "category": product[1],
            "unit_price": round(
                product[2] * random.uniform(0.85, 1.15),
                2,
            ),
        }
    )

df = pd.DataFrame(records)

output_file = REFERENCE_DIR / "products.csv"

df.to_csv(output_file, index=False)

print(f"Created {len(df)} products")
print(output_file.resolve())