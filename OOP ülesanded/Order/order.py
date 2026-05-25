class Order:
    """Combination of order items of one customer."""

    def __init__(self, order_items: list):
        """Initialize order with given items."""
        self.order_items = order_items
        self.destination = None

    @property
    def total_quantity(self) -> int:
        """Return total quantity of all items."""
        return sum(item.quantity for item in self.order_items)

    @property
    def total_volume(self) -> int:
        """Return total volume of all items."""
        return sum(item.total_volume for item in self.order_items)