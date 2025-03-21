#https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/?envType=daily-question&envId=2025-03-21
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        s = set(supplies)

        compound = []
        compound_ingredients = []
        ans = []


        for i in range(len(recipes)):
            valid = True
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in s:
                    compound.append(recipes[i])
                    compound_ingredients.append(ingredients[i])
                    valid = False
                    break
            
            if valid:
                ans.append(recipes[i])
                s.add(recipes[i])

        prev = 0
        while len(s) != prev:
            prev = len(s)
            nc = []
            nci = []
            for i in range(len(compound)):
                valid = True
                for j in range(len(compound_ingredients[i])):
                    if compound_ingredients[i][j] not in s:
                        nc.append(compound[i])
                        nci.append(compound_ingredients[i])
                        valid = False
                        break
                
                if valid:
                    ans.append(compound[i])
                    s.add(compound[i])

            compound = nc
            compound_ingredients = nci
        return ans