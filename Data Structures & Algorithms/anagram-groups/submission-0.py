from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string not in strs_map:
                strs_map[sorted_string] = [string]
            else:
                strs_map[sorted_string].append(string)
        result = []
        for anagram in strs_map.values():
            result.append(anagram)
        return result
        
        


        