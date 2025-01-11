#You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
#Return the count of days when the employee is available for work but no meetings are scheduled.
#Note: The meetings may overlap.
days = 10
meetings = [[5,7],[1,3],[9,10]]
a=[]
for i in meetings:
    b=[i for i in range(i[0],i[1]+1)]
    a+=b
a=list(set(a))

