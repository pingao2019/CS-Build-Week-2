  
#     # find the words having same letters as a group. 
#     # print a list containing lists with different group.
#     # 
#     """Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]"""

 
def groupAnagrams(strs):
    from collections import defaultdict
    d = defaultdict(list)
    for s in strs:
        d[''.join(sorted(s))].append(s)
    return (d.values())




strs=["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))




