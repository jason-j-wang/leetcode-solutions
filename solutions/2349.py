#https://leetcode.com/problems/design-a-number-container-system/?envType=daily-question&envId=2025-02-08
class NumberContainers:

    def __init__(self):
        self.indice_values = defaultdict(int)
        self.number_location = defaultdict(list)
        self.previous_indice_values = defaultdict(set)
        
    def change(self, index: int, number: int) -> None:
        # check if the index already has a number
        if self.indice_values[index] != 0:
            self.remove_index(index, self.indice_values[index])
        self.indice_values[index] = number
        if index in self.previous_indice_values[number]:
            self.previous_indice_values[number].remove(index)
        self.add_index_to_number_location(index, number)


    def find(self, number: int) -> int:
        if not self.number_location[number]:
            return -1
        
        while self.number_location[number] and self.number_location[number][0] in self.previous_indice_values[number]:
            heapq.heappop(self.number_location[number])
        if not self.number_location[number]:
            return -1
        return self.number_location[number][0]

    # remove the index from the old number
    def remove_index(self, index: int, old_number: int) -> None:
        self.previous_indice_values[old_number].add(index)

    def add_index_to_number_location(self, index: int, number: int) -> None:
        indices = self.number_location[number]
        heapq.heappush(indices, index)


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)