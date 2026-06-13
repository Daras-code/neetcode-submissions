class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(position, remainder, listofnum):
            if remainder == 0:
                result.append(listofnum[:])
            elif remainder < 0:
                return None
            else:
                for i in range(position, len(nums)):
                    listofnum.append(nums[i])
                    remainder -= nums[i]
                    backtrack(i,remainder,listofnum) 
                    listofnum.pop()
                    remainder += nums[i]
        backtrack(0,target, [])
        return result