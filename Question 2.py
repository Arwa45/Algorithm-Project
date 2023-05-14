jobs = [[1, 6, 6], [2, 5, 5],[5, 7, 5], [6, 8, 3]]
jobs.sort(key=lambda x:x[0])
weights = [row[-1] for row in jobs]
maxProfit = [row[-1] for row in jobs]
#using start point
for i in range(len(jobs)):
    for j in range(i):
        if(i==j):
            continue
        if jobs[j][1] <= jobs[i][0]:
            maxProfit[i] = max(maxProfit[i], maxProfit[j]+weights[i])
print(max(maxProfit))
