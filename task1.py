class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int) -> None:
        cur: Node | None = self.head

        if cur is not None and cur.data == key:
            self.head = cur.next
            return

        prev: Node | None = None
        while cur is not None and cur.data != key:
            prev = cur
            cur = cur.next

        if cur is None:
            return

        if prev is not None:
            prev.next = cur.next


    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# --------------- Revers list --------------- #
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# --------------- Merge sort --------------- #
    def merge_sort(self, head: Node | None) -> Node | None:
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        if middle is None:
            return head

        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        return self.sorted_merge(left, right)

    def get_middle(self, head: Node | None) -> Node | None:
        if head is None:
            return None

        slow: Node = head
        fast: Node | None = head

        while fast is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next 
            fast = fast.next.next

        return slow

    
    def sorted_merge(self, a: Node | None, b: Node | None) -> Node | None:
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def sort(self):
        self.head = self.merge_sort(self.head)

# --------------- Merge sorted list --------------- #
    def merge_sorted_lists(self, other: 'LinkedList') -> 'LinkedList':
        merged = LinkedList()
        merged.head = self.sorted_merge(self.head, other.head)
        return merged

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)


list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

merged_list = LinkedList.merge_sorted_lists(list1, list2)
print("Об'єднаний список:")
merged_list.print_list()

print("\nРеверсування:")
merged_list.reverse_list()
merged_list.print_list()

print("\nСортування:")
merged_list.sort()
merged_list.print_list()

list1 = LinkedList()
list2 = LinkedList()

