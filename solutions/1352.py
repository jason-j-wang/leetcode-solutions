#https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2025-02-14
class ProductOfNumbers:

    def __init__(self):
        self.last_zero = -1
        self.res = [1]
        self.len = 0
        

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = self.len
            num = 1
        self.res.append(num * self.res[-1])
        self.len += 1

    def getProduct(self, k: int) -> int:
        if self.last_zero >= len(self.res) - 1-k:
            return 0
        return self.res[-1] // self.res[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)