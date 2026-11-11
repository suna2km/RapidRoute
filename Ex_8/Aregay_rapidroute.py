class PackageNode:
    def __init__(self, package_id: str, address: str, weight: float):
        self.package_id = package_id
        self.address = address
        self.weight = weight
        self.next = None

class PackageSLL:
    def __init__(self):
        self.head = None

    def add_package(self, package_id: str, address: str, weight: float):
        new_package = PackageNode(package_id, address, weight)
        if self.head is None:
            self.head = new_package
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_package

    def display_packages(self):
        current = self.head
        while current:
            print(f"Package ID: {current.package_id}, Address: {current.address}, Weight: {current.weight}", end=" -> ")
            current = current.next
        print("None")

    def remove_last_package(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None


class StopNode:
    def __init__(self, address:str, name:str, time:str):
        self.address = address
        self.name = name
        self.time = time
        self.next = None
        self.prev = None

class DeliveryRouteDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_stop(self, address: str, name: str, time: str):
        new_node = StopNode(address, name, time)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node   
        self.tail = new_node

    def traverse_forward(self):
        current = self.head
        while current:
            print(f"Address: {current.address}, Name: {current.name}, Time: {current.time}")
            current = current.next
        print("End of route.")

    def traverse_backward(self):
        current = self.tail
        if current is None:
            print("No stops in the route.")
            return
        while current:
            print(f"Address: {current.address}, Name: {current.name}, Time: {current.time}")
            current = current.prev
        print("Start of route.")    

    def add_stop_at_beginning(self, address: str, name: str, time: str):
        new_node = StopNode(address, name, time)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node             

class ScheduleNode:    
    def __init__(self, day:str, route:str, time:str):
        self.day = day
        self.route = route
        self.time = time
        self.next = None

class DeliveryScheduleCLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_delivery(self, day: str, route: str, time: str):
        new_node = ScheduleNode(day, route, time)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return
        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node   

    def traverse_schedule(self, schedules: int):
        if self.head is None:
            print("No deliveries scheduled.")
            return
        current = self.head
        for schedule in range(1, schedules + 1):
            print(f"Schedule {schedule} [ Day: {current.day}, Route: {current.route}, Time: {current.time} ]")
            current = current.next

    def add_delivery_at_beginning(self, day: str, route: str, time: str):
        new_node = ScheduleNode(day, route, time)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

if __name__ == "__main__":

    print("RAPIDROUTE DELIVERY SERVICE")
    print("SINGLY LINKED LIST: Package Processing")
    package_list = PackageSLL()
    package_list.add_package(1, "123 Main St", 5.0)
    package_list.add_package(2, "456 Elm St", 10.0)
    package_list.add_package(3, "789 Oak St", 15.0)
    package_list.add_package(4, "101 Pine St", 20.0)
    package_list.add_package(5, "202 Maple St", 25.0)

    print("Packages in the list:")
    package_list.display_packages()

    package_list.remove_last_package()
    print("\nAfter removing the last package:")
    package_list.display_packages()

    route = DeliveryRouteDLL()
    route.add_stop("123 Main St", "Jane Doe", "09:00")
    route.add_stop("456 Elm St", "John Smith", "10:00")
    route.add_stop("789 Oak St", "Alice Johnson", "11:00")
    route.add_stop("101 Pine St", "Bob Wilson", "12:00")

    print("\nDOUBLY LINKED LIST: Delivery Route (Forward):")   
    route.traverse_forward()    

    print("\nDOUBLY LINKED LIST: Delivery Route (Backward):")
    route.traverse_backward()

    route.add_stop_at_beginning("202 Maple St", "Charlie Brown", "08:00")
    print("\nAfter adding a stop at the beginning:")
    route.traverse_forward()

    schedule = DeliveryScheduleCLL()
    schedule.add_delivery("Monday", "Route 1", "09:00")
    schedule.add_delivery("Tuesday", "Route 2", "10:00")
    schedule.add_delivery("Wednesday", "Route 3", "11:00")
    schedule.add_delivery("Thursday", "Route 4", "12:00")

    print("\nCIRCULAR LINKED LIST: Delivery Schedule:")
    schedule.traverse_schedule(6)

    schedule.add_delivery_at_beginning("Sunday", "Route 0", "08:00")
    print("\nAfter adding a delivery schedule at the beginning:")
    schedule.traverse_schedule(7)