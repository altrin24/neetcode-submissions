class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums) 

        letArr = [1] * size
        rghArr = [1] * size

        for i in range(0,size,1):
            if i != 0:
                letArr[i] = letArr[i-1] * nums[i-1]

        
        for j in range(size-1 , -1,-1):
            if(j != (size-1)):
                rghArr[j] = rghArr[j+1] * nums[j+1]

        ans = [1] * size

        for i in range(size):
            ans[i] = letArr[i] * rghArr[i]

        return ans        


              