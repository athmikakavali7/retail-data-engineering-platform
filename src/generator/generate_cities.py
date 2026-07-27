print("Script started")

from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("data/reference")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Output directory:", OUTPUT_DIR.resolve())

cities = [
    ("Bengaluru", "Karnataka"),
    ("Mysuru", "Karnataka"),
]

df = pd.DataFrame(cities, columns=["city", "state"])

output_file = OUTPUT_DIR / "cities.csv"

print("Writing to:", output_file.resolve())

df.to_csv(output_file, index=False)

print("Done")