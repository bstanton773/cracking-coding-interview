
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
#     def __str__(self):
#         return str(self.value)
    
#     def __repr__(self):
#         return f"<Node|{self.value}>"

    
# class LinkedList:
#     def __init__(self, head_node=None):
#         # set the .head attribute to point to the first Node in the Linked List
#         self.head = head_node
        
#     # Method to add a new node to the beginning of the Linked List
#     def push(self, new_value): # O(1) - Constant Time
#         # Create a new node with the value passed in
#         new_node = Node(new_value)
#         # Set the new_node's .next attribute to be the current head
#         new_node.next = self.head
#         # Set the head of the linked list to be the new node
#         self.head = new_node
        
#     # Method to print out all of the nodes in the linked list in order
#     def print_list(self):
#         # Start at the beginning of the list
#         node = self.head
#         # While the node is a node (and not None), continue to loop
#         while node is not None:
#             # Print the node (which will call the Node __str__ method)
#             print(node)
#             # Move on to the next node in the list
#             node = node.next
            
#     # Method to add a new node to the end of the linked list
#     def append(self, new_value): # O(n) - Linear Time
#         # Create a new node with the value passed in
#         new_node = Node(new_value)
#         # Check if the linked list is empty
#         if self.head is None:
#             # If so, set the .head attribute to the new node
#             self.head = new_node
#         # If not empty
#         else:
#             # Traverse to the end of the list
#             node = self.head
#             while node.next is not None:
#                 # move on to the next node
#                 node = node.next
#             # once node.next is None, set that node's .next to be the new node
#             node.next = new_node
            
#     # Method to get a node by value or return None if not in the Linked List
#     def get_node(self, value_to_get):
#         # Start with the beginning 
#         node_to_check = self.head
#         # While node_to_check is a node
#         while node_to_check is not None:
#             # Check if that is the node that we are looking for
#             if node_to_check.value == value_to_get:
#                 # We found it
#                 return node_to_check
#             # if not
#             node_to_check = node_to_check.next
#         # If the node_to_check becomes None, we know the value is not in the Linked List
#         return None
    
#     # Method to insert a new node in the linked list after a certain node (by value)
#     def insert_after(self, prev_value, new_value):
#         # Get the previous node by value
#         prev_node = self.get_node(prev_value)
#         # Make sure the node exists
#         if prev_node is None:
#             print(f"{prev_value} is not in the linked list")
#         else:
#             # Create a new node with the new value
#             new_node = Node(new_value)
#             # point the new_node's .next attribute to the prev_node's .next attribute
#             new_node.next = prev_node.next
#             # point the prev_node's .next attribute to the new node
#             prev_node.next = new_node



