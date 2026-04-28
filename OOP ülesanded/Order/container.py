class Container:
    """Container to transport orders."""

    def __init__(self, max_volume: int, orders: list = None):
        self.max_volume = max_volume
        self.orders = orders if orders is not None else []

    @property
    def volume(self) -> int:
        return self.max_volume

    @property
    def volume_left(self) -> int:
        used = sum(order.total_volume for order in self.orders)
        return self.max_volume - used

    def try_add_order(self, order):
        if order.total_volume <= self.volume_left:
            self.orders.append(order)
            return True
        return False
