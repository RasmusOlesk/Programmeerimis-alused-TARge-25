from container import Container

class ContainerAggregator:
    """Algorithm to prepare containers."""

    def __init__(self, container_volume: int):
        """Initialize container aggregator."""
        self.container_volume = container_volume
        self.not_used_orders = []

    def prepare_containers(self, orders: tuple) -> dict:
        """
        Create containers and put orders into them.

        Group by destination.
        """
        result = {}

        for order in orders:
            # Too big to fit in any container
            if order.total_volume > self.container_volume:
                self.not_used_orders.append(order)
                continue

            dest = order.destination
            if dest not in result:
                result[dest] = [Container(self.container_volume)]

            placed = False
            for container in result[dest]:
                if container.try_add_order(order):
                    placed = True
                    break

            if not placed:
                new_container = Container(self.container_volume)
                new_container.try_add_order(order)
                result[dest].append(new_container)

        return result