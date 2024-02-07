class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self.head = prev

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        left_half, right_half = self.split_list(head)
        left = self.merge_sort(left_half)
        right = self.merge_sort(right_half)

        return self.merge(left, right)

    def split_list(self, head):
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        return head, slow

    def merge(self, left, right):
        dummy = Node(0)
        tail = dummy

        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        elif right:
            tail.next = right

        return dummy.next

    def sort(self):
        self.head = self.merge_sort(self.head)


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next


def main():
    print(f"*** GoIT Neo Algo Final Project ***")

    # Create and reverse a single-linked list
    llist = LinkedList()
    for i in range(0, 9):
        llist.append(i)
    print(f"\nTask 1 - Single Linked List | The original list:")
    llist.print_list()

    llist.reverse()
    print(f"\nTask 1 - Single Linked List | Reversed list:")
    llist.print_list()

    # Sorting a single-linked list
    llist2 = LinkedList()
    for i in [4, 7, 2, 5, 8, 1, 9, 3, 6, 0]:
        llist2.append(i)
    print(f"\nTask 1 - Single Linked List | An unsorted list:")
    llist2.print_list()

    llist2.sort()
    print(f"\nTask 1 - Single Linked List | Sorted list:")
    llist2.print_list()

    # Merge two sorted single-linked lists
    llist3 = LinkedList()
    llist4 = LinkedList()
    for i in [1, 3, 5, 7, 9]:
        llist3.append(i)
    for i in [0, 2, 4, 6, 8,]:
        llist4.append(i)

    merged_head = merge_sorted_lists(llist3.head, llist4.head)

    # Outputting the result of the merge
    current = merged_head
    print(f"\nTask 1 - Single Linked List | Merge sorted list:")
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    main()
