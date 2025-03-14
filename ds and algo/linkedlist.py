class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "==>"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        # print(count)
        return count

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            return

        if self.head == None:
            print("Linked List is empty")
            return

        if index < 0 or index > self.get_length():
            print("Out of Bound Index")
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, item):
        if index < 0 or index > self.get_length():
            print("Out of Bound Index")
            return

        if index == 0:
            self.insert_at_beginning(item)
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                node = Node(item, itr.next)
                itr.next = node
            count += 1
            itr = itr.next

        # if empty
        # None =>

        pass

    def insert_after_value(self, data_after, data_to_insert):
        if self.get_length() == 0:
            print("Linked List is empty")
            return

        # Search for the first occurrence of data_after value in linked list
        itr = self.head
        found_match = False
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
        # Now insert data_to_insert after date_after node
        pass

        if not found_match:
            print((f"Could not insert value as {data_after} did not exist"))

    def remove_by_value(self, data):
        # remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(500)
    ll.print()
    print("==================")
    # ll.get_length()
    # ll.remove_at(2)
    # ll.insert_at(2, "New taker")
    ll.insert_after_value(900, 99)
    ll.print()
