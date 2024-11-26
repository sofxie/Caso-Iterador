class Iterador:
    def __init__(self, array): # Se puede cualquier tipo de estructura, aqui usé Array
        self.array = array # Iniciar la estructura
        self.index = 0 # Indice para recorrer cada elemento

    def next(self): # Obtiene el siguiente elemento
        item = self.array[self.index] # Recorre dentro de la estructura con el indice
        self.index += 1 # Aumenta el indice para pasar al siguiente elemento
        return item # Retorna el elemento
    def hasNext(self): #Boolean que identifica si hay mas elementos dentro de la estructura
        return self.index < len(self.array) # Verifica que el indice no sea mayor a la cantidad total de elementos en la estructura