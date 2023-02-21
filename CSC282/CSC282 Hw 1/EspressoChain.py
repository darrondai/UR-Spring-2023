# Q1 ESPRESSO CHAIN
def EspressoChain(distances, profits, k):
    # init dp array with 0s
    # set max profit using first location to the profit of the first location
    dp = [0 for i in range(len(distances))]
    dp[0] = profits[0]

    # bottom up implementation using previous values
    for j in range(1, len(distances)):
        # maxProf holds current max before each iteration
        # first check if taking jth location by itself is better than dp[j-1]
        maxProf = max(dp[j-1], profits[j])

        # take the jth location and add to highest profit from last compatible location i
        # then compare to maxProf
        for i in range(j, -1, -1):
            if (distances[j] - distances[i] >= k):
                maxProf = max(maxProf, dp[i] + profits[j])
                break;

        # save the maxProfit of using first j locations to dp[j]
        dp[j] = maxProf

    return dp[len(distances)-1]

# driver code
import time
startTime = time.perf_counter()

import sys
distances = [eval(i) for i in sys.argv[1].split(',')]
profits = [eval(i) for i in sys.argv[2].split(',')]
k = eval(sys.argv[3])
print('Max Profit: ' + str(EspressoChain(distances, profits, k)))

print('Execution Time: ' + str((time.perf_counter() - startTime)*1000) + ' ms')