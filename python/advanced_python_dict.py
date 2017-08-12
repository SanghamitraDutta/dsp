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
           
# Printing the first 3 key value pairs of the dicitonary       
count=0
for k,v in faculty_dict.items():
    if count<3:
        print(k,':',v)
        count += 1

#Q6 using re
import csv
import re 

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]
    '''
    for x in list1:
        print (x)
    '''
# Creating dictionary with last name as key    
faculty_dict = {}
for i in list1:
    L_name = re.search(r'\b[A-Z]{1}[a-z]+$',i['name']).group()
    if L_name in faculty_dict:
        faculty_dict[L_name].append([i[' degree'],i[' title'],i[' email']])
    else:
        faculty_dict.update({ L_name : [[i[' degree'],i[' title'],i[' email']]]})

for i in faculty_dict:
    print(i,':', faculty_dict[i])


# Q7
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]        

# Creating the dictionary in the specified format
                   
professor_dict = { tuple(x['name'].split()[0],x['name'].split()[-1]):[x[' degree'], x[' title'][:-17], x[' email']] for x in list1 }
  
# Printing the first 3 key value pairs of the dicitonary    
count=0
for k,v in professor_dict.items():
    if count<3:
        print(k,':',v)
        count += 1


# Q8
import csv

with open('faculty.csv') as f:
    data = list(csv.DictReader(f))
    list1 = [ dict(x) for x in data ]         

# Creating the dictionary in the specified format
                   
professor_dict = { (x['name'].split()[-1],x['name'].split()[0]):[x[' degree'], x[' title'][:-17], x[' email']] for x in list1 }
   
# Printing the first 3 key value pairs of the dicitonary       
count=0
for k,v in professor_dict.items():
    if count<3:
        print(k,':',v)
        count += 1
        
