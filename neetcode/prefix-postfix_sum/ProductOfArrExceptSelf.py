'''
LC 238 Product of Array Except Self (Medium)

Given int array nums, return new arr where arr[i] is the product of all nums except nums[i]
Example:
nums = [1,2,3,4]
outp = [24, 12, 8, 6]

I will track prefix and postfix of each nums[i]. 
1: iterate over nums and fill res[i] with prefix products
2: iterate over nums backwards and multiplyres[i] by postfix
3: return result 

'''
def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


nums = [1,2,3,4]
print(productExceptSelf(nums))