class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1

        while l < r:
            comb_sum = numbers[l] + numbers[r]

            if comb_sum == target:
                return[l+1,r+1]
            elif comb_sum > target:
                r-=1
            elif comb_sum < target:
                l+=1

