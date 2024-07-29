
def lis(nums) :
    # Make dp list
    dp = [1] * len(nums)

    # Outerloop
    for i in range(1, len(nums)) :
        for j in range(0, i) :
            if (nums[i] > nums[j] and dp[i] < dp[j] + 1) :
                dp[i] = dp[j] + 1

    return max(dp)
