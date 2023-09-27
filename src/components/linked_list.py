class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def node_append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def node_prepend(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        

    def insert_node(self, position, new_data):

        cur_position = 1
        new_node = Node(new_data)
        cur_node = self.head

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        if self.head is None and position > 0:
            print("List and position does not exist")


        while cur_position < position - 1:
            cur_node = cur_node.next

            if cur_node.next is None:
                print("Position doesn't exist")
                return
            
            cur_position += 1

        next_node = cur_node.next
        cur_node.next = new_node
        new_node.next = next_node


    def find_node(self, data):
        cur_node = self.head
        counter = 0

        while data != cur_node.data:
            counter += 1
            cur_node = cur_node.next

        print("Data found in position: " + str(counter))
        print("Data found in position: {}".format(counter))


    def delete_node(self, delete_position):

        cur_node = self.head
        prev_node = cur_node
        counter = 0

        #Suppose the delete position is 1
        # previous_node, node_to_delete, next_node

        # A , B , C
        # 0, 1, 2

        if delete_position == 0:
            self.head = cur_node.next


        while counter < delete_position:

            prev_node = cur_node
            cur_node = cur_node.next
            counter += 1

        cur_node = cur_node.next
        prev_node.next = cur_node



    def reverse_list(self):

        reverseDict = {}
        n = 0
        cur_node = self.head

        newList = LinkedList()


        while cur_node:
            reverseDict[n] = cur_node
            cur_node = cur_node.next
            n += 1



        index = len(reverseDict) - 1
        newList.node_append()



        return None


#[1] [3] [5] [8] [2] [5]

# {0:O1, 1:02, 2:03, 3:04}

#:{0:04, 1:}
# when no more next, then assign in reverse


#[2] [4] [6] [7]
class Solution: 
    def merge_list(self, list1, list2):

        llist3 = LinkedList()

        cur_node1 = list1.head
        cur_node2 = list2.head

        while cur_node1 or cur_node2:

            if not cur_node1:
                llist3.node_append(cur_node2.data)
                cur_node2 = cur_node2.next
            elif not cur_node2:
                llist3.node_append(cur_node1.data)
                cur_node1 = cur_node1.next
            elif cur_node1.data < cur_node2.data:
                llist3.node_append(cur_node1.data)
                cur_node1 = cur_node1.next
            elif cur_node2.data < cur_node1.data:
                llist3.node_append(cur_node2.data)
                cur_node2 = cur_node2.next
            elif cur_node1.data == cur_node2.data:
                llist3.node_append(cur_node1.data)
                cur_node1 = cur_node1.next


        return llist3


llist = LinkedList()
llist2 = LinkedList()

a_var = [2,9,8,3,1]
b_var = [7,5,6,2]
c_var = "hello"
d_var = "chill"

llist.node_append(1)
llist.node_append(3)
llist.node_append(5)
llist.node_append(7)
llist.node_append(55)
llist.node_append(60)



llist2.node_append(1)
llist2.node_append(2)
llist2.node_append(6)
llist2.node_append(8)
llist2.node_append(9)
llist2.node_append(57)


llist2.print_list()


print("list5 printed")


print(llist.reverse_list())



llist.print_list()
