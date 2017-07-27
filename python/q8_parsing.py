# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import csv
from operator import itemgetter

with open("football.csv") as f:
       data = list(csv.reader(f))
       list1= [dict(zip(data[0],x)) for x in data]
  
del list1[0]

goal_diff_list = [[x["Team"],int(x["Goals"])-int(x["Goals Allowed"])] for x in list1]
goal_diff_list.sort(key = itemgetter(1))
print(goal_diff_list)       
print("Team with the smallest difference in ‘for’ and ‘against’ goals is {} with a difference of {}.".format(goal_diff_list[0][0],goal_diff_list[0][1]))
      
goal_diff_list2 = [[x["Team"],abs(int(x["Goals"])-int(x["Goals Allowed"]))] for x in list1]
goal_diff_list2.sort(key = itemgetter(1))
print("Team with the smallest absolute difference in ‘for’ and ‘against’ goals is {} with an absolute difference of {}.".format(goal_diff_list2[0][0],goal_diff_list2[0][1]))
      
