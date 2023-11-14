class LLNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def has_val(self,value):
        if self.data == value:
            return True
        else:
            return False

class SingleLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_list_item(self,item):
        if not isinstance(item,LLNode):
            item = LLNode(item)
        
        if self.head is None:
            self.head = item
        
        else:
            self.tail.next = item
        
        self.tail = item
    
    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1
            current_node = current_node.next

        return count

    def output_list(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

node1 = LLNode(10)
node2 = LLNode(4)
node3 = LLNode(1)
node4 = LLNode("paul")

LL = SingleLL()
print(f'list length {LL.list_length()}')
