from pathlib import Path
from random import choice

import pandas as pd
from faker import Faker

fake = Faker("en_IN")

REFERENCE_DIR = Path("data/reference")

cities = pd.read_csv(REFERENCE_DIR / "cities.csv")

customers = []

NUMBER_OF_CUSTOMERS = 1000

for i in range(1, NUMBER_OF_CUSTOMERS + 1):

    city = cities.sample(1).iloc[0]

    customers.append(
        {
            "customer_id": f"CUS{i:06}",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "city": city["city"],
            "state": city["state"],
            "registration_date": fake.date_between(
                start_date="-3y",
                end_date="today",
            ),
        }
    )

df = pd.DataFrame(customers)

output_file = REFERENCE_DIR / "customers.csv"

df.to_csv(output_file, index=False)

print(f"Created {len(df)} customers")
print(output_file.resolve())