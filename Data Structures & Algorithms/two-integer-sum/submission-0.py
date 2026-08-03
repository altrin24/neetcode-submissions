class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        st = {}
        arr =[]

        for i in range(0,len(nums)):
            
            lpTarget = target-nums[i] 
            if lpTarget in st:
                arr=[st[lpTarget],i]
                arr.sort()
                return arr
            st[nums[i]] = i   

        return []       


        