def extended_bottom_up_cut_rod(prices, n):
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)
    
    for j in range(1, n + 1):
        max_value = float('-inf')
        
        for i in range(1, j + 1):
            if prices[i] + dp[j - i] > max_value:
                max_value = prices[i] + dp[j - i]
                cuts[j] = i
        
        dp[j] = max_value
    
    return dp, cuts


def print_cuts(prices, n):
    dp, cuts = extended_bottom_up_cut_rod(prices, n)
    
    print("Maximum Revenue:", dp[n])
    print("Cuts:")
    
    while n > 0:
        print(cuts[n], end=" ")
        n -= cuts[n]


prices = [0, 10, 5, 8, 9]
print_cuts(prices, 4)

def cut_rod_recursive(prices, n):
    if n == 0:
        return 0
    
    max_value = float('-inf')
    
    for i in range(1, n + 1):
        max_value = max(max_value, prices[i] + cut_rod_recursive(prices, n - i))
    
    return max_value


prices = [0, 10, 5, 8, 9]  # index 0 unused
print(cut_rod_recursive(prices, 4))  # 10