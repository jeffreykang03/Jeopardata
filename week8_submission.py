import numpy as np
inp = np.array(list(map(int, input().split())))

dp = np.array(([0]) * (inp.size + 2))

for i in range(inp.size):
    dp[inp[i]] += 1

miss = np.array([], dtype = int)
dup = np.array([], dtype = int)

for i in np.arange(1, dp.size):
    if(dp[i] == 0):
        miss = np.append(miss, int(i))
    if(dp[i] > 1):
        dup = np.append(dup, int(i))
print("missing: ", miss, "; duplicated: ", dup)
