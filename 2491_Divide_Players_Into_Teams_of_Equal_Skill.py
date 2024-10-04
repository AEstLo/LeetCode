class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        result = skill[l] * skill[r]
        reference_skill_per_team = skill[l] + skill[r]
        l += 1
        r -= 1
        while l < r:
            current_team_skill = skill[l] + skill[r]
            if reference_skill_per_team != current_team_skill:
                return -1
            result += skill[l] * skill[r]
            l += 1
            r -= 1
        return result
