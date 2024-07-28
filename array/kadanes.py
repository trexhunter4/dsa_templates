# Kadanes is an algorithm for finding the maximum sum of any possible subarray in an array

# O(n) Space
def kadanes_1D (nums) :
    dp = [0] * len(nums)
    dp[0] = nums[0]

    largest = float('-inf')

    for i in range(1, len(nums)) :
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    
        if (dp[i] > largest) :
            largest = dp[i]

    return largest 

# O(1) Space
def kadanes (nums) :
    max = (float('-inf'))
    sum = 0

    for num in nums :
        if (num > sum and sum < 0) :
            sum = num
        else :
            sum += num

        if (sum > max) :
            max = sum

    return max