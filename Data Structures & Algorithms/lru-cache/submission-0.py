class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Nodos ficticios (dummy nodes)
        self.left = Node(0, 0)   # LRU
        self.right = Node(0, 0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    # Eliminar un nodo de la lista doblemente enlazada
    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev

    # Insertar un nodo al final (más recientemente utilizado)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        node.prev = prev
        node.next = nxt

        prev.next = node
        nxt.prev = node

    # Obtener un valor
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mover al final porque acabamos de utilizarlo
        self.remove(node)
        self.insert(node)

        return node.value

    # Insertar o actualizar un elemento
    def put(self, key: int, value: int) -> None:

        # Si existe, actualizar su valor y moverlo al final
        if key in self.cache:
            node = self.cache[key]

            node.value = value

            self.remove(node)
            self.insert(node)

            return

        # Si no existe, crear un nodo nuevo
        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        # Si superamos la capacidad, expulsamos el LRU
        if len(self.cache) > self.capacity:

            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]