# Завдання 1
# Додайте метод delete для видалення пар ключ-значення таблиці HashTable,
# яка реалізована в конспекті.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if not self.table[key_hash]:
            self.table[key_hash].append(key_value)
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.table[key_hash].append(key_value)

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    self.table[key_hash].pop(i)
                    return True
        return False
    
    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            if bucket:
                print(", ".join(f"{pair[0]}: {pair[1]}" for pair in bucket))
            else:
                print("Empty")

# Тестуємо наш новий метод delete:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.print_table()
print("\n")
print(H.get("apple"))   # Виведе: 10
print(H.delete("apple")) # Виведе: True, бо "apple" буде видалено
print(H.get("apple"))    # Виведе: None, бо "apple" було видалено
print(H.delete("grape")) # Виведе: False, бо "grape" не існує
print("\n")
H.print_table()