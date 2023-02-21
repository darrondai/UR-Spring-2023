# Q2 LAKE ONTARIO RAID
def LakeOntario(distances, M):
    recentStop = 0
    count = 0
    i = 1
    while (i < len(distances)):
        # keep going until there must be a stop
        if (distances[i] - distances[recentStop] > M):
            # if jump from one stop to adjacent stop is > M, not possible and return inf
            if (i-1 == recentStop):
                  return float('inf')
            # else insert the stop and add to the count
            recentStop = i-1
            count += 1
        # if dist between last stop and i is less than M, need to check if i is the last stop
        # if last stop, check if you can make the last jump
        if (i == len(distances)-1):
            if (distances[i] - distances[recentStop] > M):
                return float('inf')
            count += 1
        i += 1
    return count

# driver code
import time
startTime = time.perf_counter()

import sys
distances = [eval(i) for i in sys.argv[1].split(',')]
M = eval(sys.argv[2])
print('Min Stops: ' + str(LakeOntario(distances, M)))

print('Execution Time: ' + str((time.perf_counter() - startTime)*1000) + ' ms')