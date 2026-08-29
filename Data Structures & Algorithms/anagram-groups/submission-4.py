class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_group = defaultdict(list) # sorted -> strs list
        for s in strs:
            sorted_s = ''.join(sorted(s))
            # print(f'sorted_s: {sorted_s}')
            sorted_group[sorted_s].append(s)
        return list(sorted_group.values())
        