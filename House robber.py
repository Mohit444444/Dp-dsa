class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Set previous 2 values
        secondLast = 0
        last = nums[0]

        # Compute current value using previous two values
        # The final current value would be our result
        res = 0
        for i in range(1, n):
            res = max(nums[i] + secondLast, last)
            secondLast = last
            last = res

        return res

        # time O(n)
        # space O(1)