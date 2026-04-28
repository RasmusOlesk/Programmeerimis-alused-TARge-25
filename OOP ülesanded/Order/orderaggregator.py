from order import Order

class OrderAggregator:
    """Algorithm of aggregating orders."""

    def __init__(self):
        """Initialize order aggregator."""
        self.order_items = []

    def add_item(self, item: "OrderItem"):
        """Add order item to aggregator."""
        self.order_items.append(item)

    def aggregate_order(self, customer: str, max_items_quantity: int, max_volume: int):
        """
        Create an order for a customer.

        Items must:
        - belong to the customer
        - fit quantity limit
        - fit volume limit
        """
        items = []
        used_quantity = 0
        used_volume = 0

        remaining_items = []

        for item in self.order_items:
            if item.customer == customer:
                if (used_quantity + item.quantity <= max_items_quantity and
                        used_volume + item.total_volume <= max_volume):
                    items.append(item)
                    used_quantity += item.quantity
                    used_volume += item.total_volume
                else:
                    remaining_items.append(item)
            else:
                remaining_items.append(item)

        self.order_items = remaining_items
        return Order(items)

