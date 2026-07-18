class Node:
  
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:


    def __init__(self):
        self.head = None

    # prepend
  
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

   
    # append
   
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

   
    # delete
   
    def delete(self, value):

        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:

            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

   
    # reverse
    
    def reverse(self):

        previous = None
        current = self.head

        while current:

            nxt = current.next

            current.next = previous

            previous = current

            current = nxt

        self.head = previous

    # has_cycle
   
    def has_cycle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # iter
    
    def __iter__(self):

        current = self.head

        while current:
            yield current.data
            current = current.next

   
    # repr
   
    def __repr__(self):

        return " -> ".join(str(item) for item in self) + " -> None"

# TEST CASES


ll = LinkedList()

# Test 1
ll.append(10)
ll.append(20)
ll.append(30)
print(ll)

# Test 2
ll.prepend(5)
print(ll)

# Test 3
ll.delete(20)
print(ll)

# Test 4
ll.reverse()
print(ll)

# Test 5
print(list(ll))

# Test 6
print(repr(ll))

# Test 7
print(ll.has_cycle())

# Test 8
cycle = LinkedList()
cycle.append(1)
cycle.append(2)
cycle.append(3)

cycle.head.next.next.next = cycle.head

print(cycle.has_cycle())
