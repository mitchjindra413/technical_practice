class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        totalSkill = skill[0] + skill[-1]
        
        end = -1
        res = 0
        for i in range(len(skill) // 2):
            if skill[i] + skill[end] == totalSkill:
                res += skill[i] * skill[end]
                end -= 1
            else:
                return -1
        
        return res
       