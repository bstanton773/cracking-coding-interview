class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.value))
            curr = curr.next
        print(" -> ".join(nodes))

    def reorder_alternating(self):
        if not self.head or not self.head.next:
            return

        # Step 1: Find the midpoint (slow ends at the last 'a' node)
        slow = self.head
        fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split into two halves
        first = self.head
        second = slow
        prev.next = None  # Terminate first half

        # Step 3: Interleave the two halves
        dummy = Node(0)
        curr = dummy

        while first and second:
            curr.next = first
            first = first.next
            curr = curr.next

            curr.next = second
            second = second.next
            curr = curr.next

        self.head = dummy.next


# Example usage:
ll = LinkedList()

# Fill with a1, a2, a3, b1, b2, b3
values = ["a1", "a2", "a3", "b1", "b2", "b3"]
for val in values:
    ll.append(val)

print("Original list:")
ll.print_list()

ll.reorder_alternating()

print("\nReordered list:")
ll.print_list()
