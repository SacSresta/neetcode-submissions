class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[3,4,5,6,1,2]
        l,r = 0, len(nums)-1 #0,5
        while l < r:
            m = l + (r - l) //2 # 0 + (5-0) // 2 = 5//2 = 2
            #nums[2] = 5
            if nums[m] < nums[r]: #if 5 < 2
                r = m
            else: 
                l = m +1 #l = 3, which is 6, goes until 
            
        return nums[l]

