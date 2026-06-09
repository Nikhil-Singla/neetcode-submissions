class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()

        for oneNum in nums:
            if oneNum in a:
                return True

            a.add(oneNum)

        return False
