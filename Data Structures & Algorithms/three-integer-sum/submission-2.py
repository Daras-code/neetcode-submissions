class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        seen = set()
        nums.sort()
        k = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == -nums[i] and (nums[i],nums[left],nums[right]) not in seen:
                    triples.append([nums[i],nums[left],nums[right]])
                    seen.add((nums[i],nums[left],nums[right]))
        
                elif (nums[left] + nums[right] + nums[i]) > 0:
                        right -= 1
                else:
                    left += 1
        return triples

