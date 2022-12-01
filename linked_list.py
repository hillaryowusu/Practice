#this is how linked lists are implemented

class Node: 
    def __init__(self,data=None, next=None):
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
            print("Empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--->'
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
            count+=1
            itr = itr.next
        
        return count
    
    def remove_at(self, index):
        if index <0 or index>= self.get_length():
            raise Exception("Invalid Expression")
        
        if index == 0:
            self.head = self.headl.next
            return

        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next =itr.next.next
                break
            
            itr = itr.next
            count +=1

    def insert_at(self,index, data):
        if index <0 or index>= self.get_length():
            raise Exception("Invalid Expression")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

    def insert_after_value(self, data_after, data_to_insert):
        self.data_after = data_after
        self.data_to_insert = data_to_insert

        
        count = 0
        itr = itr.head

        while itr:
            if data_after in ll:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1
    


if __name__ == '__main__':
   ll = LinkedList()
   ll.insert_at_beginning(5)
   ll.insert_at_beginning(89)
   ll.insert_at_end(45)
   ll.insert_at_end(20)
   ll.insert_values(["orange", "apple", "banana", "mango"])
   ll.print()
   print(ll.get_length())
   ll.insert_at(0,"figs")
   ll.insert_after_value("orange","cake")
   ll.print()

        
