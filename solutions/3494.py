#https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        done_by = []
        times = []
        time = 0
        
        for i in range(len(skill)):
            times.append(mana[0] * skill[i])
 
            time += mana[0] * skill[i]
            done_by.append(time)
       

        for k in range(1, len(mana)):
            additional_time = 0
            done = []
            best = done_by[-1] + mana[k] * skill[-1]
            for i in range(len(skill)-2, -1, -1):
                needed = best - mana[k] * skill[i+1]
                if needed < done_by[i] + mana[k] * skill[i]:
                    additional_time += done_by[i] + mana[k] * skill[i] - needed
                    best = done_by[i] + mana[k] * skill[i]
                else:
                    best -= mana[k] * skill[i+1]

            total = []
            actual = done_by[-1] + mana[k] * skill[-1] + additional_time
            for i in range(len(skill)-1, -1, -1):
                total.append(actual)
                actual -= mana[k] * skill[i]
            total.reverse()
            done_by = total


        return done_by[-1]
        