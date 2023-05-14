#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating a function to schedule our jobs and to get the maximum profits

def schedule_jobs(jobs):

'''First we sort our jobs in decreasing order of their profits 
We used lambda function which is inline function it will take x which is every tabel in the jobs list 
and it will acsses x[2] of the tabel which is job profit '''
    
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    '''Initialize the scheduling table'''
    n = len(jobs)
    ##sort the jobs by deadline decreasing and get the max deadline
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    ##time slot is list  contains from 5 
    table = [0] * (max_deadline+1)

    # Schedule the jobs
    count = 0
    profit = 0
    for i in range(n):
        # Find the latest available time slot for this job  #in range i don't reach to zero the min index is 1
        for j in range(jobs[i][1], 0, -1):
            if table[j] == 0:
                table[j] = jobs[i][0]#put  the id of this job in the table of time slot
                count += 1
                profit += jobs[i][2]
                break

    return count, profit,table


# In[ ]:


jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
count, profit,table = schedule_jobs(jobs)
print("Number of jobs done:", count)
print("Maximum profit:", profit)
#the table after i put id in it when the time spot is empty 
print("table is",table)

