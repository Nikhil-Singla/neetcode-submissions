class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabet = [0] * 26

        for letter in s:
            alphabet[ord(letter) - 97] += 1

        for letter in t:
            alphabet[ord(letter) - 97] -= 1

        for frequency in alphabet:
            if frequency != 0:
                return False

        return True