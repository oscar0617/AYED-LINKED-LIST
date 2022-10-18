class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def getValue(self):
        return self.value

    def setValue(self, new_value):
        self.value = new_value

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise Exception("New Next must be Node")

    def clear(self):
        self.value = None
        self.next = None

    def __str__(self):
        next = self.next
        return "Node("+str(self.value)+") -->" + ("x" if next is None else str(next))

class LinkedList:
    def __init__(self, data = []):
        self.head, self.tail, self.len = None, None, 0
        for e in data:
            self.append(e)

    def __len__(self):
        return self.len

    def append(self, value):
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            current_tail = self.tail
            current_tail.setNext(new_node)
            self.setTail(new_node)
        self.len = self.len + 1

    def search(self, value):
        current = self.head
        while current is not None and current.getValue() != value:
            current = current.getNext()
        return current
    def getHead(self):
        return self.head
    def getTail(self):
        return self.tail
    def setTail(self, new_tail):
        if new_tail is not None:
            new_tail.setNext(None)
            self.tail = new_tail
        else:
            self.tail = None

    def update(self, old_value, new_value):
        node_origin = self.search(old_value)
        node_origin.setValue(new_value)

    def slice(self, value, n=1):
        ld = LinkedList()
        node_origin = self.search(value)
        if node_origin is not None:
            current, index = node_origin, 0
            while current is not None and index < n:
                ld.append(current.getValue())
                current = current.getNext()
                index += 1
        return ld

    def isEmpty(self):
        return len(self) == 0

    def merge(self, list_b):
        if self.isEmpty():
            return list_b
        if list_b.isEmpty():
            return self
        self.tail.setNext(list_b.getHead())
        self.setTail(list_b.getTail())

    def delete(self, value):
        value_node = self.search(value)
        if value_node is not None:
            if len(self) == 1:# Soy el único
                self.head, self.tail = None, None
            else:
                if value_node == self.getHead():
                    self.head = value_node.getNext()
                else:
                    #Buscar el previo a value_node
                    prev = self.head
                    while prev.getNext() != value_node:
                        prev = prev.getNext()
                    if value_node == self.getTail():
                        self.setTail(prev)
                    else:
                        prev.setNext(value_node.getNext())
            value_node.clear()
            self.len -= 1
        else:
            raise Exception("Element not found.")

    def deleteStack(self, value):
        value_node = self.search(value)
        if value_node is not None:
            if len(self) == 1:  # Soy el único
                self.head, self.tail = None, None
            else:
                prev = self.head
                while prev.getNext() != value_node and prev.getNext() == None:
                    prev = prev.getNext()
                if value_node == self.getTail():
                    self.setTail(prev)
            value_node.clear()
            self.len -= 1
        else:
            raise Exception("Element not found.")
#FIFO
class Queue:
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, e):
        self.data.append(e) #Punto de referencia cómo el inicio

    def dequeue(self): #como punto de referencia el inicio
        element = self.data.getHead().getValue()
        self.data.delete(element)
        return element

    def __str__(self):
        return "Queue("+str(self.data.getHead())+")"

    def __len__(self):
        return len(self.data)

#Implementación LIFO
class Stack:
    def __init__(self):
        self.data = LinkedList()
    def push(self, e):
        self.data.append(e) #Punto de referencia cómo el final

    def pop(self):
        element = self.data.getTail()
        value = self.data.getTail().getValue()
        prev = self.data.getHead()
        while prev.getNext() != element:
            prev = prev.getNext()
        self.data.setTail(prev)
        return value

    def __str__(self):
        return "Stack("+str(self.data.getHead())+")"
    def __len__(self):
        return len(self.data)

def main():
    list = Stack()
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(1)
    list.push(2)
    list.push(3)
    list.push(1)
    list.push(2)
    list.push(3)
    print(list)
    cabeza = list.pop()
    print(cabeza)
    cabeza = list.pop()
    print(cabeza)
    print(list)

main()