class RandomizedSet:

    # hash map that stores indices that points to a linked list
    # inserting in a linked list is O(1), inserting to end of array is O(1)
    # removing from a hash map is O(1)
    # choosing a random indice given the size of the set is O(1) (i think)
    def __init__(self):
        self.array = []
        self.data = {}  # value -> index

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.array.append(val)
        self.data[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        index = self.data[val]

        last_element = self.array[len(self.array) - 1]
        self.array[len(self.array) - 1] = val

        self.array[index] = last_element

        self.array.pop()
        self.data[last_element] = index
        del self.data[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
