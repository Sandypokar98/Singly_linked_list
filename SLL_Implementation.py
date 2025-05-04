class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def traverse(self,data):
        temp=self.start
        while temp:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,data1,data2):
        temp=self.traverse(data1)
        if temp:
            if temp.next==None:
                self.insert_at_last(data2)
            else:
                n=Node(data2,temp.next)
                temp.next=n
        else:
            print(data1,"is not part of list")
    def print_list(self):
        if self.is_empty():
            print("Empty")
            return
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
        print("")
    def del_last(self):
        if self.is_empty():
            print("Error: List is already empty")
        elif self.start.next is None:
            self.del_first()
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def del_first(self):
        if self.start:
            self.start=self.start.next
        else:
            print("List is already empty")
    def del_item(self,data):
        if self.is_empty():
            print("Error: List is already empty")
        elif self.start.next is None:
            if self.start.item==data:
                self.del_first()
            else:
                pass
        else:
            temp=self.start
            if temp.item==data:
                self.del_first()
            else:
                while temp.next.item != data:
                    temp=temp.next
                temp.next=temp.next.next
    def del_all(self):
        self.start=None
    def length(self):
        count=0
        temp=self.start
        while temp:
            count+=1
            temp=temp.next
        return count
    def search(self,data):
        index=0
        temp=self.start
        if temp is not None:
            while temp is not None:
                if temp.item==data:
                    return index
                index+=1
                temp=temp.next
            print(f"{data} is not present in list")
            return -1
        else:
            print("List is empty")
            return -1
    def reverse(self):
        if self.is_empty():
            print("list is empty")
            return
        prev=None
        temp=self.start
        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        self.start=prev
    def sort(self):
        if self.is_empty() or self.start.next is None:
            print("List has 1 or zero element")
        else:
            swaping=True
            while swaping:
                temp=self.start
                swaping=False
                while temp.next:
                    if temp.item > temp.next.item:
                        temp.item,temp.next.item=temp.next.item,temp.item
                        swaping = True  
                    temp=temp.next
    def concat(self,l_list):
        if l_list.is_empty():
            print("list is empty")
        if self.is_empty():
            self.start=l_list.start
        else:
            temp=self.start
            while temp.next:
                temp=temp.next
            temp.next=l_list.start
        

#driver code
sll=SLL()
print(sll.is_empty())       #True
sll.insert_at_start(20)     #insert 20 at start
sll.print_list()            #20
print(sll.length())         #1
sll.insert_at_start(10)     #insert 10 at start
print(sll.is_empty())       #False
sll.print_list()            #10 20
print(sll.length())         #2
sll.insert_at_last(30)      #insert 30 at last
sll.print_list()            #10 20 30
print(sll.length())         #3
sll.insert_after(10,25)     #insert 25 after 10
sll.print_list()            #10 25 20 30
print(sll.length())         #4
sll.del_item(10)            #delete 10
sll.print_list()            #25 20 30
print(sll.length())         #3
sll.insert_at_start(10)     #insert 10 at start
sll.print_list()            #10 25 20 30
print(sll.length())         #4
print(sll.search(3))        #searches 3 in list if not present the shows message and returns -1
sll.insert_at_start(1)      #insert 1 at start
sll.print_list()            #1 10 25 20 30
print(sll.length())         #5
sll.del_last()              #delete last element
sll.print_list()            #1 10 25 20
print(sll.length())         #4
sll.del_first()             #delete 1st element
sll.print_list()            #10 25 20
#sll.del_all()              #delete all line is commented
sll.print_list()            #10 25 20
print(sll.length())         #3
sll.reverse()               #reverse list order
sll.insert_at_start(30)     #insert 30 at start
sll.insert_at_last(15)      #insert 15 at last
sll.print_list()            #30 20 25 10 15
sll.sort()                  #sorted in ascending order
sll.print_list()            #10 15 20 25 30

sll2=SLL()                  #sll2 singly linked list object is created
sll2.insert_at_start(20)
sll2.print_list()
print(sll.length())
sll2.insert_at_start(10)
print(sll.is_empty())
sll2.print_list()
print(sll.length())
sll2.insert_at_last(30)
sll2.print_list()
print(sll.length())
sll2.insert_after(10,25)
sll2.print_list()           #10 25 20 30
sll.concat(sll2)            #concatination
sll.print_list()            #10 15 20 25 30 10 25 20 30