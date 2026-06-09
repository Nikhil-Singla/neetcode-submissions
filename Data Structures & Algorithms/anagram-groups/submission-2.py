class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finaldict = {}
        for onestring in strs:
            hashset = [0] * 26
            strin = ""
            for letter in onestring:
                hashset[ord(letter)-97] += 1
                print(letter)

            for i in hashset:
                strin += str(i) + ","

            print(strin)
            finaldict.setdefault(strin, []).append(onestring)
        
        answer = []
        for group in finaldict.values():
            answer.append(group)

        return answer