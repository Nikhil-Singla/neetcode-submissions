class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "NULL"
        chars = set(''.join(strs))
        for i in range(1, 1000):
            if chr(i) not in chars:
                delimiter = chr(i)
                break 
                
        ans = delimiter + delimiter.join(strs)
        return ans

    def decode(self, s: str) -> List[str]:
        if s == "NULL":
            return []
        delimiter = s[0]
        ret = s.split(delimiter)
        del ret[0]
        return ret 
