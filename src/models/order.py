from dataclasses import dataclass


@dataclass
class Order:

    order_id: str

    customer_id: str

    product_id: str

    quantity: int

    unit_price: float

    payment_method: str

    city: str

    state: str

    order_timestamp: str