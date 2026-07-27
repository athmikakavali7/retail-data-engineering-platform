from datetime import UTC, datetime
from pathlib import Path
import random

import pandas as pd


REFERENCE_DIR = Path("data/reference")


class RetailOrderGenerator:
    """
    Generates realistic retail order events from reference datasets.
    """

    def __init__(self):

        self.customers = self._load_csv("customers.csv")
        self.products = self._load_csv("products.csv")
        self.payment_methods = self._load_csv("payment_methods.csv")

        self.order_number = 1

    def _load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load a reference CSV file.
        """

        file_path = REFERENCE_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found in {REFERENCE_DIR}")

        return pd.read_csv(file_path)

    def generate_order(self) -> dict:
        """
        Generate one retail order.
        """

        customer = self.customers.sample(n=1).iloc[0]
        product = self.products.sample(n=1).iloc[0]
        payment = self.payment_methods.sample(n=1).iloc[0]

        quantity = random.randint(1, 5)

        unit_price = float(product["unit_price"])

        total_amount = round(quantity * unit_price, 2)

        order_id = f"ORD{self.order_number:08}"

        self.order_number += 1

        return {
            "order_id": order_id,
            "customer_id": customer["customer_id"],
            "customer_name": f"{customer['first_name']} {customer['last_name']}",
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "category": product["category"],
            "quantity": quantity,
            "unit_price": unit_price,
            "total_amount": total_amount,
            "payment_method": payment["payment_method"],
            "city": customer["city"],
            "state": customer["state"],
            "order_timestamp": datetime.now(UTC).isoformat(),
        }