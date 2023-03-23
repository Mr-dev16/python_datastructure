class Single_Linked_List:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.node_next = None
    
    def __init__(self):
        #function init of value 
        self.head = None
        self.body = None
        self.size = 0

    def __str__(self):
        #function read array in cycle not stop if is not None
        array = []
        node_now = self.head
        #condition why read is the size array
        while node_now != None:
            array.append(node_now.value)
            node_now = node_now.node_next
        return str(array) + " Size: " + str(self.size)
    
    def Prepend(self, value):
        #append element first of the linked list
        new_node = self._Node(value)
        if self.head == None and self.body == None:
            self.head = new_node
            self.body = new_node
        else:
            new_node.node_next = self.head
            self.head = new_node
        self.size += 1

    def Append(self, value):
        #function append values on the final array
        new_node = self._Node(value)
        if self.head == None and self.body == None:
            self.head = new_node
            self.body = new_node
        else:
            self.body.node_next = new_node
            self.body = new_node
        self.size += 1

    def Shift(self):
        #out first element of the linked list 
        if self.size == 0:
            self.head = None
            self.body = None
        else:
            node_delete = self.head
            self.head = node_delete.node_next
            node_delete.node_next = None
            self.size -= 1
            return node_delete.value

    def Pop(self):
        #function delete ultima element linked list 
        if self.size == 0:
            self.head = None
            self.body = None
        else:
            node_now = self.head
            new_body = node_now
            while node_now.node_next != None:
                new_body = node_now
                node_now = node_now.node_next
            self.body = new_body
            self.body.node_next=None
            self.size -= 1
            return print(node_now.value)
    

    def Get(self, index):
        #get value of the node with you input index
        if index == self.size - 1:
            return self.body
        elif index == 0:
            return self.head
        elif not index > 0 or  index < self.size - 1 :
            node_now  = self.head
            counter = 0
            while counter != index:
                node_now = node_now.node_next
                counter += 1
            return node_now
        else:
            return None





