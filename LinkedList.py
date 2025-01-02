class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, element):
        node = Node(element, self.head)
        self.head = node

    def insert_at_specified_index(self, index, element):
        if index < 0 or index > self.get_length_of_the_linked_list():
            raise Exception("Index out of Range")
        else:
            if index == 0:
                self.insert_at_start(element)
            else:
                iterator = self.head
                count = 0
                while iterator.next:
                    if count == index-1:
                        break
                    count += 1
                    iterator = iterator.next
                iterator.next = Node(element, iterator.next)

    def insert_at_end(self, element):
        if self.head is None:
            self.insert_at_start(element)
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            node = Node(element, None)
            iterator.next = node

    def get_length_of_the_linked_list(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next
        return count

    def remove_element_at_start(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            self.head = self.head.next

    def remove_at_specified_index(self, index):
        if index < 0 or index >= self.get_length_of_the_linked_list():
            raise Exception("Index out of Range")
        elif index == 0:
            self.remove_element_at_start()
        else:
            count = 0
            iterator = self.head
            while iterator.next:
                if count == index-1:
                    break
                count += 1
                iterator = iterator.next
            iterator.next = iterator.next.next

    def remove_element_at_the_end(self):
        iterator = self.head
        while iterator.next.next:
            iterator = iterator.next
        iterator.next = None


    def remove_by_element(self, element):
        if self.head.data == element:
            self.head = self.head.next
        else:
            iterator = self.head
            while iterator.next:
                if iterator.next.data == element:
                    break
                iterator = iterator.next
            iterator.next = iterator.next.next


    def linear_search(self, target_element):
        count = 0
        iterator = self.head
        while iterator:
            if iterator.data == target_element:
                print(count)
                break
            count += 1
            iterator = iterator.next
        else:
            print("Element is Not in Linked List")


    def iterable_elements_convert_to_linked_list(self, list_of_elements):
        for i in list_of_elements:
            self.insert_at_end(i)


    def sort_linked_list(self):
        # it will perform Bubble Sort Technique to sort Linked List
        current = self.head
        while current.next:
            iterator = current.next
            while iterator:
                if current.data > iterator.data:
                    current.data, iterator.data = iterator.data, current.data
                iterator = iterator.next
            current = current.next


    def display_linked_list(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            iterator = self.head
            ll = ""
            while iterator:
                ll += str(iterator.data) + "-->"
                iterator = iterator.next
            print(ll)

if __name__ == "__main__":
    ll = LinkedList()  # create the Linked List Object
    nums = [10, 30, 40, 20, 100, 80, 60]
    ll.iterable_elements_convert_to_linked_list(nums)
    ll.display_linked_list()
    ll.sort_linked_list()
    ll.display_linked_list()

"""
Sample Output:
first convert list of items convert Linked List and Display 
    10-->30-->40-->20-->100-->80-->60-->  
sort the Linked List and Display
    10-->20-->30-->40-->60-->80-->100-->
Similarly we can use all function by using created Linked List Object
"""
