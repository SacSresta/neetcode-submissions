class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1 #0,1
        while l < r:
            m = (l + r) //2 # 0 + (1-0) // 2 = 1//2 = 2
            #nums[2] = 5
            if nums[m] > nums[r]: #if 5 < 2
                l = m +1
            else: 
                r =m  #l = 3, which is 6, goes until 
            
        pivot = l

        def binary_search(left:int, right:int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) -1)



