class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #parse list and make dictionaries of each O(n*m) n # of words, m # length of words        
            # if not in dict add collection in anagram dict

            # else add to dict array

        ans = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            ans[key].append(word)

        return list(ans.values())



