#https://leetcode.com/problems/minimum-array-end/description/?envType=daily-question&envId=2025-02-03
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x

        
        b = bin(x)[2:]
        nb = bin(n-1)[2:]

        num = [b[i] for i in range(len(b))]
        num = num[::-1]

        embed = [nb[i] for i in range(len(nb))]
        embed = embed[::-1]

        # for _ in range(n-1):
        #     carryOver = True
        #     for i in range(len(curNum)):
        #         if canChange[i] == "0" and curNum[i] == "0":
        #             curNum[i] = "1"
        #             carryOver = False
        #             break
        #         elif canChange[i] == "0" and curNum[i] == "1":
        #             curNum[i] = "0"
        #     if carryOver:
        #         canChange.append("0")
        #         curNum.append("1")

        pointer = 0
        for i in range(len(num)):
            if pointer >= len(embed):
                break
            if num[i] == "0":
                num[i] = embed[pointer]
                pointer += 1
        
        num += embed[pointer:]


        num = num[::-1]
        return int("".join(num), 2)

            
                

        