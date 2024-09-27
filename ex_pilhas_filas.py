# Definição da estrutura de nó para a lista encadeada
class No:
    def __init__(self, demanda):
        self.demanda = demanda
        self.proximo = None

# Definição da fila usando listas encadeadas
class FilaEncadeada:
    def __init__(self):
        self.frente = None  # Início da fila
        self.tras = None    # Final da fila

    # Método para enfileirar (adicionar demanda no final da fila)
    def enfileirar(self, demanda):
        novo_no = No(demanda)
        if self.tras is None:  # Se a fila está vazia
            self.frente = self.tras = novo_no
        else:
            self.tras.proximo = novo_no
            self.tras = novo_no
        print(f"Demanda {demanda} adicionada à fila.")

    # Método para desenfileirar (remover demanda da frente da fila)
    def desenfileirar(self):
        if self.frente is None:  # Verifica se a fila está vazia
            print("A fila está vazia. Nenhuma demanda para processar.")
            return None
        demanda_removida = self.frente.demanda
        self.frente = self.frente.proximo
        if self.frente is None:  # Se a fila fica vazia após a remoção
            self.tras = None
        print(f"Demanda {demanda_removida} removida da fila.")
        return demanda_removida

    # Método para verificar se a fila está vazia
    def esta_vazia(self):
        return self.frente is None

    # Método auxiliar para exibir o estado atual da fila
    def exibir_fila(self):
        if self.frente is None:
            print("Fila vazia.")
            return
        atual = self.frente
        fila = []
        while atual is not None:
            fila.append(atual.demanda)
            atual = atual.proximo
        print("Fila atual:", " -> ".join(map(str, fila)))

# Exemplo de uso do sistema de fila
fila = FilaEncadeada()

# Adicionando demandas na fila
fila.enfileirar(101)
fila.enfileirar(102)
fila.enfileirar(103)

# Exibindo a fila
fila.exibir_fila()

# Removendo demandas da fila
fila.desenfileirar()

# Exibindo a fila após remoção
fila.exibir_fila()

# Removendo mais demandas
fila.desenfileirar()
fila.desenfileirar()

# Tentativa de remoção com a fila vazia
fila.desenfileirar()

# Exibindo a fila final
fila.exibir_fila()
