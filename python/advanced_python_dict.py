# Q6

import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]    
 
# Creating the dictionary in the specified format

faculty_dict = {}
for x in list1:
    if x['name'].split()[-1] not in faculty_dict:
        faculty_dict.update({ x['name'].split()[-1]:[[x[' degree'], x[' title'][:-17],x[' email']]]})
    else:
        faculty_dict[x['name'].split()[-1]].append([x[' degree'],x[' title'][:-17],x[' email']])                      
                              
print(faculty_dict)
