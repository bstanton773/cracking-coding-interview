class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.value))
            curr = curr.next
        print(" -> ".join(nodes))

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # 2.1
    def remove_duplicates(self):
        first = self.head
        prev = first
        while first:
            check = first.next
            while check:
                if check.value == first.value:
                    prev.next = check.next
                else:
                    prev = check
                check = check.next
            first = first.next
            prev = first

    # 2.2
    def return_kth_last_element(self, k):
        total = 0
        node = self.head
        while node:
            total += 1
            node = node.next
        kth_last = total - k
        node_num = 0
        node = self.head
        while node_num < kth_last:
            node = node.next
            node_num += 1
        return node

    # 2.3
    def remove(self, value):
        node = self.head
        if node.value == value:
            self.head = node.next
            return
        prev = node
        node = node.next
        while node:
            if node.value == value:
                prev.next = node.next
                return
            prev = node
            node = node.next


# 2.1 
print("2.1")
# Write code to remove duplicates from an unsorted linked list


names = LinkedList()
names.append("Brian")
names.append("Brian")
names.append("Adam")
names.append("Donovan")
names.append("Brian")
names.append("Katelyn")
names.append("Adam")
names.append("Katelyn")
names.append("Brian")
names.append("Brian")
names.append("Brian")
names.append("Donovan")
names.append("Donovan")


names.print_list()

names.remove_duplicates()

names.print_list()


print("="*50)
# 2.2
print("2.2")
# Implement an algorithm to find the kth to last element of a singly linked list.

weekdays = LinkedList()
weekdays.append('Sunday')
weekdays.append('Monday')
weekdays.append('Tuesday')
weekdays.append('Wednesday')
weekdays.append('Thursday')
weekdays.append('Friday')
weekdays.append('Saturday')

weekdays.print_list()

print(weekdays.return_kth_last_element(5))


print("="*50)
# 2.3
print("2.3")
# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

weekdays.print_list()

weekdays.remove("Wednesday")

weekdays.print_list()
