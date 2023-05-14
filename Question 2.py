jobs = [[1, 6, 6], [2, 5, 5],[5, 7, 5], [6, 8, 3]]
# Using start point:
jobs.sort(key=lambda x:x[0])
weights = [row[-1] for row in jobs]
maxProfit = [row[-1] for row in jobs]
for i in range(len(jobs)):
    for j in range(i):
        if(i==j):
            continue
        if jobs[j][1] <= jobs[i][0]:
            maxProfit[i] = max(maxProfit[i], maxProfit[j]+weights[i])
print(max(maxProfit))
# Using the end point:
jobs.sort(key=lambda x:x[1])
weights = [row[-1] for row in jobs]
maxProfit = [row[-1] for row in jobs]
for i in range(len(jobs)-1,-1,-1):
    for j in range(i,-1,-1):
        if(i==j):
            continue
        if jobs[i][0] >= jobs[j][1]:
            maxProfit[i] = max(maxProfit[i], maxProfit[j]+weights[i])
print(max(maxProfit))
