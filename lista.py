class Lista():

    def __init__(self):
        self.head = None
        self.length = 0
        self.index = 0

    def push(self, data):
        nodo = Nodo(data, self.index)
        if self.head == None:
            self.head = nodo
        else:
            self.last.next = nodo

        self.last = nodo
        self.length += 1
        self.index += 1

    def print(self):
        aux = self.head
        while aux != None:
            print(aux.data, end=' ')
            aux = aux.next

    def isEmpty(self):
        return self.head == None

    def eliminar_del_fat(self, fat):
        aux = self.head
        while aux != None:
            fat[aux.data] = None
            aux = aux.next

        return True, fat, self.length

    def editar_nodo(self, actual, nuevo):
        aux = self.head
        while aux.data != actual:
            aux = aux.next

        aux.data = nuevo



    def get_data_by_index(self,index):
        aux = self.head
        while aux != None:
            if aux.index == index:
                return aux.data
            aux = aux.next

    def get_index_by_value(self,value):
        aux = self.head
        while aux != None:
            if aux.data == value:
                return aux.index
            aux = aux.next

class Nodo():

    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.next = None





