# Define a function named "max_profit" that takes a list of jobs as input.

# Sort the list of jobs in decreasing order of their profits.

# Initialize a scheduling table with zeros for each possible deadline.

# Set the maximum deadline for the scheduling table to the deadline of the job with the highest deadline in the list of jobs.

# Loop through each job in the list of jobs.

# For each job, find the latest available time slot in the scheduling table by looping backwards through the scheduling table from the job's deadline.

# If an available time slot is found, schedule the job in that time slot, update the count of jobs done and the total profit earned.

# Return the count of jobs done and the total profit earned.
