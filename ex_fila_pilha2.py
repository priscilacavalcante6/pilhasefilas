# Para abordar este desafio, você pode implementar uma fila baseada em listas encadeadas em Python.
# Esta estrutura é ideal para gerenciar demandas em um ambiente de processamento intenso,
# pois permite inserções e remoções eficientes sem a necessidade de realocar todos os elementos da fila.
# Aqui está um exemplo de como você poderia implementar essa fila:

class Node:  # DEMANDA NA FILA
    def __init__(self, id):
        self.id = id
        self.next = None

class Queue:  # GERENCIA A FILA DE PROCESSOS
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, id):  # ADICIONA A DEMANDA NO FINAL DA FILA
        new_node = Node(id)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:  # Se a fila estava vazia
            self.head = new_node

    def dequeue(self):  # REMOVE A DEMANDA MAIS ANTIGA DO INÍCIO DA FILA
        if not self.head:
            return None  # A fila está vazia
        removed_id = self.head.id
        self.head = self.head.next
        if not self.head:  # Se a fila ficou vazia após a remoção
            self.tail = None
        return removed_id

# Exemplo de uso
process_queue = Queue()
process_queue.enqueue(1)
process_queue.enqueue(2)
process_id = process_queue.dequeue()
print(f"Processo removido da fila: {process_id}")  # Deve exibir 1
process_id = process_queue.dequeue()
print(f"Processo removido da fila: {process_id}")  # Deve exibir 2
process_id = process_queue.dequeue()
print(f"Processo removido da fila: {process_id}")  # Deve exibir None, pois a fila está vazia


# Nesse código, a classe Node representa cada demanda na fila, 
# enquanto a classe Queue gerencia a fila de processos. 
# O método enqueue adiciona novas demandas ao fim da fila, 
# e o método dequeue remove a demanda mais antiga do início da fila. 
# Essa implementação garante que a ordem das demandas seja mantida e que a manipulação da fila seja
# feita de maneira eficiente, adequando-se ao aumento do volume de trabalho após a fusão da empresa.
