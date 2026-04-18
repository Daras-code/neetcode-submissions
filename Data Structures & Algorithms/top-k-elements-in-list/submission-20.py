class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        count = 1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            dictionary[nums[i]] = count
            if nums[i] != nums[i+1]:
                count = 1
        dictionary[nums[-1]] = count
        sorted_items =sorted(dictionary.items(), key =lambda x:x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]