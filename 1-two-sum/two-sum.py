class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                # If the complement exists in our map, we've found the solution.
                return [num_map[complement], i]
            # Otherwise, add the current number and its index to the map.
            num_map[num] = i
        #heheheh2
        