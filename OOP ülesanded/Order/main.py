from container import Container
from containeraggregator import ContainerAggregator
from order import Order
from orderaggregator import OrderAggregator
from orderitem import OrderItem


if __name__ == '__main__':
    print("Order items")

    order_item1 = OrderItem("Apple", "iPhone 11", 100, 10)
    order_item2 = OrderItem("Samsung", "Samsung Galaxy Note 10", 80, 10)
    order_item3 = OrderItem("Mööbel 24", "Laud", 300, 200)
    order_item4 = OrderItem("Apple", "iPhone 11 Pro", 200, 10)
    order_item5 = OrderItem("Mööbel 24", "Diivan", 20, 200)
    order_item6 = OrderItem("Mööbel 24", "Midagi väga suurt", 20, 400)

    print(order_item3.total_volume)  # 60000

    print("Order Aggregator")
    oa = OrderAggregator()
    oa.add_item(order_item1)
    oa.add_item(order_item2)
    oa.add_item(order_item3)
    oa.add_item(order_item4)
    oa.add_item(order_item5)
    oa.add_item(order_item6)
    print(f'Added {len(oa.order_items)}(6 is correct) order items')

    order1 = oa.aggregate_order("Apple", 350, 3000)
    order1.destination = "Tallinn"
    print(f'order1 has {len(order1.order_items)}(2 is correct) order items')

    order2 = oa.aggregate_order("Mööbel 24", 325, 64100)
    order2.destination = "Tallinn"
    print(f'order2 has {len(order2.order_items)}(2 is correct) order items')

    print(f'after orders creation, aggregator has only {len(oa.order_items)}(2 is correct) order items left.')

    print("Container Aggregator")
    ca = ContainerAggregator(70000)
    too_big_order = Order([OrderItem("Apple", "Apple Car", 10000, 300)])
    too_big_order.destination = "Somewhere"
    containers = ca.prepare_containers((order1, order2, too_big_order))
    print(f'prepare_containers produced containers to {len(containers)}(1 is correct) different destination(s)')

    try:
        containers_to_tallinn = containers['Tallinn']
        print(f'volume of the container to tallinn is {containers_to_tallinn[0].volume}(70000 is correct) cm^3')
        print(f'container to tallinn has {len(containers_to_tallinn[0].orders)}(2 is correct) orders')
    except KeyError:
        print('Container to Tallinn not found!')

    print(f'{len(ca.not_used_orders)}(1 is correct) cannot be added to containers')
