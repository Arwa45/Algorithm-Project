
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
  jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
  # Initialize the scheduling table
  print(jobs)
  n = len(jobs)
  max_deadline = max(jobs, key=lambda x: x[1])[1]
  print(max_deadline)
  table = [0] * (max_deadline+1)
  # Schedule the jobs
  count = 0
  profit = 0
  for i in range(n):
    # Find the latest available time slot for this job
    for j in range(jobs[i][1], 0, -1):
 
      table[j] = jobs[i][0]

