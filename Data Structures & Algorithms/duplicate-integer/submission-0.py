class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = []
        for i in range(len(nums)):
            current_num = nums[i] 
            rest_all = nums[i+1:]
            if current_num in rest_all:
                result.append(current_num)
            else:
                pass

        if len(result) != 0:
            return True
        else:
            return False

            
         