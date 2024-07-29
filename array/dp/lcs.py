def longestCommonSubsequence(text1, text2) :
        # Create dp 2d arr
        # dp = [[0] * (len(text2) + 1)] * (len(text1) + 1)
        dp = []
        for row in range(len(text1) + 1) :
            dp.append([0] * (len(text2) + 1))

        # Recurrence relation
        # When text1[i] == text2[i][j]
        # dp[i][j] = dp[i - 1][j - 1] + 1
        # When text1[i] != text2[j]
        # dp[i][j] = max(3 around it)

        # dp loop
        for i in range(1, len(text1) + 1) :
            for j in range(1, len(text2) + 1) :
                # Check bounds
                if text1[i - 1] == text2[j - 1] :
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else :
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        result = dp[len(text1)][len(text2)]

        if result > min(len(text2), len(text1)) :
            return min(len(text2), len(text1))
        return result