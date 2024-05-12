class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origins = set()
        total = set()
        for origin, destiny in paths:
            total.add(origin)
            total.add(destiny)
            origins.add(origin)
        return (total - origins).pop()
