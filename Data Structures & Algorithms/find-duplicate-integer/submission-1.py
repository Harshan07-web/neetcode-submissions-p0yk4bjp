class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #pls remember this is suposed to be solved 
        #by floyd cyc, not hashset, slow and fast pointer
        #imagine array as LL
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast==slow:
                break

        s2 = 0
        while True:
            slow = nums[slow]
            s2 = nums[s2]
            if slow==s2:
                return s2