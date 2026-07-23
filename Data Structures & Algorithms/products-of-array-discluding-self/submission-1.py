class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums) 

        letArr = [1] * size
        rghArr = [1] * size

        for i in range(0,size,1):
            if i != 0:
                letArr[i] = letArr[i-1] * nums[i-1]

        suf = 1
        for j in range(size - 1, -1, -1):
            letArr[j] *= suf
            suf *= nums[j]

        return letArr       


              