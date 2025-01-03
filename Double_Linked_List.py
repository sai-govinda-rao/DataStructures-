class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, element):
        node = Node(element)
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.prev = None
            self.tail.next = None
        else:
            self.head.prev = node
            self.head = node
            self.head.prev = None
            self.head.next = self.tail
            self.tail = node

    def insert_at_end(self, element):
        node = Node(element)
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.prev = None
            self.tail.next = None

        else:
            iterator = self.tail
            while iterator.next:
                iterator = iterator.next
            node.prev = iterator
            iterator.next = node

    def insert_at_specified_index(self, index, element):
        if index < 0 or index > self.get_length_of_Double_linked_list():
            raise Exception("Index out of Range")
        elif index == 0:
            self.insert_at_start(element)
        else:
            iterator = self.head
            count = 0
            while iterator.next:
                if count == index-1:
                    break
                iterator = iterator.next
                count += 1
            node = Node(element, iterator, iterator.next)
            iterator.next = node
    def remove_at_start(self):
        if self.tail is None:
            print("Empty")
        else:
            self.head = self.head.next
            self.tail = self.tail.next

    def remove_at_specified_index(self, index):
        if index < 0 or index > self.get_length_of_Double_linked_list()-1:
            raise Exception("Index out of Range")
        elif index == 0:
            self.remove_at_start()
        elif index == self.get_length_of_Double_linked_list()-1:
            self.remove_at_last()
        else:
            iterator = self.head
            count = 0
            while iterator:
                if count == index-1:
                    break
                count += 1
                iterator = iterator.next
            iterator.next = iterator.next.next
            iterator.next.prev = iterator


    def remove_at_last(self):
        if self.tail is None:
            print("Empty")
        elif self.get_length_of_Double_linked_list() == 1:
            self.head = None
            self.tail = None
        else:
            iterator = self.head
            while iterator.next.next:
                iterator = iterator.next
            iterator.next = None

    def iterable_data_items_convert_to_Double_linked_list(self, elements):
        for i in elements:
            self.insert_at_end(i)

    def sort_doubly_linked_list(self):
        iterator1 = self.head
        while iterator1.next:
            iterator2 = iterator1.next
            while iterator2:
                if iterator1.data > iterator2.data:
                    iterator1.data, iterator2.data = iterator2.data, iterator1.data
                iterator2 = iterator2.next
            iterator1 = iterator1.next

    def linear_search(self, target):
        count = 0
        iterator = self.head
        while iterator:
            if iterator.data == target:
                print("Target is Found at index ", count)
                break
            count += 1
            iterator = iterator.next
        else:
            print("Target is Not in the Double Linked List")

    def get_length_of_Double_linked_list(self):
        iterator = self.tail
        count = 0
        while iterator:
            count += 1
            iterator = iterator.next
        return count

    def display_Doubly_Linked_List(self):
        if self.head is None:
            print("Double Lined List is Empty")
        else:
            iterator = self.tail
            dll = ""
            while iterator:
                dll += str(iterator.data) + "<-->"
                iterator = iterator.next
            print(dll)


if __name__ == "__main__":
    dll = Double_Linked_List()
    nums = [10, 1, 35, 40, 500, 11, 10]
    dll.iterable_data_items_convert_to_Double_linked_list(nums)
    dll.display_Doubly_Linked_List()
    dll.sort_doubly_linked_list()
    dll.display_Doubly_Linked_List()
    dll.linear_search(500)

"""
output:
    10<-->1<-->35<-->40<-->500<-->11<-->10<-->
    1<-->10<-->10<-->11<-->35<-->40<-->500<-->
    Target is Found at index  6
"""