
# Define a function named "max_profit" that takes a list of jobs as input.

# Sort the list of jobs in decreasing order of their profits.

# Initialize a scheduling table with zeros for each possible deadline.

# Set the maximum deadline for the scheduling table to the deadline of the job with the highest deadline in the list of jobs.

# Loop through each job in the list of jobs.

# For each job, find the latest available time slot in the scheduling table by looping backwards through the scheduling table from the job's deadline.

# If an available time slot is found, schedule the job in that time slot, update the count of jobs done and the total profit earned.

# Return the count of jobs done and the total profit earned.

def max_profit(jobs):
  # Sort the jobs in decreasing order of their profits
  #First we sort our jobs in decreasing order of their profits  
  #and it will acsses x[2] of the tabel which is job profit 
  jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
  # Initialize the scheduling table
  print(jobs)
  n = len(jobs)
  max_deadline = max(jobs, key=lambda x: x[1])[1]
  print(max_deadline)
  #time slot is list  contains from 5 zeros
  table = [0] * (max_deadline+1)
  # Schedule the jobs
  count = 0
  profit = 0
  for i in range(n):
    # Find the latest available time slot for this job
    for j in range(jobs[i][1], 0, -1):
      
      if table[j] == 0: 
        table[j] = jobs[i][0]
        no_of_jobs += 1
        profit += jobs[i][2]
        break
      #Return the count of the jobs done and total earned
  return no_of_jobs, profit

jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
no_of_jobs, profit = max_profit(jobs)
print("Number of jobs done:", no_of_jobs)
print("Maximum profit:", profit)
 
      

