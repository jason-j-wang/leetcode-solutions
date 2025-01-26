#https://leetcode.com/problems/move-pieces-to-obtain-a-string/?envType=daily-question&envId=2025-01-26
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s = {"L": 0, "R": 0, "_": 0}
        t = {"L": 0, "R": 0, "_": 0}

        for i in range(len(start)):
            s[start[i]] += 1
            t[target[i]] += 1



            if target[i] == "R":
                if s["L"] != t["L"] or s["R"] < t["R"]: #or (s["R"] == t["R"] and start[i] != target[i]):
                    return False

                # for key in s:
                #     s["L"] = 0
                #     t["L"] = 0

            if target[i] == "L":
                if s["R"] != t["R"] or s["L"] > t["L"] or (s["L"] == t["L"] and start[i] != target[i]):
                    return False
                # for key in s:
                #     s["R"] = 0
                #     t["R"] = 0

            if start[i] == "R" and s["L"] != t["L"]:
                return False

            if start[i] == "L" and s["R"] != t["R"]:
                return False

            
                
        return s["L"] == t["L"] and s["R"] == t["R"]
